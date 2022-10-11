y=''
Input=input("f(x)=  ")
print('')
NewFormula=[]
Variable0=[]
Formula=Input.split()
for x in Formula:
    Variable=x.split('^')
    if len(Variable)>1:
        for a in Variable[1:]:
            y=a
        exp=y
        y=''
        for a in Variable[:1]:
            b=a.split('x')
            for c in b:
                y=y+c

        coe1=y
        coe=(int(coe1))*(int(exp))
        exp=int(exp)
        exp=exp-1
        Variable=f'{coe}x^{(exp)}'
        NewFormula.append(Variable)
    else:
        Variable=str(Variable[:1])
        Variable=Variable.rstrip(']')
        Variable = Variable.rstrip("'")
        Variable=Variable.lstrip('[')
        Variable = Variable.lstrip("'")
        for d in Variable:
            if d=='x':
                Variable0=Variable.split('x')
                for y in Variable0[:1]:
                    y=y
                Variable=y
                NewFormula.append(y)

print('dy/dx=  ',end='')
for x in NewFormula:
    print(x,'',end='')
