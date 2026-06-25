# Task 1

## Description

This folder contains the deliverable for Task 1 of the Synergy_TP project.
It includes a Python virtual environment setup, a sample script
(`src/hello.py`) that imports and uses the `requests` package, and the
supporting documentation for setup and Linux command usage.

```
task_1/
├── README.md
├── setup_log.md
├── linux_commands.md
├── requirements.txt
├── venv/              (created locally, ignored by .gitignore)
└── src/
    └── hello.py
```

## Setup Instructions

1. Clone the repository and move into it:

```bash
   git clone <your-repo-url>
   cd Synergy_TP
```

2. Move into the `task_1` folder:

```bash
   cd task_1
```

## Create and Activate the Virtual Environment

Create the virtual environment (run once, from inside `task_1/`):

```bash
python -m venv task_1/venv
```

Activate it:

- **cmd:**

```cmd
  task_1\venv\Scripts\activate.bat
```
I knew it worked because my shell prompt wwas prefixed with `(venv)`.

## Setup Requirements

With the virtual environment activated, install the dependencies listed in
`requirements.txt`:

```bash
(venv) D:\Synergy\Synergy_TP>pip freeze > task_1/requirements.txt
```

## Run the Script

Go back to the **Synergy_TP repository root** (one level up from `task_1`)
and run the script from there, with the virtual environment still active:

```bash
cd ..
python task_1/src/hello.py
```

Expected output:

```
Hello from Task 1!
Python virtual environment is working.
```
