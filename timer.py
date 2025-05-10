import time
def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        time_format = f'{mins:02d}:{secs:02d}'
        print(time_format, end='\r')
        time.sleep(1)
        seconds -= 1
    print("Time's up...!")
try:
    total_seconds = int(input("Enter time in seconds: "))
    if total_seconds <= 0:
        print("Please enter a postive number.")
    else:
        countdown_timer(total_seconds)
except ValueError:
    print("Invalid input. please enter an integer")

