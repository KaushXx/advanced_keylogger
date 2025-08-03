# 🧠 Advanced Python Keylogger

This is an advanced keylogger built with Python that can track and log detailed user activity on a Windows system. It’s intended for **educational and ethical use only**, such as learning how keyloggers work or testing endpoint protection systems in a controlled environment.

---

## 🚨 Disclaimer

> ⚠️ This tool is for **educational** and **ethical penetration testing** purposes **only**.  
> Do **not** use this on machines without proper authorization.  
> Misuse can be **illegal** and may result in **criminal charges**.  
> Always follow ethical hacking guidelines.

---

## 🛠 Features

✔️ Logs **active window titles** (detects when the user switches apps)  
✔️ Monitors and logs **clipboard changes** (copy-paste tracking)  
✔️ Logs every **key press** and **key release**  
✔️ Creates a **Windows Registry key** for persistence (optional or for testing)  
✔️ Saves everything in a neatly formatted **log file**

---

## 📂 How It Works

This keylogger uses libraries like:

- `pynput` – for capturing keystrokes
- `win32gui` – to get active window titles
- `pyperclip` – to monitor clipboard changes
- `schedule` & `threading` – for background tasks
- `logging` – to save all activity to a log file
- `platform` – detect operating system

---

## 🚀 Setup

1. Clone the repo:

```bash
git clone https://github.com/kaushxx/advanced-keylogger.git
cd advanced-keylogger
