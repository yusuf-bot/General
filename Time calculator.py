def add_time(x,y):
    day=0
    e=0
    X=x.split(':')
    for a in X[:1]:
        a=int(a)
        aa=a
        if a>12:
            print ("error")
    for b in X[1:]:
        bbb=b.split()
        for bbbb in bbb[:1]:
            bbbb=int(bbbb)
            bb=bbbb
            if bb>60:
                print ("error")
        for bbbb in bbb[1:]:
            bbbbb=bbbb
        
    Y=y.split(':')
    for c in Y[:1]:
        c=int(c)
        cc=c
    for d in Y[1:]:
        d=int(d)
        dd=d

    f=bb+dd
    while f>=60:
        f=f-60
        e=e+1
        
    e=cc+aa+e
    while e>12:
        e=e-12
        if bbbbb=='a.m':
            bbbbb='p.m'
        else:
            bbbbb='a.m'
            day=day+1

    if day==0:
        print (e,':',f, bbbbb)
    elif day==1:
        print (e,':',f, bbbbb, 'next day')
    else:
        print (e,':',f, bbbbb, day, 'days later')

for x in range (5):
    A=input("Enter time: ")
    B=input("Enter time difference: ")
    add_time (A,B)

