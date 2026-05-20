import matplotlib.pyplot as plt
import pandas as pd
import os
import sys
import time
options = ['Age', 'Daily Screen Time Hours', 'Social Media Hours', 'Sleep Hours', 'Study Work Hours', 'Productivity Score', 'Stress Level', 'Platform']

options1 = ['age', 'daily screen time hours', 'social media hours', 'sleep hours', 'study work hours', 'productivity score', 'stress level', 'platform']

xval = {
    "age" : ['0-18', '19-25', '26-35', '36-45', '46-55'],
    "daily_screen_time_hours" : ['0-3', '3-6', '6-9', '9-12', 0],
    "social_media_hours" : ['0-3', '3-6', '6-9', 0, 0],
    "sleep_hours" : ['0-3', '3-6', '6-9', 0, 0],
    "study_work_hours" : ['0-3', '3-6', '6-9', '9-12', 0],
    "productivity_score" : ['0-25', '25-50', '50-75', '75-100', 0],
    "average" : [0, 0, 0, 0, 0]
}

df = pd.DataFrame(xval)

social_media = pd.read_csv('social_media_sleep_stress_productivity_11000.csv',
                            index_col=False,
                            header= 0,
                            names=['user_id', 'age', 'daily_screen_time_hours', 'social_media_hours', 'sleep_hours', 'exercise_minutes', 'study_work_hours', 'productivity_score', 'stress_level', 'platform'],
                            )

random_social_media = social_media.sample(n=300)

