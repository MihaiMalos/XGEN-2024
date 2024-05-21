import pandas as pd

fake_dataset = pd.read_csv('Fake.csv')
fake_dataset['Label'] = '0'

true_dataset = pd.read_csv('True.csv')
true_dataset['Label'] = '1'

# Merge the two CSV files
full_dataset = pd.concat([fake_dataset, true_dataset], ignore_index=True)

# Save the merged CSV to a new file
full_dataset.to_csv('FakeReal.csv', index=False)