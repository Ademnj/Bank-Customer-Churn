import sqlite3
import pandas as pd
from forcln import db
from analiz import toplam_mus,terk_orani,terkeden_mus

conn = sqlite3.connect("bankdata.db")
db.to_sql("bankdata", conn, if_exists="replace", index=False)

# 1. En Çok Müşteri Kaybeden Ülke Hangisi?
sorgu1 = """
SELECT Geography, SUM(Exited) 
FROM bankdata 
GROUP BY Geography
"""
sonuc1 = pd.read_sql(sorgu1, conn)

print(sonuc1)


#Şikayet edenlerin ne kadarı terk etti?
sorug2 = """SELECT Complain, COUNT(*) AS toplam_mus,SUM(Exited) AS terkeden_mus,(SUM(Exited) * 100.0 / COUNT (*)) AS terk_orani FROM bankdata GROUP BY Complain""" 

sorug2 = pd.read_sql(sorug2, conn)
print(sorug2)

#Kredi Kartı Sahibi Olmak Terki Engelliyor mu?
sorgu3 = """SELECT HasCrCard, COUNT(*) AS toplam_mus,SUM(Exited) AS terkeden_mus,(SUM(Exited) * 100.0 / COUNT(*)) AS terk_orani FROM bankdata GROUP BY HasCrCard"""
sorgu3 = pd.read_sql(sorgu3, conn)
print(sorgu3)
#Müşterilerin Bankada Kalma Süresi (Tenure) Terki Nasıl Etkiliyor?
sorgu4 = """SELECT Tenure, COUNT(*) AS toplam_mus, SUM(Exited) AS terkeden_mus,(SUM(Exited) * 100.0 / COUNT(*)) AS terk_orani FROM bankdata GROUP BY Tenure ORDER BY Tenure ASC"""
sorgu4 = pd.read_sql(sorgu4, conn)
print(sorgu4)
sorgu5 = """SELECT NumOfProducts, COUNT(*) AS toplam_mus,SUM(Exited) AS terkeden_mus,(SUM(Exited) * 100.0 / COUNT(*)) AS terk_orani FROM bankdata GROUP BY NumOfProducts ORDER BY NumOfProducts ASC"""
sorgu5 = pd.read_sql(sorgu5,conn)
print(sorgu5)

conn.close()