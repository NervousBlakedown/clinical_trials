"""Create random patient data.
Can be used for clinical trials, etc."""

# Imports
import pandas as pd
import numpy as np
from faker import Faker

# Define the number of patients to generate
num_patients = 100000 # as many rows as you need, baby

# Generate random patient demographics
genders = ['M', 'F']
ages = np.random.normal(loc=50, scale=20, size=num_patients).astype(int)
genders = np.random.choice(genders, size=num_patients)
zip_codes = np.random.randint(low=10000, high=99999, size=num_patients)

# Generate random medical history data
# Number of elements in this list must match number of elements in prob. distribution variable below
medical_history = ['Diabetes', 'Hypertension', 'Cancer', 'Asthma', 'Heart disease', 'Stroke']

# Probability Distribution on line below must add up to 1
medical_history_prob = [0.15, 0.20, 0.1, 0.2, 0.3, .05]

# check if the probabilities sum to 1
if np.sum(medical_history_prob) == 1.0:
    print("The probabilities sum to 1.")
else:
    print("The probabilities do not sum to 1.")

medical_history_data = []
for i in range(num_patients):
    mh = np.random.choice(medical_history, p=medical_history_prob)
    medical_history_data.append(mh)

# Generate random genetic information
genetic_data = np.random.normal(loc=0, scale=1, size=num_patients)

# Combine the data into a Pandas DataFrame
patient_data = pd.DataFrame({
    'age': ages,
    'gender': genders,
    'zip_code': zip_codes,
    'medical_history': medical_history_data,
    'genetic_information': genetic_data
})

# begin faker instance
faker = Faker()

# append a new column with full names using faker
patient_data['full_name'] = patient_data.apply(lambda x: faker.name(), axis=1)

# append a patient ID column in existing dataframe
# generate a random ID for each row
patient_data['patient_id'] = np.random.randint(10000, 10000000, size=len(patient_data))

# Get column names in dataframe
patient_data.columns

# get the column names and save them as a list variable
cols = patient_data.columns.tolist()

# optional: move the last column to the first position
cols = cols[-1:] + cols[:-1]

# optional: move the second-to-last column to the second position
cols = [cols[0]] + [cols[-2]] + cols[1:-2] + [cols[-1]]

# optional: move last column to second-from-left position
cols = cols[:-2] + [cols[-1]] + [cols[-2]]

# not optional: after rearranging columns, reindex the dataframe with the updated column order
patient_data = patient_data[cols]

# Save the data to a CSV file (default path is working directory)
patient_data.to_csv("C:\\Users\\blake\\iCloudDrive\\github\\datasets\\medical\\sample_patient_data.csv", index=False)