kayaba = 100
kirito = 100
first = 10
second = 15
third = 20
z = kayaba-first
k = 0 
number = int(input("สู้กด 1 หนีกด 2"))
while k < 1 :
    k = k+1
    if number == 2 :
        print ("gameover")
    elif number == 1 :
        weapon = (input("เลือกอาวุธ มี first second third"))
        if weapon == "first" :
            hit = int(input("ตีกี่ครั้ง"))
            for i in range (hit) :
                print (kayaba-first)
                first = first+10
            if kayaba > 0 :
                print ("You Did not win yet")
                hit = int(input("ตีกี่ครั้ง"))
                for i in range (hit) :
                    print (kayaba-first)
                    first = first+10
                if kayaba > 0 :
                    print ("You Did not win yet")
                    hit = int(input("ตีกี่ครั้ง"))
                    for i in range (hit) :
                        print (kayaba-first)
                        first = first+10
            if kayaba <= 0 :
                print ("You won")
            else :
                print ("You Lose")
        elif weapon == "second" :
            hit = int(input("ตีกี่ครั้ง"))
            for i in range (hit) :
                print (kayaba-second)
                second = second+15
            if kayaba <= 0 :
                print ("You won")
            else :
                print ("You Lose")
        elif weapon == "third" :
            hit = int(input("ตีกี่ครั้ง"))
            for i in range (hit) :
                    print (kayaba-third)
                    third = third+20
            if kayaba <= 0 :
                print ("You won")
            else :
                print ("You Lose")
        
    else :
        print ("nothing happening")
   
