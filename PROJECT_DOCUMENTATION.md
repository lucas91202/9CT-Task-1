# CT1A - Task 1

## Identifying and Defining
### Mind Map
![](Untitled-2026-04-24-1440.png)

### Define Your Purpose
Social media affects people's sleep, stress and productivity.

### Functional Requirements
The program will be able to load csv files, it will be unable to load incorrect file types however. 
The program will need to sort and group data, and work with missing values.
Statistical analysis that the program will need to do includes, mean, median, mode and range. This will allow the user to compare with the different statistics.
The data will need to be visualised using Matplotlib line graphs. (Social media hours vs productivity, stress, etc.)
The system should output graphs and tables. The final dataset should be stored in a .csv file.

### Non-Functional Requirements
The user interface should be easy to navigate and understand, allowing users to understand what they are looking for. The README document should describe how the program is to be used. The system will be tested to ensure that the system will not have errors.

### Use-Case
Actor: User

Goal: To be able to access and interact with data using the program's user interface

Preconditions:
- The dataset is already loaded by the administrator
- The user is able to see and interact with the interface

Main Flow:
1. The user is greeted with the UI
2. The user then selects one of the given options:

    - Sort data and find averages
    - View graphs of certain aspects of the user's choice
    - Change certain values
    - Exit to the first menu
3. The system performs the actions requested by the user

Postconditions:
- User has interacted with the data
- Updates are saved
- Data remains available for future use