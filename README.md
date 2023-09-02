# Desktop Scheduler 💻 🕙

## Introduction 📄

Desktop Scheduler is a Python application that allows users to schedule automatic backups of files and directories.

## Features ✨

- Schedule automatic backups
- Backup multiple sources and destinations
- User-friendly GUI

## Installation 📥

Clone the repository and install the required packages:

```sh
git clone https://github.com/yourusername/desktop-scheduler.git
cd desktop-scheduler
pip install -r requirements.txt
```

## Usage 🔧

Run the application:

```sh
python main.py
```

Follow the instructions in the GUI to set up your backups.

## Automation ⚙️

### Windows

1. Open the Task Scheduler and choose to create a new task.
2. In the "General" tab, give your task a name.
3. In the "Triggers" tab, create a new trigger that starts the program daily at your preferred time.
4. In the "Actions" tab, create a new action that starts the program. The action should start the Python interpreter, with the arguments being the path to your script. For example, if Python is installed at `C:\Python39\python.exe` and your script is located at `C:\path\to\script.py`, the action should start the program `C:\Python39\python.exe` with the add arguments `C:\path\to\script.py`.
5. Click "OK" to create the task.

### Linux

1. Open your crontab file by running `crontab -e` in the terminal.
2. Add a new line in the following format:
```
MM HH * * * /path/to/python /path/to/script.py
```
Replace `MM` with the minute and `HH` with the hour you want to run the script, and `/path/to/python` and `/path/to/script.py` with the paths to your Python interpreter and script, respectively.
3. Save and close the file.

Your script will now run automatically at the scheduled time.

---

Remember to adjust the paths according to your setup. This is a basic guide and may need to be adapted depending on the user's specific configuration.

## License 📑

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Screenshots 📷

![image](https://github.com/ken3stokes/Desktop_Backup_Scheduler/assets/138406955/fb104684-f0c2-43c2-88ac-1a868a17f885)



