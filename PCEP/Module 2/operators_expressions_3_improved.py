def get_int_input(prompt, min_value, max_value=None):
    while True:
        try:
            value = int(input(prompt))
            if max_value is None:
                if min_value <= value:
                    return value
                print(f"Value must be greater than {min_value}, please try again")
            if min_value <= value <= max_value:
                return value
            print(f"Value must be between {min_value} and {max_value}, please try again.")
        except ValueError:
            print("Invalid input. Please enter an integer")
            
start_hour = get_int_input("Starting time (hours 0-23): ",0, 23)
start_mins = get_int_input("Starting time (mins 0-59): ", 0, 59)
dura = get_int_input("Event duration (minutes): ",0)

dura_hour = dura // 60
dura_mins = dura % 60

end_mins = start_mins + dura_mins

if end_mins >= 60:
    dura_hour += 1
    end_mins %= 60
    
end_hour = (start_hour + dura_hour) % 24

print(f"end time = {end_hour:02d}:{end_mins:02d}")
print()