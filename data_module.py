import matplotlib.pyplot as plt
import pandas as pd
import os
import sys
import time
options = ['Age', 'Daily Screen Time', 'Social Media Hours', 'Sleep Hours', 'Study Work Hours', 'Productivity Score', 'Stress Level', 'Platform']

xval = {
    "age" : ['0-18', '19-25', '26-35', '36-45', '46-55'],
    "daily_screen_time" : ['0-3', '3-6', '6-9', '9-12', 0],
    "social_media_hours" : ['0-3', '3-6', '6-9', 0, 0],
    "sleep_hours" : ['0-3', '3-6', '6-9', 0, 0],
    "study_work_hours" : ['0-3', '3-6', '6-9', '9-12', 0],
    "productivity_score" : ['0-25', '25-50', '50-75', '75-100', 0],
    "average" : [0, 0, 0, 0, 0]
}

df = pd.DataFrame(xval)

social_media = pd.read_csv('social_media_sleep_stress_productivity_11000.csv',
                            index_col=False,
                            header= None,
                            names=['user_id', 'age', 'daily_screen_time_hours', 'social_media_hours', 'sleep_hours', 'exercise_minutes', 'study_work_hours', 'productivity_score', 'stress_level', 'platform'],
                            )
random_social_media = social_media.sample(n=300)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def at(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
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
    at("Viewing dataset...\n", 0.05)
    num = len(social_media.columns)
    if num == 10:
        social_media.drop(columns=['user_id', 'exercise_minutes'], inplace=True)
        print(social_media)
    else:
        print(social_media)

def filtersearch():
    if filter not in ["stress_level", "platform"]:
        at("1. Find the average\n2. Search all entries for a number\n3. Sort frequency by ascending or descending\n4. Find values between two ranges\n5. Exit\nChoose an option from 1-5: ")
        filter2 = int(input())
        while filter2 not in [1, 2, 3, 4, 5]:
            at("1. Find the average\n2. Search all entries for a number\n3. Sort frequency by ascending or descending\n4. Find values between two ranges\n5. Exit\nChoose an option from 1-5: ")
            filter2 = int(input())
        if filter2 == 1:
            average = social_media.loc[:, [f'{filter}']].mean()
            at(average.to_string())
        elif filter2 == 2:
            at("Enter the number or decimal you would like to search for: ")
            userentry = float(input())
            valuecount = social_media[filter].value_counts().get(userentry, 0)
            at(f"Occurences of {userentry}: {valuecount}") #show the rows with the number?
        elif filter2 == 3:
            at("Enter how you would like to sort the data(ascending/descending): ")
            ascdsc = input().strip().lower()
            while ascdsc not in ['ascending', 'descending']:
                at("Enter how you would like to sort the data(ascending/descending): ")
                ascdsc = input().strip().lower()
            if ascdsc == "ascending":
                asc = social_media[filter].value_counts(ascending=True)
                at(asc.to_string())
            else:
                dsc = social_media[filter].value_counts(ascending=False)
                at(dsc.to_string())
        elif filter2 == 4:
            at("Enter the lower number of the range: ")
            val1 = float(input())
            at("Enter the higher number of the range: ")
            val2 = float(input())
            valu = social_media[filter].value_counts().sort_index()
            value = valu.loc[val1:val2]
            at(value.to_string())
        elif filter2 == 5:
            search_data()
    else:
        at("1. Search for amounts of each word\n2. Exit\nChoose an option from 1-2: ")
        filter3 = int(input())
        while filter3 not in [1, 2]:
                    at("1. Search for amounts of each word\n2. Exit\nChoose an option from 1-2: ")
                    filter3 = int(input())
        if filter3 == 1:
            if filter == "stress_level":
                at("Options: Low, Medium, High\nEnter the corresponding stress level: ")
                userentry1 = input().capitalize()
                while userentry1 not in ['Low', 'Medium', 'High']:
                    at("Invalid")
                    at("Options: Low, Medium, High\nEnter the corresponding stress level: ")
                    userentry1 = input().capitalize()
                valuecount = social_media[filter].value_counts().get(userentry1, 0)
                at(f"Occurences of {userentry1}: {valuecount}")
            elif filter == "platform":
                at("Options: Twitter, Youtube, Snapchat, LinkedIn, Instagram\nEnter the corresponding platform: ")
                userentry2 = input().capitalize()
                while userentry2 not in ['Twitter', 'Youtube', 'Snapchat', 'Linkedin', 'Instagram']:
                    at("Invalid")
                    at("Options: Twitter, Youtube, Snapchat, LinkedIn, Instagram\nEnter the corresponding platform: ")
                    userentry2 = input().capitalize()
                if userentry2 == "Linkedin":
                    userentry2 = userentry2[:6]+"I"+userentry2[7:]
                    valuecount = social_media[filter].value_counts().get(userentry2, 0)
                    at(f"Occurences of {userentry2}: {valuecount}")
                elif userentry2 == "Youtube":
                    userentry2 = userentry2[:3]+"T"+userentry2[4:]
                    valuecount = social_media[filter].value_counts().get(userentry2, 0)
                    at(f"Occurences of {userentry2}: {valuecount}") 
                else:
                    valuecount = social_media[filter].value_counts().get(userentry2, 0)
                    at(f"Occurences of {userentry2}: {valuecount}")

        elif filter3 == 2:
            search_data()   

def search_data():
    global filter
    at("Choose a topic to sort:\nAge, Daily Screen Time Hours, Social Media Hours, Sleep Hours, Study Work Hours, Productivity Score, Stress Level, Platform: ")
    fil = input().lower()
    filter = fil.replace(" ", "_")
    filtersearch()

def graph(x, y, z):
        word = val.sort_values(ascending=False) #find averages of y value and use groups of x
        word.plot(
                kind= 'bar',
                x= x,
                y= y,
                color='blue',
                alpha=0.3,
                title=f'{x} vs {z}'
                )
        plt.show()

def graph2(x, y, z):    
        df2 = df[df[x] != 0]  
        df2.plot(
                kind= 'bar',
                x= x,
                y= y,
                color='blue',
                alpha=0.3,
                title=f'{x} vs {z}'
                )
        plt.show()

def graph3(x, y, z):    
        df2 = df[df[x] != 0]  
        df2.plot(
                kind= 'bar',
                x= x,
                y= y,
                color='blue',
                alpha=0.3,
                title= z
                )
        plt.show()

def graph4(x, y, z):
        word = val.sort_values(ascending=False) #find averages of y value and use groups of x
        word.plot(
                kind= 'bar',
                x= x,
                y= y,
                color='blue',
                alpha=0.3,
                title=z
                )
        plt.show()

def graph5(x, y, z):      
        random_social_media.plot(
                kind= 'scatter',
                x= x,
                y= y,
                color='blue',
                alpha=0.3,
                title= z
                )
        plt.show()

def average(x, y): 
    global val
    l = 0
    if x in ["stress_level", "platform"]:
        val = social_media.groupby(x)[y].mean()
        if x == "stress_level":
            val = val.reindex(['Low', 'Medium', 'High'])
    else:
        for z in df[x]:
            split = df[x].str.split("-", expand=True)
            split.columns = ['a', 'b']
            if split['a'].iloc[l] == False:
                pass
            else:
                df['average'] = df['average'].astype('float64')
                nums = float(split['a'].iloc[l])
                nums2 = float(split['b'].iloc[l])
                value = social_media.loc[social_media[x].between(nums, nums2), y].mean()
                df.at[l, 'average'] = value
                l += 1

def view_visualisation(): 
    global first
    global second_value
    global second_val
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
                if first_value not in ["stress_level", "platform"]:
                    average(first_value, second_value)
                    graph2(first_value, 'average', second_value)
                else:
                    average(first_value, second_value)
                    graph(first_value, 'average', second_value)

    if choice == '1':
        tp = int(input("Options:\n1. Bar Graphs\n2. Scatter Plot\n3. Exit\nChoose an option from 1-3: "))
        if tp == 1:
            graph_options = int(input("Options:\n1. Social media hours vs sleep hours\n2. Social media hours vs stress level\n3. Social media hours vs productivity score\nChoose an option from 1-3 or 0 to exit: "))
            if graph_options == 1:
                average('social_media_hours', 'sleep_hours')
                graph3('social_media_hours', 'average', 'Social media effect on sleep')
            elif graph_options == 2:
                average('stress_level', 'social_media_hours')
                graph4('stress_level', 'average', 'Social media effect on stress levels')
            elif graph_options == 3:
                average('social_media_hours', 'productivity_score')
                graph3('social_media_hours', 'average', 'Social media effect on productivity level out of 100')
            elif graph_options == 0:
                print('Exiting...')
                view_visualisation()
        elif tp == 2:
            graph_options = int(input("Options:\n1. Social media hours vs sleep hours\n2. Social media hours vs productivity score\nChoose an option from 1-2 or 0 to exit: "))
            if graph_options == 1:
                graph5('social_media_hours', 'sleep_hours', 'Social media effect on sleep')
            elif graph_options == 2:
                graph5('social_media_hours', 'productivity_score', 'Social media effect on productivity')
            elif graph_options == 0:
                print('Exiting...')
                view_visualisation()
        elif tp == 3:
            print('Exiting...')
            view_visualisation()
