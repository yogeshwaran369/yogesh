#hand cricket:
import random
score=0
c_score=0
comip=["batting","bowl"]
a=input("choose odd or even:")
b=int(input("enter no"))
com1=random.randint(1,6)
print(com1)
res=b+com1
if(res%2==0):
    res="even"
else:
    res="odd"
    
if(res==a):
    print("you won the toss")
    a1=input("Choose batting or bowling".lower())
    if(a1=="batting"):
        print("start play")
        for i in range(10):
            a3=int(input())
            com=random.randint(1,6)
            if(a3==com):
                print("match over-your out")
                break
            else:
                score+=a3
        print("your score ",score)
        print("1st_off_over")
        print("target",score)
        print("start bowl")
        for i in range(10):
            a3=int(input())
            com=random.randint(1,6)
            if(a3==com ):
                print("match_over computer out")
                break
            else:
                c_score+=com
        print("commputer score",c_score)
        if(score>c_score):
             print("you won the game")
        elif(score==c_score):
            print("match tie")
        else:
            print("computer won ")

    elif(a1=="bowling"):
        print("start bowl")
        for i in range(10):
            a4=int(input())
            com=random.randint(1,6)
            if(com==a4):
                print("match over-computer out")
                break
            else:
                c_score+=com
        print("computer score",c_score)
        print("1st_off_over")
        print("targert",c_score)
        print("start play")
        for i in range(10):
            a3=int(input())
            com=random.randint(1,6)
            if(a3==com ):
                print("match over-your out your result |below|")
                break
            else:
                score+=a3
        print("your score",score)
        if(score>c_score):
            print("you won the game")
        elif(score==c_score):
            print("match tie")
        else:
            print("computer won ")
           
                
else:
    print("computer won the toss")
    comip1=random.choice(comip)
    print("computer choose to ",comip1)
    if(comip1=="batting"):
        print("start bowl")
        for i in range(10):
            a5=int(input())
            com=random.randint(1,6)
            if(a5==com):
                print("match over-computer out")
                break
            else:
                c_score+=a5
        print("computer score ",c_score)
        print("1st_off_over")
        print("target",c_score)
        print("start batting")
        for i in range(10):
            a=int(input())
            com=random.randint(1,6)
            if(com==a):
                print("match over-computer out")
                break
            else:
                score+=a
        if(score>c_score):
            print("you won the game")
        elif(score==c_score):
            print("match tie")
        else:
            print("computer won ")
    elif(comip1=="bowl"):
        print("start batting")
        for i in range(10):
            a=int(input())
            com=random.randint(1,6)
            if(com==a):
                print("match over-your'e out")
                break
            else:
                score+=a
        print("your_score",score)
        print("1st_off_over")
        print("target=",score)
        print("start bowl")
        for i in range(10):
            a5=int(input())
            com=random.randint(1,6)
            if(a5==com):
                print("match over-computer out")
                break
            else:
                c_score+=com
        print("computer score ",c_score)
        if(score>c_score):
            print("you won")
        elif(score==c_score):
            print("mathch tie")
        else:
            print("computer won")
            
             
    
        

           
   
       
   

