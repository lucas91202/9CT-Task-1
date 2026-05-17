from data_module import at, clear_screen, menu, view_datset, search_data, view_visualisation

def main():
    clear_screen()
    at('Starting...', 0.2)
    clear_screen()
    menu()
    while True:
        at("Choose an option from 1-6: ", 0.05)
        choice = int(input())
        while choice not in [1, 2, 3, 4, 5, 6]:
            at("Invalid input.", 0.05)
            at("Choose an option from 1-6: ", 0.05)
            choice = int(input())
        clear_screen()
        if choice == 1:
            view_datset()
        elif choice == 2: 
            search_data() #small fixes to work on
        elif choice == 3:
            view_visualisation() #fix text, change graphs y axis to not start from 0
        elif choice == 4:
            print("Update data entry") #work on
        elif choice == 5:
            print("save data") #work on
        elif choice == 6:
            break #add exiting screen

if __name__ == "__main__":
    main()