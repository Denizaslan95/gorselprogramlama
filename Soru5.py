a = "send-150-3-2-1\nreceive-250-3-0\n"
k = a.split("\n")
b = 0
def n(c , f):
   if ((int(f[0]) >= 0 and int(f[0]) <= 255) and (int(f[1]) >= 1 and int(f[1]) <= 4) and (int(f[2]) >= 0 and int(f[2]) <= 1) and ((len(f) == 4 and int(f[3]) >= 0 and int(f[3]) <= 1) or len(f) == 3)):
      print("Kod Tipi: " + c)
      if (int(f[0]) >= 0 and int(f[0]) <= 50):
         print("Sinyal Gucu: " + f[0] + " - Cok Zayif")
      elif (int(f[0]) >= 51 and int(f[0]) <= 100):
         print("Sinyal Gucu: " + f[0] + " - Zayif")
      elif (int(f[0]) >= 101 and int(f[0]) <= 150):
         print("Sinyal Gucu: " + f[0] + " - Orta")
      elif (int(f[0]) >= 151 and int(f[0]) <= 200):
         print("Sinyal Gucu: " + (f[0]) + " - Guclu")
      elif (int(f[0]) >= 201 and int(f[0]) <= 255):
         print("Sinyal Gucu: " + f[0] + " - Cok Guclu")
      else:
         print("Sinyal Gucu: Gecersiz")
      if (int(f[1]) == 1):
         print("Cihaz: " + f[1] + " - Televizyon")
      elif (int(f[1]) == 2):
         print("Cihaz: " + f[1] + " - Camasir Makinesi")
      elif (int(f[1]) == 3):
         print("Cihaz: " + f[1] + " - Buzdolabi")
      elif (int(f[1]) == 4):
         print("Cihaz: " + f[1] + " - Firin")
      else:
         print("Cihaz: Gecersiz")
      if (int(f[2]) == 0):
         print("Durumu: " + f[2] + " - Off")
      elif (int(f[2]) == 1):
         print("Durumu: " + f[2] + " - On")
      else:
         print("Durumu: Gecersiz")
      if (len(f) == 4):
         if (int(f[3]) == 0):
            print("Cevap: " + f[3] + " - Istenmiyor")
         elif (int(f[3]) == 1):
            print("Cevap: " + f[3] + " - Isteniyor")
         else:
            print("Cevap: Gecersiz")
   else:
      print("Error: ikinci bolum hatali")
for i in k:
   if (len(i) > 0):
      f = i.split("-")
      c = f.pop(0)
      b += 1
      if (b > 1):
         print("------")
      if (c == "send"):
         if (len(f) != 4):

            print("Error: ikinci bolum hatali")
         else:
            n(c + " - Giden", f)
      elif (c == "receive"):
         if (len(f) != 3):
            print("Error: ikinci bolum hatali")
         else:
            n(c + " - Gelen", f)
      else:
       print("Error: send ya da receive icermiyor")
