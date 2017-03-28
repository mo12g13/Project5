
def validata_user_input_choice():

    while True:
        try:
            value_enter = int(input("Please enter a valid number: "))

            if value_enter >=0:
                break
        except ValueError:
            print("Please enter a valid number")
            continue
    return value_enter