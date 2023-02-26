import time

start_time = None

while True:
    # Get user input
    user_input = input("Enter a command ('start' or 'stop'): ")
    
    # Check the user's input
    if user_input == "start":
        if start_time is not None:
            print("The timer is already running.")
        else:
            start_time = time.time()
            print("Timer started.")
    elif user_input == "stop":
        if start_time is None:
            print("The timer is not running.")
        else:
            end_time = time.time()
            elapsed_time = end_time - start_time
            
            # Convert elapsed time to hours, minutes, and seconds
            hours = int(elapsed_time // 3600)
            minutes = int((elapsed_time % 3600) // 60)
            seconds = int(elapsed_time % 60)
            
            print(f"Elapsed time: {hours} hours, {minutes} minutes, {seconds} seconds.")
            start_time = None
    else:
        print("Invalid command.")
