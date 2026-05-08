


def menu():
    def ui_line():
        print("---------------------------------------------------------------------------------")
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
        print("---------------------------------------------------------------------------------")



    while True:
        ui_line()
        choice = int(input("Choose an option from 1-6: ").strip())
        while choice not in [1, 2, 3, 4, 5, 6]:
            print("Invalid input.")
            choice = int(input("Choose an option from 1-6: ").strip())
        if choice == 1:
            print("view dataset")
        elif choice == 2: 
            
        break

if __name__ == "__main__":
    menu()