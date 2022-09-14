#madlib
name=input()
adj=input()
madlib=f"hello! my name is {name}! computer secience is {adj}"
print (madlib)

#guess random no. by user
import random
def guess(x):
    number=random.randint(0,x)
    guess=-1
    while guess!=number:
        guess=int(input(f"enter a number between 0 and {x}"))
        if guess>number:
            print ("number too high")
        elif guess<number:
            print ("number too small")
    print (f"yay{number}")
        
num=int(input())
guess(num)


#guess number by comp.
def comp_guess(low,high):
    feedback=''
    while feedback!='c' :
        if low!=high:
        num=random.randint(low,high)
        else:
            guess=low
        feedback=str(input(f"is the number {num}, if its higher (h), if its lower (l), if its correct (c)"))
        if feedback =='h':
            high=num-1
        elif feedback == 'l':
            low=num+1
    print ('yay')

low=int(input("LOW:"))
high=int(input("HIGH:"))
comp_guess(low,high)    
