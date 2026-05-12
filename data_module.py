import matplotlib
import pandas as pd

def view_datset():
    social_media = pd.read_csv('social_media_sleep_stress_productivity_11000.csv',
                               header= None,
                               names=['user_id', 'age', 'daily_screen_time_hours', 'social_media_hours', 'sleep_hours', 'exercise_minutes', 'study_work_hours', 'productivity_score', 'stress_level', 'platform']
                               )

    print(social_media)

view_datset()