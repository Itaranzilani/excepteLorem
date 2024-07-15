while True:
    position = input("Please enter the position you want (0-8): ")
    try:
        position = int(position)
        if 0 <= position <= 8:
            print(f"You entered a valid position: {position}")
            break
        else:
            print("Error: The position must be between 0 and 8.")
    except ValueError:
        print("Error: Please enter a valid integer.")
