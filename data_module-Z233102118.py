import matplotlib.pyplot as plt
import pandas as pd
options = ['User ID', 'Age', 'Daily Screen Time', 'Social Media Hours', 'Sleep Hours', 'Study Work Hours', 'Productivity Score', 'Stress Level', 'Platform']

numerical = {
    
}

social_media = pd.read_csv('social_media_sleep_stress_productivity_11000.csv',
                            header= None,
                            names=['user_id', 'age', 'daily_screen_time_hours', 'social_media_hours', 'sleep_hours', 'exercise_minutes', 'study_work_hours', 'productivity_score', 'stress_level', 'platform']
                            )

def menu():
    print("_________________________________________________________________________________")
    print("|                                                                               |")
    print("|                       ===== Data Viewer Interface =====                       |")
    print("|    Options:                                                                   |")
    print("|                                                                               |")
    print("|        1. View dataset                                                        |")
    print("|        2. Search of filter for data                                           |")
    print("|        3. View visualisation                                                  |")
    print("|        4. Update a data entry                                                 |")
    print("|        5. Save changes                                                        |")
    print("|        6. Exit                                                                |")
    print("|                                                                               |")
    print("|_______________________________________________________________________________|")

def view_datset():
    print("Viewing dataset...\n")
    social_media.drop(columns=['user_id', 'exercise_minutes'], inplace=True)
    print(social_media.to_string(index=False))

def search_data():
    s

def graph(x, y, z):
    social_media.plot(
               kind=z,
               x= x,
               y= y,
               color='blue',
               alpha=0.3,
               title=f'{x} vs {y}'
              )
    plt.show()

def view_visualisation(): #unfinished work on later
    choice = input("Would you like to view prechosen graphs(recommended) or choose your own variables? Enter 1 for prechosen, 2 for custom variables or 0 to exit: ")
    while choice not in ['1', '2']:
        print("Invalid input")
        choice = input("Would you like to view prechosen graphs(recommended) or choose your own variables? Enter 1 for prechosen and 2 for custom variables.")
    if choice == '2':
        first = input(f"Choose the x value of the graph: {", ".join(options)}. Enter 0 to exit. ").lower()
        if first == "0":
            print("Exiting...")
            menu()
        elif first != "0":
            second = input(f"Choose the y value of the graph: {", ".join(options)}. Enter 0 to exit. ").lower()
            if second == "0":
                print("Exiting...")
                menu()
            elif first == second:
                while first == second:
                    print("The two values can not be the same.")
                    second = input(f"Choose the second value to compare with: {", ".join(options)}. Enter 0 to exit. ").lower()
                    if second == "0":
                        print("Exiting...")
                        menu()
        else:
            first_value = first.replace(" ", "_")
            second_value = second.replace(" ", "_")
            graph_type = input("What kind of graph would you like? Options: scatter, bar, pie.").strip().lower()
            graph(first_value, second_value, graph_type)
    if choice == '1':
        graph_options = int(input("Options:\n1. Social media hours vs sleep hours\n2. Social media hours vs stress level\n3. Social media hours vs productivity score\nChoose an option from 1-3 or 0 to exit: "))
        if graph_options == 1:
            graph('social_media_hours', 'sleep_hours', 'scatter')
        if graph_options == 2:
            graph('stress_level', 'social_media_hours', 'bar')

view_visualisation()