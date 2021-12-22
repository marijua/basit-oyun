karakter_1 = {"adi":"ender",
              "gücü":100,
               "silahi":"tabanca",
               "cani":100}


karakter1 = input("Karakter 1in Bilgilerini Görmek İçin Evet Diyiniz : ")


if karakter1 == "Evet" or "evet":
	print()
	print("Karakter 1in Adı : {}".format(karakter_1["adi"]))
	print("Karakter 1in Gücü : {}".format(karakter_1["gücü"]))
	print("Karakter 1in Silahı : {}".format(karakter_1["silahi"]))
	print("Karakter 1in Canı : {}".format(karakter_1["cani"]))
	print()
elif karakter1 == "Hayır" or "hayır":
	print("Çıkış Yapılıyor...")
else:
	print("Hatalı Komut Girdiniz!")

karakter_2 = {"adi":"mehmet",
              "gücü":50,
               "silahi":"kılıç",
               "cani":100}

karakter2 = input("Karakter 2nin Bilgilerini Görmek için Evet Diyiniz : ")

if karakter2 == "Evet" or "evet":
	print()
	print("Karakter 2nin Adı : {}".format(karakter_2["adi"]))
	print("Karakter 2nin Gücü : {}".format(karakter_2["gücü"]))
	print("Karakter 2nin Silahı : {}".format(karakter_2["silahi"]))
	print("Karakter 2nin Canı : {}".format(karakter_2["cani"]))
	print()
elif karakter2 == "Hayır" or "hayır":
	print("Çıkış Yapılıyor...")
else:
	print("Hatalı Komut Girdiniz!")

def vur(vuran:dict,vurulan:dict):
	eksilen = vuran["gücü"]
	vurulan["cani"] = vurulan["cani"] - eksilen

doven = input("Vuranı Belirle : ")
dovulen = input("Vurulanı Belirle : ")

if doven == "karakter_1" and dovulen == "karakter_2":
  vur(karakter_1,karakter_2)
elif doven == "karakter_2" and dovulen == "karakter_1":
  vur(karakter_2,karakter_1)
else:
  print("Hatalı Komut!")

guncel = input("Savaştan Sonra Güncel Canları Görmek İçin Evet Diyiniz  : ")

if guncel == "Evet" or "evet":
  print("Karakter 1in Yeni Canı : {}".format(karakter_1["cani"]))
  print("Karakter 2nin Yeni Canı : {}".format(karakter_2["cani"]))
else:
  print("Hatalı Komut!")