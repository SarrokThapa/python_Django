### What is PIP?
pip = Python Package Installer
It is used to install, update, and remove external Python libraries/modules.
    ```pip install django```
   ```pip install numpy```

# What does pip do?

pip allows you to:

1. Install Python packages
2. Update packages
3. Uninstall packages
4. See installed packages

# What is pip freeze?
pip freeze shows all installed packages + their versions.
-It is mainly used to create requirements.txt for projects:
``` pip freeze > requirements.txt ```
-This file helps others install exactly the same packages using:
```pip install -r requirements.txt```


# How to Install a virtual environment(venv)

Step1: Instal virtualenv
```pip install virtualenv```

Step 2: Create a virtual environment
```virtualenv env```
Step 3: Activate the virtual environment
```env\Scripts\activate```
You will see (env) appear in the terminal means it's activated.
Step 4: Deactivate when done
```deactivate```


### What is UV
uv is a blazingly fast Python tool written in Rust that can:

Create virtual environments
Install packages
Manage Python versions
Run Python scripts directly
Replace pip & virtualenv

It is becoming very popular because it is much faster than pip.

### What is a Virtual Environment (venv)?
A virtual environment is a separate, isolated workspace where you install Python packages only for one project.
It keeps your project’s dependencies separate from your system Python.

## Why do we need a virtual env?
1. To avoid version conflicts
Different projects need different package versions.
Example:
Project A needs Django 5
Project B needs Django 4

Without a virtual env, they would conflict, because your system can’t install both at once.

2. Keep the project clean & portable
Everything your project needs stays inside the env/ folder.
Easy to share with:
```pip freeze > requirements.txt```
Then others can install exactly the same versions.

3. Protect system Python
Installing packages globally can break your system.
Virtual env keeps everything separate so nothing touches the system Python.

4. Required for Django projects
Django needs many packages (Django, djangorestframework, pillow, etc.)
Virtual env keeps all these dependencies only inside the project.

# When should you use virtual env?
Always — anytime you start a new:
Python project
Django project
Flask project
Machine learning/AI project





