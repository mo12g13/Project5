import process_data
import input_validation
import user_interface

def main():
    user_interface.display_menu_option()

    while True:
        user_interface.display_menu_option()
        value_enter = input_validation.validata_user_input()
        if value_enter == 1:
            process_data.rape_violent_homicide_robbeies_percapita_from_1975_to_2015()
            continue

        elif value_enter == 2:
            process_data.rape_and_violent_crime_from_2012_2015()
            continue

        elif value_enter == 0:
            break
if __name__=='__main__':
    main()