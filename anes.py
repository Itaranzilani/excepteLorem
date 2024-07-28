import multiprocessing

def LED_control(duration, state):
    # Function logic here
    print(f"LED control started with duration {duration} and state {state}")

duration = 5
LED_STATE_FLASHING = True

# Create and start the process
multiprocessing.Process(target=LED_control, name="LED", args=(duration, LED_STATE_FLASHING)).start()
