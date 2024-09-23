import requests

depremler = requests.get("https://deprem.afad.gov.tr/last-earthquakes.html")
print(depremler)
# <Response [200]> okuma başarılı demektir
# 4xx bir hata oluştuğunu söyler
print(depremler.text)  # request karşıdan bilgi çeker

doviz_data = requests.get('https://www.tcmb.gov.tr/kurlar/today.xml')
print(doviz_data.text)
# metin string gelir json dictionary olarak gelir
