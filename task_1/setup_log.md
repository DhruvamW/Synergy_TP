# Setup Log – Task 1

This log records the exact commands used to set up Task 1, in the order
they were run.

## 1. Clone Repository from Github

```bash
PS D:\Synergy> git clone https://github.com/DhruvamW/Synergy_TP.git
```


## 2. Create the virtual environment (inside task_1)

```bash
python -m venv task_1/venv
```

## 3. Activate the virtual environment

```cmd
task_1\venv\Scripts\activate.bat
```

## 4. Install a package

```bash
pip install --upgrade pip
pip install requests
```

## 5. Generate requirements.txt

```bash
pip freeze > requirements.txt
```

## 7. Create the script and docs

Content for each file was then written using VS Code.

## 8. Create the root .gitignore

created in repository

(Edited to exclude venv/, __pycache__/, and OS-specific files.)

## 9. Verify the script runs from the repo root

```bash
python task_1/src/hello.py
```
Output:
Hello from Task 1!
Python virtual environment is working.

## 10. Stage and commit changes

```bash
git add .
git commit -m "Add Task 1: venv setup, hello.py, requirements, and docs"
```

## 11. Confirm the final commit hash

```bash
git log -1 --format="%H"
```
