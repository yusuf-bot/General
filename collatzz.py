print('This is a way to watch the collatz conjecture!')
x=int(input('Enter any natural number: '))
print('')
count=0
List=[]

while x>=1:
    List.append(x)
    print(x, '', end='')
    for y in range(0, x):
        print("*", end='')
    print('')
    if x%2==0:
        x=x/2
        x=int(x)
        count+=1
    else:
        if x==1:
            print (f"there were {count} steps")
            break
        else:
            x=(3*x)+1
            x=int(x)
            count+=1
if x==1:
    High=0
    for y in List:
        if y>High:
            High=y

print (f'the largest number was {High}!')
