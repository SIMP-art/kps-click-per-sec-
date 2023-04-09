import time,os
import keyboard

def calculate_typing_speed(dur:int) -> float:
    start_time = time.time()
    num_keys = 0
    while True:
        keyboard.read_event()
        num_keys += 1
        elapsed_time = time.time() - start_time
        if elapsed_time >= dur:
            break
    return num_keys // elapsed_time

if __name__ == "__main__":
    print("Press any key to start...")
    keyboard.read_event()
    print("Listening...")
    typing_speed = calculate_typing_speed(5) # Listen for 5 seconds, you can change if you want
    os.system("cls" if os.name == 'nt' else "clear")
    print(f"You typed {typing_speed} keys per second")
