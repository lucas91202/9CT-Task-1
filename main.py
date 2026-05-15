from data_module import options, numerical, social_media, random_social_media, menu, view_datset, filtersearch, search_data, graph, view_visualisation

def main():
    menu()
    while True:
        choice = int(input("Choose an option from 1-6: ").strip())
        while choice not in [1, 2, 3, 4, 5, 6]:
            print("Invalid input.")
            choice = int(input("Choose an option from 1-6: ").strip())
        if choice == 1:
            view_datset()
        elif choice == 2: 
            search_data()
        elif choice == 3:
            print(numerical)
        elif choice == 4:
            print("Update data entry")
        elif choice == 5:
            print("save data")
        elif choice == 6:
            break


if __name__ == "__main__":
    main()
