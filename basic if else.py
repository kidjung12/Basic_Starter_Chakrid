x = int(input("ค่า x"))
z = "idk"
a = 10
b = 15
c = 25
d = 35
e = 45
f = a*0.07
g = b*0.07
h = c*0.07
i = d*0.07
j = e*0.07
name = "chakrid"
uid =  "681305000134"
if x < 5 :
   print ("free")
elif x >= 5 and x <= 50 :
   print (a)
   print (f)
   print (a+f)
elif x >= 51 and x <= 100 :
   print (b)
   print (g)
   print (b+g)
elif x >= 101 and x <= 300 :
   print (c)
   print (h)
   print (c+h)
elif x >= 301 and x <= 500 :
   print (d)
   print (i)
   print (d+i)
elif x > 500 :
   print (e)
   print (j)
   print (e+j)
else:
   print ("free")