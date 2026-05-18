from data_module import at, clear_screen, pause, menu, view_datset, search_data, view_visualisation, update_data, save

def main():
    clear_screen()
    at('Starting...', 0.05)
    pause(1)
    clear_screen()
    pause(1)
    menu()
    while True:
        at("Choose an option from 1-6: ", 0.05)
        choice = input()
        while choice not in ['1', '2', '3', '4', '5', '6']:
            at("Invalid input.", 0.05)
            pause(1)
            clear_screen()
            menu()
            at("Choose an option from 1-6: ", 0.05)
            choice = input()
        clear_screen()
        if choice == '1':
            view_datset()
        elif choice == '2': 
            search_data() #small fixes to work on
        elif choice == '3':
            view_visualisation() #fix text, change graphs y axis to not start from 0
        elif choice == '4':
            update_data()
        elif choice == '5':
            save()
        elif choice == '6':
            at('Exiting...', 0.05)
            pause(1)
            clear_screen()
            break

if __name__ == "__main__":
    main()