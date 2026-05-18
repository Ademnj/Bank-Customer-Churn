import pandas as pd
from forcln import db
import numpy

terkeden_mus = db["Exited"].sum()
toplam_mus = len(db)

terk_orani = (terkeden_mus / toplam_mus) * 100
print(f"Terk Eden Müşteri Sayısı : {terkeden_mus}. Terk Oranı : %{terk_orani:.2f}")

#yaş gruplarına göre terk oranı

yas_sinirlari = [0, 25, 35, 45, 55, 65, 100]
yas_etiketleri = ['0-18', '26-35', '36-45', '46-55', '56-65', '65+']
db["Yas_Grubu"] = pd.cut(db["Age"], bins=yas_sinirlari,labels=yas_etiketleri)

yas_analizi = db.groupby("Yas_Grubu")["Exited"].agg(toplam_mus="count",terkeden_mus="sum",terk_orani=lambda x: round(x.mean() * 100,2)).reset_index()

print(yas_analizi)

#ülkeye göre terk oran

# 1. Fransa için hesaplayalım
fransa_toplam = len(db[db['Geography'] == 'France'])
fransa_giden = db[db['Geography'] == 'France']['Exited'].sum()
fransa_oran = (fransa_giden / fransa_toplam) * 100

# 2. Almanya için hesaplayalım
almanya_toplam = len(db[db['Geography'] == 'Germany'])
almanya_giden = db[db['Geography'] == 'Germany']['Exited'].sum()
almanya_oran = (almanya_giden / almanya_toplam) * 100


# 3. İSPANYA için hesaplayalım
ispanya_toplam = len(db[db['Geography'] == 'Spain'])
ispanya_giden = db[db['Geography'] == 'Spain']['Exited'].sum()
ispanya_oran = (ispanya_giden / ispanya_toplam) * 100


# Sonuçları yazdır
print(f"Fransa Terk Oranı: %{fransa_oran:.2f}")
print(f"Almanya Terk Oranı: %{almanya_oran:.2f}")
print(f"İspanya Terk Oranı: %{ispanya_oran:.2f}")


kalanlar = db[db['Exited'] == 0]
gidenler = db[db['Exited'] == 1]

kalan_ortskr = kalanlar["CreditScore"].mean()
giden_ortkskr = gidenler["CreditScore"].mean()
print(f"Bankada Kalan Müşterilerin Kredi Skoru Ortalaması: {kalan_ortskr:.2f}")
print(f"Bankayı Terk Eden Müşterilerin Kredi Skoru Ortalaması: {giden_ortkskr:.2f}")

#AKTİF ÜYE OLMAYANLARIN TERK ORANI

aktif_olmayan = db[db["IsActiveMember"] == 0]
aktif_dgl = len(aktif_olmayan)
print(f"Toplam Aktif Olmayan Üye Sayısı: {aktif_dgl}")
aktif_olmayan_terk_eden = aktif_olmayan["Exited"].sum()
aktif_olmayan_terk_orani = (aktif_olmayan_terk_eden / aktif_dgl) * 100
print(f"Aktif Olmayanların Terk Eden Sayısı: {aktif_olmayan_terk_eden}")
print(f"Aktif Olmayanların Terk Oranı: %{aktif_olmayan_terk_orani:.2f}")