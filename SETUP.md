# Setup Instructions

How to set up a virtual environment and install the dependencies in `requirements.txt`.

## 1. Create a virtual environment

From the repo root:

```
python -m venv .venv
```

This creates a `.venv` folder containing an isolated Python install.

## 2. Activate the virtual environment

**Windows (PowerShell):**
```
.venv\Scripts\Activate.ps1
```

**Windows (cmd.exe):**
```
.venv\Scripts\activate.bat
```

**macOS/Linux (bash/zsh):**
```
source .venv/bin/activate
```

Your terminal prompt should now show `(.venv)` at the start, confirming the environment is active.

## 3. Install dependencies

```
pip install -r requirements.txt
```

This installs pandas (version pinned in `requirements.txt`) into the virtual environment.

## 4. Run the scripts

With the virtual environment still active, run scripts from the repo root so relative paths like `data/titanic.csv` resolve correctly:

```
python code/titanic.py
```

## 5. Deactivate when done

```
deactivate
```

## Adding new dependencies later

If a script needs a new package, install it while the virtual environment is active, then update `requirements.txt` so others can reproduce the environment:

```
pip install <package>
pip freeze > requirements.txt
```
