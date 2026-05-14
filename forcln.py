import pandas as pd

db = pd.read_csv("data/Customer-Churn-Records.csv")

print(db.shape)
print(db.head())