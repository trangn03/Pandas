import pandas as pd
from datetime import datetime, timedelta
import win32com.client as win32

# 1. Load the Excel data 
file_path = r"M:\AS 9100 D\Approved Supplier List Certificates [INTERNAL]\F-11 APPROVED SUPPLIER LIST - 9.12.2025.xlsx"
df = pd.read_excel(file_path, header=3)

# 2. Clean the column headers
df.columns = df.columns.astype(str).str.replace('\n', ' ').str.strip()

# 3. Filter for Active suppliers only
active_suppliers = df[df['Select'] == 'Active'].copy()

# 4. Handle the mixed data and fill missing processes
active_suppliers = active_suppliers[active_suppliers['Date'] != 'Not Cert']
active_suppliers['Date'] = pd.to_datetime(active_suppliers['Date'], errors='coerce')

# Fill any blank cells in the Process column with 'N/A' so the email looks clean
active_suppliers['Process'] = active_suppliers['Process'].fillna('N/A')

# 5. Define the expiration window (30 days from today)
today = pd.to_datetime('today')
warning_window = today + pd.Timedelta(days=30)

# 6. Find suppliers whose expiration date falls within the warning window
expiring_soon = active_suppliers[
    (active_suppliers['Date'] <= warning_window) & 
    (active_suppliers['Date'].notna())
]

# 7. Generate ONE Outlook email with an HTML table of all expiring certificates
if not expiring_soon.empty:
    outlook = win32.Dispatch('outlook.application')
    
    # Updated HTML body to include a 3-column table
    html_body = """
    <html>
    <head>
    <style>
        table { border-collapse: collapse; width: 80%; font-family: Calibri, Arial, sans-serif; }
        th, td { border: 1px solid #dddddd; text-align: left; padding: 8px; }
        th { background-color: #f2f2f2; color: #333333; }
        .date-col { color: #d9534f; font-weight: bold; } 
    </style>
    </head>
    <body style="font-family: Calibri, Arial, sans-serif; font-size: 11pt; color: #000000;">
        <p>Hello,</p>
        <p>The following supplier certifications are expiring within the next 30 days (or have already expired):</p>
        
        <table>
            <tr>
                <th>Approved Supplier</th>
                <th>Approved Process</th>
                <th>Expiration Date</th>
            </tr>
    """
    
    # Loop through the rows to add each supplier, process, and date to the table
    for index, row in expiring_soon.iterrows():
        supplier = row['Approved Supplier']
        process = row['Process']
        exp_date = row['Date'].strftime('%m/%d/%y')
        
        # Add the 3 data cells (<td>) for each row
        html_body += f"""
            <tr>
                <td>{supplier}</td>
                <td>{process}</td>
                <td class="date-col">{exp_date}</td>
            </tr>
        """
    
    # Add the closing HTML tags
    html_body += """
        </table>
        <br>
        <p>Please review the AS 9100 D supplier portal to request updated documentation.</p>
    </body>
    </html>
    """
    
    # Create the single email
    mail = outlook.CreateItem(0)
    
    # UPDATE THIS LINE: Put your personal work email address inside the quotes
    mail.To = 'your.email@company.com' 
    
    mail.Subject = "ACTION REQUIRED: Weekly NADCAP Expiration Report"
    mail.HTMLBody = html_body
    
    # mail.Send() 
    mail.Display() 

print("Script execution complete. Check Outlook for the drafted report.")