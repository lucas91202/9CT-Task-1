


def menu():
    def ui_line():
        print("_________________________________________________________________________________")
        print("|                                                                               |")
        print("|                       ===== Data Viewer Interface =====                       |")
        print("|    Options:                                                                   |")
        print("|                                                                               |")
        print("|        1. View dataset                                                        |")
        print("|        2. View visualisation                                                  |")
        print("|        3. Search or filter for data                                           |")
        print("|        4. Update a data entry                                                 |")
        print("|        5. Save changes                                                        |")
        print("|        6. Exit                                                                |")
        print("|                                                                               |")
        print("|_______________________________________________________________________________|")



    while True:
        ui_line()
        choice = int(input("Choose an option from 1-6: ").strip())
        while choice not in [1, 2, 3, 4, 5, 6]:
            print("Invalid input.")
            choice = int(input("Choose an option from 1-6: ").strip())
        if choice == 1:
            print("view dataset")
        elif choice == 2: 
            print("View visualisation")
            visual_choice = input(f'What data would you like to visualise? ') #enter options
            print(f"Show dataset for {visual_choice}")
        elif choice == 3:
            print("Search or filter for data")
            #find averages/medians/range/mode
        elif choice == 4:
            print("Update data entry")
        elif choice == 5:
            print("save data")
        elif choice == 6:
            break
        break

if __name__ == "__main__":
    menu()