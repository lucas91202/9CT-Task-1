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

## Researching and Planning

### Research Your Chosen Issue
- [Sleep and Social Media](https://www.sleepfoundation.org/how-sleep-works/sleep-and-social-media)
- [Impact of Social Media on Work Efficiency](https://pmc.ncbi.nlm.nih.gov/articles/PMC8355543/)
- [Social Media and Mental Health](https://www.helpguide.org/mental-health/wellbeing/social-media-and-mental-health)

### Discuss Your Findings
Social media can provide both positive and negative impacts on health. Social media positively benefits us as it allows us to interact with friends, family and work colleagues. However, excessive social media can result with, lack of sleep, depression, high stress and isolation. An example of a positive feature of social media includes the usage of WeChat in China, as it is widely used by Chinese companies, highly benefiting the efficiency of work. A negative example however, is FOMO or fear of missing out. This is relevant to social media as for example, sites like Facebook or Instagram create feelings that other people are living life better than you are. This triggers anxiety and could impact self-esteem. Social media can be both good and bad for health, however, it should be used in moderation, to avoid effects like fear of missing out.

### Acquire Your Data
[Dataset from Kaggle](https://www.kaggle.com/datasets/jayjoshi37/social-media-usage-vs-sleep-stress-and-productivity/data)

### Data Dictionary
|Field|Datatype|Formart for Display|Description|Example|Validation|
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| age | int64 | N | The serveyed user's age | 23 | Must not contain letters |
| daily_screen_time | float64 | N.NN | The daily screen time of the user in hours | 2.39 | Must contain only numbers and be 2 decimal places |
| social_media_hours | float64 | N.NN | The amount of screen time on social media apps in hours | 1.39 | Must be only numbers and be 2 decimal places |
| sleep_hours | float64 | N.NN | The amount of sleep the user got in hours | 8.46 | Only a number with 2 decimal places |
| study_work_hours | float64 | N.NN | The amount of time the user spent studying or working in hours | 3.73 | Only numbers, to two decimal places |
| productivity_score | float64 | N.NN | A score out of 100 of the user's productivity | 33.86 | Must be 100 or lower and have 2 decimal places |
| stress_level | string | XX...XX | How stressed the user is from low, medium and high | Low | Must not contain numbers, can only be low, medium and high |
| platform | string | XX...XX | The social media platform that the user used the most | Youtube | Must contain only letters and should be a social media platform name |

## Testing and Evaluating
### Test Your Analysis
I have checked through my program and confirmed that it gives correct results based off of the dataset.

### Analyse and Conclude
Social media has an effect on both sleep and productivity, however, it does not effect stress levels. Using my analysis, I found that only sleep and productivity were effected by higher social media hour usage, whereas stress levels had varying results. For example, users who had 0-3 social media hours on average had a productivity score slightly above those who had 6-9 hours, and those who had lower social media hours also had more sleep hours. This would allow you to assume that social media does have an effect on both sleep and productivity, but not stress level. However, these differences were very small as the dataset, consisting of 11000 entries, brang the gaps closer. Social media has an effect on both sleep and productivty, however, it does not effect stress likely because of external factors that were not considered.

### Peer Verification ()

### Version Control
#### Commits on May 20, 2026
- worked on step 4 and fixed a typo in the menu function
- Update data_module.cpython-314.pyc

#### Commits on May 19, 2026
- worked on step 4
- small changes
- final changes potentially
- worked on issues to have the code work on all devices
- Create data_module.cpython-314.pyc

#### Commits on May 18, 2026
- FINISHED

#### Commits on May 17, 2026
- small adjustments
- finished visualisations
- worked on data visulisation

#### Commits on May 16, 2026
- worked on data visualisations, close to finishing

#### Commits on May 15, 2026
- finished filtering, working on categories for graphs
- worked on filtersearch function
- Merge branch 'main' of https://github.com//9CT-Task-1
- working on searching and filtering data

#### Commits on May 14, 2026
- worked on visualisation function
- Worked on visualisations

#### Commits on May 12, 2026
- Update data_module.py
- finished ui, starting work on functions

#### Commits on May 8, 2026
- started main.py
- Update main.py

#### Commits on May 7, 2026
- Removed unnecessary columns

#### Commits on May 3, 2026
- Finished Identifying and Defining as well as Researching and Planning

#### Commits on May 1, 2026
- Added to my project documentation
- Update PROJECT_DOCUMENTATION.md
- Update PROJECT_DOCUMENTATION.md
- Create Untitled-2026-04-24-1440.png

#### Commits on Apr 30, 2026
- Add files via upload

#### Commits on Apr 24, 2026
- Created files for task, moving on to mind map
- Initial commit

### Evaluate Your Project

#### Requirements Outline
I believe that my project does mostly fit the functional requirements I set in the requirements outline. However, my project misses a few points mentioned. The project is only able to load one csv file, which is the dataset I used to create my project around. The program can sort and group data as a part of the search function. Statistical features the program can do only includes mean. Mode is not included however, the program can search for occurences of a specific number of the user's choice. The program succesfully outputs graphs and the final dataset is stored in a .csv file. The README and the user interface are both made well, allowing users to navigate and use the program. The system has been tested and has no errors. The program successfully fits the use-case, following each part of it correctly.

#### Peer Feedback

#### Project Management
The creation of the project was very well organised and began with the early stages and brainstorming. Once an idea had been found, a purpose and dataset were also found. After researching and planning how the project would work, coding begun. Version control above demonstrates the progress on the project, starting on the main file, before working through the visualisations and searching feature. Once both were finished, the rest of the features were also finished. Once all features were finished, the entire project was put together and I began bug testing. Overall, the steps taken were very well organised and the project management was well done.

#### Data and Security
The data is timely as it is very recent, however, it is synthetic and not usable in real world scenarios. The data is therefore inaccurate and invalid, as the dataset is only meant for educational, analytical and machine learning purposes; it is used to simulate realistic user behaviour but it does not represent real people. The data is potentially biased as the creator created the data to simulate realistic behaviours, meaning the creator may have a biased view of how people behave. The project should have no issues concerning security. The user experience of the program could be improved upon to be made more accessible for users. This could be done by reducing the reading required, this would mean creating more menus, similar to how the program opens. The user experience could also be made more accessible for those who could have difficulty understanding what certain parts of the program mean, as some parts require reading to understand what to input.