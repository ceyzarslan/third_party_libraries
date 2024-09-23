import os

print("Bulunduğumuz konum :", os.getcwd())  # projenin dosya konumunu verir
path = os.getcwd()
print(dir(os))  # içinde geçen fonksiyonların tüm listesini verir

print("System: ", os.listdir(os.getcwd()))  # OS MODÜLÜ BANA NERDE NASIL ÇALIŞMAM GEREKTİĞİNİ SÖYLÜYOR

os.environ["HOME"] = "Ceyda Özarslan!"
print(os.getenv('HOME'))

print(os.name)  # microsoft, nt
print(os.sep)  # microsoft , \

os.system('notepad.exe') #notepad çalıştırır
