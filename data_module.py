import matplotlib.pyplot as plt
import pandas as pd
options = ['Age', 'Daily Screen Time', 'Social Media Hours', 'Sleep Hours', 'Study Work Hours', 'Productivity Score', 'Stress Level', 'Platform']

xval = {
    "age" : ['0-18', '19-25', '26-35', '36-45', '46-55'],
    "daily_screen_time" : ['0-3', '3-6', '6-9', '9-12', ''],
    "social_media_hours" : ['0-3', '3-6', '6-9', '', ''],
    "sleep_hours" : ['0-3', '3-6', '6-9', '', ''],
    "study_work_hours" : ['0-3', '3-6', '6-9', '9-12', ''],
    "productivity_score" : ['0-25', '25-50', '50-75', '75-100', ''],
    "average_age" : ['', '', '', '', ''],
    "average_daily_screen_time" : ['', '', '', '', ''],
    "average_social_media_hours" : ['', '', '', '', ''],
    "average_sleep_hours" : ['', '', '', '', ''],
    "average_study_work_hours" : ['', '', '', '', ''],
    "average_productivity_score" : ['', '', '', '', ''],
}

df = pd.DataFrame(xval)

social_media = pd.read_csv('social_media_sleep_stress_productivity_11000.csv',
                            index_col=False,
                            header= None,
                            names=['user_id', 'age', 'daily_screen_time_hours', 'social_media_hours', 'sleep_hours', 'exercise_minutes', 'study_work_hours', 'productivity_score', 'stress_level', 'platform'],
                            )
random_social_media = social_media.sample(n=300)

test = []

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
    num = len(social_media.columns)
    if num == 10:
        social_media.drop(columns=['user_id', 'exercise_minutes'], inplace=True)
        print(social_media)
    else:
        print(social_media)

def filtersearch():
    if filter not in ["stress_level", "platform"]:
        filter2 = int(input("1. Find the average\n2. Search all entries for a number\n3. Sort frequency by ascending or descending\n4. Find values between two ranges\n5. Exit\nChoose an option from 1-5: "))
        while filter2 not in [1, 2, 3, 4, 5]:
            filter2 = int(input("1. Find the average\n2. Search all entries for a number\n3. Sort frequency by ascending or descending\n4. Find values between two ranges\n5. Exit\nChoose an option from 1-5: "))
        if filter2 == 1:
            average = social_media.loc[:, [f'{filter}']].mean()
            print(average.to_string())
        elif filter2 == 2:
            userentry = float(input("Enter the number or decimal you would like to search for: "))
            valuecount = social_media[filter].value_counts().get(userentry, 0)
            print(f"Occurences of {userentry}: {valuecount}") #show the rows with the number?
        elif filter2 == 3:
            ascdsc = input("Enter how you would like to sort the data(ascending/descending): ").strip().lower()
            while ascdsc not in ['ascending', 'descending']:
                ascdsc = input("Enter how you would like to sort the data(ascending/descending): ").strip().lower()
            if ascdsc == "ascending":
                asc = social_media[filter].value_counts(ascending=True)
                print(asc.to_string())
            else:
                dsc = social_media[filter].value_counts(ascending=False)
                print(dsc.to_string())
        elif filter2 == 4:
            val1 = float(input("Enter the lower number of the range: "))
            val2 = float(input("Enter the higher number of the range: "))
            valu = social_media[filter].value_counts().sort_index()
            value = valu.loc[val1:val2]
            print(value.to_string())
        elif filter2 == 5:
            search_data()
    else:
        filter3 = int(input("1. Search for amounts of each word\n2. Exit\nChoose an option from 1-2: "))
        while filter3 not in [1, 2]:
                    filter3 = int(input("1. Search for amounts of each word\n2. Exit\nChoose an option from 1-2: "))
        if filter3 == 1:
            if filter == "stress_level":
                userentry1 = input("Options: Low, Medium, High\nEnter the corresponding stress level: ").capitalize()
                while userentry1 not in ['Low', 'Medium', 'High']:
                    print("Invalid")
                    userentry1 = input("Options: Low, Medium, High\nEnter the corresponding stress level: ").capitalize()
                valuecount = social_media[filter].value_counts().get(userentry1, 0)
                print(f"Occurences of {userentry1}: {valuecount}")
            elif filter == "platform":
                userentry2 = input("Options: Twitter, Youtube, Snapchat, LinkedIn, Instagram\nEnter the corresponding platform: ").capitalize()
                while userentry2 not in ['Twitter', 'Youtube', 'Snapchat', 'Linkedin', 'Instagram']:
                    print("Invalid")
                    userentry2 = input("Options: Twitter, Youtube, Snapchat, LinkedIn, Instagram\nEnter the corresponding platform: ").capitalize()
                if userentry2 == "Linkedin":
                    userentry2 = userentry2[:6]+"I"+userentry2[7:]
                    valuecount = social_media[filter].value_counts().get(userentry2, 0)
                    print(f"Occurences of {userentry2}: {valuecount}")
                elif userentry2 == "Youtube":
                    userentry2 = userentry2[:3]+"T"+userentry2[4:]
                    valuecount = social_media[filter].value_counts().get(userentry2, 0)
                    print(f"Occurences of {userentry2}: {valuecount}") 
                else:
                    valuecount = social_media[filter].value_counts().get(userentry2, 0)
                    print(f"Occurences of {userentry2}: {valuecount}")

        elif filter3 == 2:
            search_data()
            

def search_data():
    global filter
    fil = input("Choose a topic to sort:\nAge, Daily Screen Time Hours, Social Media Hours, Sleep Hours, Study Work Hours, Productivity Score, Stress Level, Platform: ").lower()
    filter = fil.replace(" ", "_")
    filtersearch()


def graph(x, y, z):
    if x not in ['stress_level', 'platform']:
        df.plot(
                kind= z,
                x= x,
                y= y,
                color='blue',
                alpha=0.3,
                title=f'{x} vs {y}'
                )
        plt.show()
    else:
        word = social_media.groupby(x)[y].sum().sort_values(ascending=False) #find averages of y value and use groups of x
        word.plot(
                kind= z,
                x= x,
                y= y,
                color='blue',
                alpha=0.3,
                title=f'{x} vs {y}'
                )
        plt.show()

second_value = "age"

def average(x): # Finish making sure that the average function adds the values to the correct respective '' in the xval dataframe
    l = 0
    for z in df[x]:
        split = df[x].str.split("-", expand=True).astype(int)
        split.columns = ['a', 'b']
        nums = int(split['a'].iloc[l])
        nums2 = int(split['b'].iloc[l])
        aver = social_media.loc[social_media[x].between(nums, nums2), x].mean()
        test.append(aver)
        l += 1

average(second_value)

print(test)
def view_visualisation(): #Work on fully implementing the average function
    global first
    global second_value
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
            average(second_value)
            add = "average_"
            second_val = add + second_value
            graph(first_value, second_val, graph_type)
    if choice == '1':
        graph_options = int(input("Options:\n1. Social media hours vs sleep hours\n2. Social media hours vs stress level\n3. Social media hours vs productivity score\nChoose an option from 1-3 or 0 to exit: "))
        if graph_options == 1:
            graph('social_media_hours', 'sleep_hours', 'scatter')
        if graph_options == 2:
            graph('stress_level', 'social_media_hours', 'bar')

