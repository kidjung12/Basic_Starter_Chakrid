kayaba = 100
kirito = 100
first = 10
second = 15
third = 20
z = kayaba-first
k = 0 
number = int(input("สู้กด 1 หนีกด 2 "))
while k < 1 :
    k = k+1
    if number == 2 :
        print ("gameover")
    elif number == 1 :
        weapon = (input("เลือกอาวุธ มี 1 2 3 "))
        if weapon == "1" :
            hit = int(input("ตีกี่ครั้ง "))
            for i in range (hit) : 
                kayaba -= first
                print(kayaba)
            if kayaba > 0 :
                hit = int(input("ตีกี่ครั้ง "))
                for i in range (hit) :
                    kayaba -= first
                    print(kayaba) 
                if kayaba > 0 :
                    hit = int(input("ตีกี่ครั้ง "))
                    for i in range (hit) :
                        kayaba -= first
                        print(kayaba) 
            if kayaba <= 0 :
                print ("You won")
            else :
                print ("You Lose")
        elif weapon == "2" :
            hit = int(input("ตีกี่ครั้ง "))
            for i in range (hit) :
                kayaba -= second
                print(kayaba)
            if kayaba > 0 :
                hit = int(input("ตีกี่ครั้ง "))
                for i in range (hit) :
                    kayaba -= second
                    print(kayaba) 
                if kayaba > 0 :
                    hit = int(input("ตีกี่ครั้ง "))
                    for i in range (hit) :
                        kayaba -= second
                        print(kayaba) 
            if kayaba <= 0 :
                print ("You won")
            else :
                print ("You Lose")
        elif weapon == "3" :
            hit = int(input("ตีกี่ครั้ง "))
            for i in range (hit) :
                kayaba -= third
                print(kayaba)
            if kayaba > 0 :
                hit = int(input("ตีกี่ครั้ง "))
                for i in range (hit) :
                    kayaba -= third
                    print(kayaba) 
                if kayaba > 0 :
                    hit = int(input("ตีกี่ครั้ง "))
                    for i in range (hit) :
                        kayaba -= third
                        print(kayaba) 
            if kayaba <= 0 :
                print ("You won")
            else :
                print ("You Lose")
    else :
        print ("nothing happening")
   
