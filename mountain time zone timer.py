import time
import datetime
import pytz

# Set the time zone to Mountain Time Zone
mt_zone = pytz.timezone('US/Mountain')

start_time = None

while True:
    # Get user input
    user_input = input("Enter a command ('start' or 'stop'): ")
    
    # Check the user's input
    if user_input == "start":
        if start_time is not None:
            print("The timer is already running.")
        else:
            start_time = datetime.datetime.now(mt_zone)
            print(f"Timer started at {start_time.strftime('%Y-%m-%d %H:%M:%S %Z')}.")
    elif user_input == "stop":
        if start_time is None:
            print("The timer is not running.")
        else:
            end_time = datetime.datetime.now(mt_zone)
            elapsed_time = end_time - start_time
            print(f"Elapsed time: {elapsed_time}.")
            start_time = None
    else:
        print("Invalid command.")
