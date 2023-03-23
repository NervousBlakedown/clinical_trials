# Identify potential participants for clinical trials using data mining techniques

# Imports
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier

# Load the patient data
patient_data = pd.read_csv("C:\\Users\\blake\\iCloudDrive\\github\\datasets\\medical\\sample_patient_data.csv")

# Append 'eligible_for_trial' column into dataframe
# patient_data['eligible_for_trial'] = pd.Series() # blank value

# Append 'eligible_for_trial' column into dataframe and fill it with random values
patient_data['eligible_for_trial'] = np.random.choice(['Yes', 'No'], size=len(patient_data))

# Convert both 'gender' columns to binary features to work properly
patient_data['is_male'] = (patient_data['gender'] == 'M').astype(int)
patient_data['is_female'] = (patient_data['gender'] == 'F').astype(int)

# Convert 'medical_history' column into binary features using one-hot encoding
medical_history = patient_data['medical_history'].str.get_dummies(',')
patient_data = pd.concat([patient_data, medical_history], axis=1)

# Define the target variable and features
target_variable = 'eligible_for_trial' # must be in dataframe

# use features (feature selection) for trial eligibility
# removed both original gender columns and replaced with binary value columns 
features = ['age', 'is_male', 'is_female'] + list(medical_history.columns) + ['genetic_information'] 
# features = ['age', 'is_male', 'is_female', 'medical_history', 'genetic_information'] 


# Split the data into training and testing sets
train_data = patient_data.sample(frac=0.8, random_state=1)
test_data = patient_data.drop(train_data.index)

# Train a decision tree classifier
classifier = DecisionTreeClassifier()
classifier.fit(train_data[features], train_data[target_variable])

# Use the classifier to predict eligibility for the test data
predictions = classifier.predict(test_data[features])
test_data['predictions'] = predictions

# Identify potential participants for the clinical trial
potential_participants = test_data[test_data['predictions'] == 1]
print(potential_participants)
