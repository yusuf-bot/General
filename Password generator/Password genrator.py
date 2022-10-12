import random
def PassGen():
    lower='abcdefghijklmnopqrstuvwxyz'
    upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num='0123456789'
    sym='!@#$%^&*(_+/|}><?'
    use=lower+upper+num+sym
    lent=12
    Password="".join(random.sample(use,lent))
    Input=input('wht do u want thwe password for?  ')
    Password=Input+Password
    file=open('passwords.txt','a')
    file.write(f'The password for {Input} is {Password}')
    file.close()