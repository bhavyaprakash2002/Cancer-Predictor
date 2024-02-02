import pandas as pd
import numpy as np
import pickle

data = pd.read_excel(r"C:\Users\Bhavya Prakash\Downloads\archive (5)\cancer patient data sets.xlsx")
data.drop('Patient Id', axis=1, inplace = True)

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
encoded_level = le.fit_transform(data['Level'])
encoded_level_df = pd.DataFrame(encoded_level)

data = data.drop('Level',axis = 1)
data = pd.concat([data,encoded_level_df],axis = 1)

data.columns = [                     'Age',                   'Gender',
                  'Air Pollution',              'Alcohol use',
                   'Dust Allergy',     'OccuPational Hazards',
                   'Genetic Risk',     'chronic Lung Disease',
                  'Balanced Diet',                  'Obesity',
                        'Smoking',           'Passive Smoker',
                     'Chest Pain',        'Coughing of Blood',
                        'Fatigue',              'Weight Loss',
            'Shortness of Breath',                 'Wheezing',
          'Swallowing Difficulty', 'Clubbing of Finger Nails',
                  'Frequent Cold',                'Dry Cough',
                        'Snoring',                          'Level']

x = data.iloc[:,:22]
y = data['Level']

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y, random_state = 42)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression(max_iter=100000)
model.fit(x_train,y_train)

print(model.score(x_train,y_train))
pickle.dump(model, open("model.pkl", "wb"))


