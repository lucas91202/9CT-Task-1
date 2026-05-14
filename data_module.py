import matplotlib as plt
import pandas as pd
options = ['Age', 'Daily Screen Time', 'Social Media Hours', 'Sleep Hours', 'Study Work Hours', 'Productivity Score', 'Stress Level', 'Platform']
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

def view_datset():
    social_media = pd.read_csv('social_media_sleep_stress_productivity_11000.csv',
                               header= None,
                               names=['user_id', 'age', 'daily_screen_time_hours', 'social_media_hours', 'sleep_hours', 'exercise_minutes', 'study_work_hours', 'productivity_score', 'stress_level', 'platform']
                               )
    social_media.drop(columns=['user_id', 'exercise_minutes'], inplace=False)
    print(social_media)

def view_visualisation():
    first_value = input(f"Choose the first value to compare with: {options}. Enter 0 to exit.")
    second_value = input(f"Choose the second value to compare with: {options}. Enter 0 to exit")
    if first_value or second_value == 0:
        menu()
    else:
        while second_value == first_value:
            print("The two values can not be the same.")
            second_value = input(f"Choose the second value to compare with: {options}. Enter 0 to exit")
        
    



view_visualisation()