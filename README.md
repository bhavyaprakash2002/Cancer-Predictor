# Cancer-Predictor
This repo aims at predicting cancer of human beings.
The dataaset was taken from kaggle (https://www.kaggle.com/datasets/rishidamarla/cancer-patients-data?rvi=1)
The dataset contains 25 columns out of which the first 24 are recognised as features and the column 'Level' is recognised as the required target.
Features such as 'Age', 'Sex', 'Alcohol use', 'Dust Allergy', etc. are taken as input and 'Level' is predicted.

The unnecessary columns from the dataset were removed to make it more efficient. 
Data was checked for null values (if any).
LabelEncoder was used for classifying 'Level' hence assuming :
0 to be low
1 to be medium
2 to be high

Classification was done by the help of LogisticRegression and it resulted in precision and recall score of 99%.
