import pandas as pd

db = pd.read_csv("data/Customer-Churn-Records.csv")

print(db.shape)
print(db.isnull().sum())
print(db.dtypes)
print(db.head())


"""EXCEL VERİLERİ ÇOK TEMİZ HATTA HİÇ HATA YOK O YÜZDEN BİR DÜZENLEME YAPILMAMIŞTIR."""