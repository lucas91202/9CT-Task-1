# 9CT-Task-1
## Overview
The program allows users to filter through data from a dataset on social media, sleep, stress and more. The program allows the user to make changes to the dataset, save the changes, view the dataset, search for values and create graphs using the columns of the datset.

## Usage Instructions
### Starting Notes
If running the program does not work, open the terminal and run `pip install pandas` and `pip install matplotlib`. Verify this works by checking if `data_module.py` has no errors or issues.

### Running the Program
Once you run the program, you should be presented with a menu, presenting options 1-6. From here, you may choose any option to continue.

### View Dataset
This will present the dataset used, it is shortened to avoid presenting all 11000 lines of the data.

### Search Data
This presents the user with column names to retrieve data from. Once a column is chosen, the user is presented with a selection of choices for the user to pick from.

### View Visualisation
This presents the user with two options:
- View prechosen graphs that determine the effects of social media on stress, productivity and sleep
- Allows the user to choose their own variables and create a graph accordingly. Certain limitations appear when using the data with worded values. Examples include stress levels or productivity.

### Update a Data Entry
Choosing this option allows the user to choose a user id or row to edit. Once choosing the row, they are then prompted to choose a column. A value is then chosen for the selected location.

### Save Changes
Allows the user to save any changes they made with the original dataset.

### Exit
Self-explanatory; shuts the program down.