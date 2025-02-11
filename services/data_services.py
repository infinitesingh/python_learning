import pandas as pd
from config import logging

def city_sal_mapping(data):
    df = pd.read_csv('data/city_age_salary.csv')
    #print(df)

    logging.info('Satrteed filteration for: city: {0} and age: {1}'.format( data.get('City'),data.get('Age Bracket')))
    try:
        filterd_df = df[
            (df['City'] == data.get('City')) & (df['Age Bracket'] == data.get('Age Bracket'))
        ]
        print(filterd_df)
    except Exception as e:
        return 'Error in filteration as: {0}'.format(e)

    return int(filterd_df['Salary'])
