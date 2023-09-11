import pyautogui
import keyboard

def click_event(event):
    if event.event_type == keyboard.KEY_DOWN and event.name == 'esc':
        # Exit the program when the 'esc' key is pressed
        return False
    else:
        # Get the current mouse coordinates and print them
        x, y = pyautogui.position()
        print(f"Mouse clicked at coordinates (x={x}, y={y})")

print("Click anywhere on the screen to get coordinates. Press 'esc' to exit.")
keyboard.on_press_key('esc', click_event)
keyboard.wait('esc')  # Wait for the 'esc' key to be pressed to exit the program
keyboard.unhook_all()