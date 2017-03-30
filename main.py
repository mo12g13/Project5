import process_data
import input_validation
import user_interface

# A various action to be performed base on the user choice


def main():
    user_interface.display_menu_option()

    while True:
        user_interface.display_menu_option()
        value_enter = input_validation.validata_user_input_choice()
        if value_enter == 1:
            process_data.rape_violent_homicide_robbeies_percapita_from_1975_to_2015()
            continue

        elif value_enter == 2:
            process_data.rape_and_violent_crime_percapita_from_2012_2015()
            continue

        elif value_enter == 3:
            process_data.rape_crime_per_capita_from_1975_to_2015()

        elif value_enter == 4:
            process_data.violent_crime_per_capita_from_2012_to_2015()

        elif value_enter == 5:
            process_data.assault_crime_per_capita_from_1975_2015()

        elif value_enter == 6:
            process_data.average_rape_crime_from_1975_2015()

        elif value_enter == 7:
            process_data.average_assault_crime_from_1975_2015()

        elif value_enter == 0:
            break

if __name__=='__main__':
    main()