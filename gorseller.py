import matplotlib.pyplot as plt
from forcln import db
from analiz import gidenler,terk_orani,fransa_giden,almanya_giden,ispanya_giden

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
ulkeler = ["Almanya","İspanya","Fransa"]
oranlar = [32.4, 16.1, 16.6] 
axes[0, 0].bar(ulkeler, oranlar, color=['red', 'blue', 'orange'])
axes[0, 0].set_title('Ülkelere Göre Terk Oranları (%)')
axes[0, 0].set_ylabel('Oran')

yas_gruplari = ['0-25', '26-35', '36-45', '46-55', '56-65', '65+']
yas_oranlari = [7.5, 12.0, 22.0, 48.0, 48.0, 15.0]
axes[0, 1].plot(yas_gruplari, yas_oranlari, marker='o', color='purple', linewidth=2)
axes[0, 1].set_title('Yaş Gruplarına Göre Terk Trendi (%)')
axes[0, 1].grid(True, linestyle='--')

durumlar = ['Kalanlar', 'Terk Edenler']
sayilar = [7963, 2037] 
axes[1, 0].pie(sayilar, labels=durumlar, autopct='%1.1f%%', colors=['green', 'darkred'], startangle=90)
axes[1, 0].set_title('Genel Müşteri Dağılımı')

# 4. GRAFİK (Sağ Alt): Ürün Sayısına Göre Terk Durumu
urun_sayisi = ['1 Ürün', '2 Ürün', '3 Ürün', '4 Ürün']
urun_oranlari = [27.7, 7.5, 82.7, 100.0] 
axes[1, 1].barh(urun_sayisi, urun_oranlari, color='teal')
axes[1, 1].set_title('Ürün Sayısına Göre Terk Oranları (%)')
axes[1, 1].set_xlabel('Oran')

plt.tight_layout()
plt.savefig('gorseller/Genel.png', dpi=150)
plt.show()