import pandas as pd
import csv

df = pd.read_csv('noduplicates.csv')

df = df.drop_duplicates()

df.to_csv('noduplicates.csv', index=False)