def pause(x):
    time.sleep(x)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def at(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def next():
    at("Press enter to return")
    input()    

def menu():
    print("_________________________________________________________________________________")
    print("|                                                                               |")
    print("|                       ===== Data Viewer Interface =====                       |")
    print("|    Options:                                                                   |")
    print("|                                                                               |")
    print("|        1. View dataset                                                        |")
    print("|        2. Search or filter for data                                           |")
    print("|        3. View visualisation                                                  |")
    print("|        4. Update a data entry                                                 |")
    print("|        5. Save changes                                                        |")
    print("|        6. Exit                                                                |")
    print("|                                                                               |")
    print("|_______________________________________________________________________________|")

def view_datset():
    at("Viewing dataset...\n", 0.05)
    pause(1)
    clear_screen()
    num = len(social_media.columns)
    if num == 10:
        social_media.drop(columns=['user_id', 'exercise_minutes'], inplace=True)
        print(social_media)
    else:
        print(social_media)
    next()
    clear_screen()
    pause(1)
    menu()

def filtersearch():
    clear_screen()
    if filter == '0':
        at("Returning to menu...", 0.05)
        pause(1)
        clear_screen()
        menu()
    elif filter not in ["stress_level", "platform"]:
        social_media[filter] = pd.to_numeric(social_media[filter], errors='coerce')
        at("1. Find the average\n2. Search all entries for a number\n3. Sort frequency by ascending or descending\n4. Find values between two ranges\n5. Exit\nChoose an option from 1-5: ")
        filter2 = input()
        while filter2 not in ['1', '2', '3', '4', '5']:
            at("Invalid input.")
            pause(1)
            clear_screen()
            at("1. Find the average\n2. Search all entries for a number\n3. Sort frequency by ascending or descending\n4. Find values between two ranges\n5. Exit\nChoose an option from 1-5: ")
            filter2 = input()
        if filter2 == '1':
            average = social_media.loc[:, [f'{filter}']].mean()
            at(average.to_string())
            next()
            clear_screen()
            filtersearch()
        elif filter2 == '2':
            at("Enter the number or decimal you would like to search for: ")
            userentry = float(input())
            valuecount = social_media[filter].value_counts().get(userentry, 0)
            at(f"Occurences of {userentry}: {valuecount}")
            next()
            clear_screen()
            filtersearch()
        elif filter2 == '3':
            at("Enter how you would like to sort the data(ascending/descending): ")
            ascdsc = input().strip().lower()
            while ascdsc not in ['ascending', 'descending']:
                at("Enter how you would like to sort the data(ascending/descending): ")
                ascdsc = input().strip().lower()
            if ascdsc == "ascending":
                asc = social_media[filter].value_counts(ascending=True)
                at(asc.to_string())
                next()
                clear_screen()
                filtersearch()
            else:
                dsc = social_media[filter].value_counts(ascending=False)
                at(dsc.to_string())
                next()
                clear_screen()
                filtersearch()
        elif filter2 == '4':
            at("Enter the lower number of the range: ")
            val1 = float(input())
            at("Enter the higher number of the range: ")
            val2 = float(input())
            valu = social_media[filter].value_counts().sort_index()
            value = valu.loc[val1:val2]
            at(value.to_string())
            next()
            clear_screen()
            filtersearch()
        elif filter2 == '5':
            clear_screen()
            search_data()
    else:
        at("1. Search for amounts of each word\n2. Exit\nChoose an option from 1-2: ")
        filter3 = int(input())
        while filter3 not in [1, 2]:
                    at("1. Search for amounts of each word\n2. Exit\nChoose an option from 1-2: ")
                    filter3 = int(input())
        if filter3 == 1:
            if filter == "stress_level":
                clear_screen()
                at("Options: Low, Medium, High\nEnter the corresponding stress level: ")
                userentry1 = input().capitalize()
                while userentry1 not in ['Low', 'Medium', 'High']:
                    at("Invalid")
                    at("Options: Low, Medium, High\nEnter the corresponding stress level: ")
                    userentry1 = input().capitalize()
                valuecount = social_media[filter].value_counts().get(userentry1, 0)
                at(f"Occurences of {userentry1}: {valuecount}")
                next()
                clear_screen()
                filtersearch()
            elif filter == "platform":
                clear_screen()
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
                    next()
                    clear_screen()
                    filtersearch()
                elif userentry2 == "Youtube":
                    userentry2 = userentry2[:3]+"T"+userentry2[4:]
                    valuecount = social_media[filter].value_counts().get(userentry2, 0)
                    at(f"Occurences of {userentry2}: {valuecount}")
                    next()
                    clear_screen()
                    filtersearch() 
                else:
                    valuecount = social_media[filter].value_counts().get(userentry2, 0)
                    at(f"Occurences of {userentry2}: {valuecount}")
                    next()
                    clear_screen()
                    filtersearch()

        elif filter3 == 2:
            clear_screen()
            search_data()   

def search_data():
    global filter
    at("Choose a topic to sort:\nAge, Daily Screen Time Hours, Social Media Hours, Sleep Hours, Study Work Hours, Productivity Score, Stress Level, Platform, Or enter 0 to exit: ")
    fil = input().lower()
    if fil not in options1 + ['0']:
        at("Invalid topic.")
        pause(1)
        clear_screen()
        at("Choose a topic to sort:\nAge, Daily Screen Time Hours, Social Media Hours, Sleep Hours, Study Work Hours, Productivity Score, Stress Level, Platform, Or enter 0 to exit: ")
        fil = input().lower()
    filter = fil.replace(" ", "_")
    filtersearch()

def graph(x, y, z):
        word = val
        word.plot(
                kind= 'bar',
                x= x,
                y= y,
                color='blue',
                alpha=0.3,
                title=f'{x} vs {z}'
                )
        a, b = plt.ylim()
        c = a + (b - a) * 0.75
        plt.ylim(c, b)
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
        a, b = plt.ylim()
        c = a + (b - a) * 0.75
        plt.ylim(c, b)
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
        a, b = plt.ylim()
        c = a + (b - a) * 0.75
        plt.ylim(c, b)
        plt.show()

def graph4(x, y, z):
        word = val
        word.plot(
                kind= 'bar',
                x= x,
                y= y,
                color='blue',
                alpha=0.3,
                title=z
                )
        a, b = plt.ylim()
        c = a + (b - a) * 0.75
        plt.ylim(c, b)
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
    social_media[y] = pd.to_numeric(social_media[y], errors='coerce')
    l = 0
    if x in ["stress_level", "platform"]:
        val = social_media.groupby(x)[y].mean()
        if x == "stress_level":
            val = val.reindex(['Low', 'Medium', 'High'])
        else:
            val = val.reindex(['Twitter', 'YouTube', 'Snapchat', 'LinkedIn', 'Instagram'])
    else:
        for z in df[x]:
            split = df[x].str.split("-", expand=True)
            split.columns = ['a', 'b']
            if split['a'].iloc[l] == False:
                print('a')
                pass
            else:
                social_media_numeric = pd.to_numeric(social_media[x], errors='coerce')
                df['average'] = df['average'].astype('float64')
                nums = float(split['a'].iloc[l])
                nums2 = float(split['b'].iloc[l])
                value = social_media.loc[social_media_numeric.between(nums, nums2), y].mean()
                df.at[l, 'average'] = value
                l += 1

def qgraph():
    global social_media
    clear_screen()
    at("Displaying graph... Close the popup to return to menu")
    first_value = first.replace(" ", "_")
    second_value = second.replace(" ", "_")
    if first_value not in ["stress_level", "platform"]:
        average(first_value, second_value)
        graph2(first_value, 'average', second_value)
    else:
        if first_value == "stress_level":
            order1 = ["Low", "Medium", "High"]
            social_media[first_value] = pd.Categorical(
                social_media[first_value], categories=order1, ordered=True
            )
            social_media = social_media.sort_values(first_value)
            average(first_value, second_value)
            graph(first_value, 'average', second_value)
        else:
            average(first_value, second_value)
            graph(first_value, 'average', second_value)

def view_visualisation(): 
    global first
    global second
    global second_value
    global second_val
    at("Would you like to view prechosen graphs(recommended) or choose your own variables? Enter 1 for prechosen, 2 for custom variables or 0 to exit: ")
    choice = input()
    while choice not in ['1', '2']:
        at("Would you like to view prechosen graphs(recommended) or choose your own variables? Enter 1 for prechosen, 2 for custom variables or 0 to exit: ")
        choice = input()
    if choice == '2':
        at(f"Choose the x value of the graph: {', '.join(options)}. Enter 0 to exit. ")
        first = input().lower()
        while first not in options1+["0"]:
            at("Invalid option.")
            pause(1)
            clear_screen()
            at(f"Choose the x value of the graph: {', '.join(options)}. Enter 0 to exit. ")
            first = input().lower()
        if first == "0":
            at("Exiting...")
            pause(1)
            clear_screen()
            menu()
            return
        elif first != "0":
            at(f"Choose the y value of the graph: {', '.join(options)}. Enter 0 to exit or 1 to go back and edit your x value. ")
            second = input().lower()
            while second not in options1[0:6] + ["0", "1"]:
                at("Invalid option.")
                pause(1)
                clear_screen()
                at(f"Your choice for the x value: {first}")
                at(f"Choose the y value of the graph: {', '.join(options)}. Enter 0 to exit or 1 to go back and edit your x value. ")
                second = input().lower()
            if second == "0":
                at("Exiting...")
                pause(1)
                clear_screen()
                menu()
                return
            elif second == "1":
                at(f"Rechoose the x value of the graph: {', '.join(options)}. Enter 0 to exit. ")
                first = input().lower()
                while first not in options1+['0']:
                    at("Invalid option.")
                    pause(1)
                    clear_screen()
                    at(f"Rechoose the x value of the graph: {', '.join(options)}. Enter 0 to exit. ")
                    first = input().lower()
                if first == "0":
                    at("Exiting...")
                    pause(1)
                    clear_screen()
                    menu()
                    return
                at(f"Choose the y value of the graph: {', '.join(options)}. Enter 0 to exit. ")
                second = input().lower()
                while second not in options1[0:6]+['0']:
                    at("Invalid option.")
                    pause(1)
                    clear_screen()
                    at(f"Your choice for the x value: {first}")
                    at(f"Choose the y value of the graph: {', '.join(options)}. Enter 0 to exit. ")
                    second = input().lower()
                if second == "0":
                    at("Exiting...")
                    pause(1)
                    clear_screen()
                    menu()
                    return
                elif first == second:
                    at("Invalid.")
                    pause(1)
                    clear_screen()
                    at(f"Your choice for the x value: {first}")
                    at(f"Choose the y value of the graph: {', '.join(options)}. Enter 0 to exit. ")
                    second = input().lower()
                    while second not in options1[0:6]+['0']:
                        at("Invalid option.")
                        pause(1)
                        clear_screen()
                        at(f"Your choice for the x value: {first}")
                        at(f"Choose the y value of the graph: {', '.join(options)}. Enter 0 to exit. ")
                        second = input().lower()
                    if second == '0':
                        at("Exiting...")
                        pause(1)
                        clear_screen()
                        menu()
                        return
                    else:
                        qgraph()
                else:
                    qgraph()
            elif first == second:
                while first == second:
                    at("The two values can not be the same.")
                    pause(1)
                    clear_screen
                    at(f"Choose the y value of the graph: {', '.join(options)}. Enter 0 to exit. ")
                    second = input().lower()
                    if second == "0":
                        print("Exiting...")
                        menu()
                    else:
                        qgraph()
            else:
                qgraph()

    if choice == '1':
        at("Options:\n1. Bar Graphs\n2. Scatter Plot\n3. Exit\nChoose an option from 1-3: ")
        tp = input()
        while tp not in ["1", "2", "3"]:
            at("Invalid.")
            pause(1)
            clear_screen()
            at("Options:\n1. Bar Graphs\n2. Scatter Plot\n3. Exit\nChoose an option from 1-3: ")
            tp = input()
        if tp == "1":
            clear_screen()
            at("Options:\n1. Social media hours vs sleep hours\n2. Social media hours vs stress level\n3. Social media hours vs productivity score\nChoose an option from 1-3 or 0 to exit: ")
            graph_options = input()
            while graph_options not in ['1', '2', '3', '0']:
                at("Invalid.")
                pause(1)
                clear_screen()
                at("Options:\n1. Social media hours vs sleep hours\n2. Social media hours vs stress level\n3. Social media hours vs productivity score\nChoose an option from 1-3 or 0 to exit: ")
                graph_options = input()
            if graph_options == '1':
                clear_screen()
                at("Displaying graph... Close the popup to return to menu")
                average('social_media_hours', 'sleep_hours')
                graph3('social_media_hours', 'average', 'Social media effect on sleep')
            elif graph_options == '2':
                clear_screen()
                order1 = ["Low", "Medium", "High"]
                social_media['stress_level'] = pd.Categorical(
                social_media['stress_level'], categories=order1, ordered=True
                )
                at("Displaying graph... Close the popup to return to menu")
                average('stress_level', 'social_media_hours')
                graph4('stress_level', 'average', 'Social media effect on stress levels')
            elif graph_options == '3':
                clear_screen()
                at("Displaying graph... Close the popup to return to menu")
                average('social_media_hours', 'productivity_score')
                graph3('social_media_hours', 'average', 'Social media effect on productivity level out of 100')
            elif graph_options == '0':
                clear_screen()
                at('Exiting...')
                pause(1)
                clear_screen()
                view_visualisation()
        elif tp == "2":
            clear_screen()
            at("Options:\n1. Social media hours vs sleep hours\n2. Social media hours vs productivity score\nChoose an option from 1-2 or 0 to exit: ")
            graph_options = input()
            while graph_options not in ['1', '2', '0']:
                at('Invalid')
                pause(1)
                clear_screen()
                at("Options:\n1. Social media hours vs sleep hours\n2. Social media hours vs productivity score\nChoose an option from 1-2 or 0 to exit: ")
                graph_options = input()
            if graph_options == '1':
                clear_screen()
                at("Displaying graph... Close the popup to return to menu")
                graph5('social_media_hours', 'sleep_hours', 'Social media effect on sleep')
            elif graph_options == '2':
                clear_screen()
                at("Displaying graph... Close the popup to return to menu")
                graph5('social_media_hours', 'productivity_score', 'Social media effect on productivity')
            elif graph_options == '0':
                clear_screen()
                at('Exiting...')
                pause(1)
                clear_screen()
                view_visualisation()
        elif tp == "3":
            clear_screen()
            at('Exiting...')
            pause(1)
            clear_screen()
            view_visualisation()

    clear_screen()
    pause(1)
    menu()

def update_data():
    at("Choose a userid(row) to update. Enter a number from 0-11000 or e to exit: ")
    user = input()
    if user.lower() == 'e':
        at("Exiting...")
        pause(1)
        clear_screen()
        menu()
        return
    
    if user.isdigit():
        user = int(user)
    else:
        while user.isdigit() == False:
            at("Enter a number")
            pause(1)
            clear_screen()
            at("Choose a userid(row) to update. Enter a number from 0-11000 or e to exit: ")
            user = input()

    while user not in range(0, 11001):
        at('Invalid')
        pause(1)
        clear_screen()
        at("Choose a userid(row) to update. Enter a number from 0-11000 or e to exit: ")
        user = int(input())

    at("Choose a column to update: Age, Daily Screen Time Hours, Social Media Hours, Sleep Hours, Study Work Hours, Productivity Score, Stress Level, Platform, Or enter e to exit. ")
    user2 = input().strip().lower()
    while user2 not in options1 + ['e']:
        at("Not a column name.")
        at("Choose a column to update: Age, Daily Screen Time Hours, Social Media Hours, Sleep Hours, Study Work Hours, Productivity Score, Stress Level, Platform, Or enter 0 to exit. ")
        user2 = input().strip().lower()

    if user2 == 'e':
        at("Exiting...")
        pause(1)
        clear_screen()
        menu()
        return

    elif user2 not in ['productivtity score', 'stress level']: 
        at(f"Enter the new value you would like for the {user2} column: ")
        update = int(input())
        social_media.loc[social_media['user_id'] == user, user2] = update
        clear_screen()
        at("Updating...", 0.05)
        pause(1)
        at("Done!")
        pause(1)
        clear_screen()
        menu()
    else:
        at(f"Enter the new word you would like for the {user2} column: ")
        update = str(input())
        social_media.loc[social_media['user_id'] == user, user2] = update
        clear_screen()
        at("Updating...", 0.05)
        pause(1)
        at("Done!")
        pause(1)
        clear_screen()
        menu()

def save():
    social_media.to_csv('social_media_sleep_stress_productivity_11000.csv', index=False)
    at('All changes saved.')
    pause(1)
    clear_screen()
