Input=[]
er=1
while er==1:
    ope=input('enter operation with spaces, to end press x')
    if ope=='x':
        break
    Input.append(ope)
ans=str(input("do you want to see the answer"))
def artemic_calc(List):
    for x in List:
        print (' ')
        print (' ')
        y=x.split()
        for z in y[:1]:
            print ('  ',z)
            z=int(z)
            b=z
        for z in y[1:2]:
            print (z, end=' ')
        for z in y[2:3]:
            print (" ",z)
            z=int(z)
            a=z
        for z in y[1:2]:
            if z=='+':
                Res=b+a
            else :
                Res=b-a

        print ('------')
        if ans=='Y':
            print (Res)
        else:
            print (' ')
        print ('--------')
artemic_calc(Input)
