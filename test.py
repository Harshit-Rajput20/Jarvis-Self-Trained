from pynput import keyboard

def on_press(key):
    try:
        print(f'Key {key.char} with code {key.vk} pressed')
    except AttributeError:
        print(f'Special key {key} pressed')

def on_release(key):
    print(f'Key {key} released')

# Set up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
