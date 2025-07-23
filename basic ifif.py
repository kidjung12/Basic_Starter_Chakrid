Y = (input("ประเภทสมาชิก"))
Z = int(input("จำนวนเงิน"))
if Y == "Gold" :
   if Z >= 1000:
      print ("ได้รับส่วนลด 15%")
      result = Z-(Z*0.15)
      print(result)
   else :
      print ("ได้รับส่วนลด 10%")
      result = Z-(Z*0.10)
      print(result)
elif Y == "Sliver" :
   if Z >= 1000:
      print ("ได้รับส่วนลด 10%")
      result = Z-(Z*0.10)
      print(result)
   else :
      print ("ได้รับส่วนลด 5%")
      result = Z-(Z*0.05)
      print(result)
else :
   print("ไม่มีส่วนลด")
   print(Z)