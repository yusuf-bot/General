
ListOT=[]
ledger=dict()
while True:
    account=input("Enter name of your current or new account")
    ans=input("do u want to deposit or withdraw, or other")
    if ans=='deposit':
        amount=input("$")
        amount =float(amount)
        ledger[account]=ledger.get(account,0)+ amount
        ListOT.append([account,'+',amount])
    if ans=='withdraw':
        amount=input("$")
        amount =float(amount)
        ledger[account]=ledger.get(account,0)- amount
        if (ledger[account])<0:
            print ('not enough funds')
            ledger[account]=ledger.get(account,0)-+amount
        else:
            ListOT.append([account,'-',amount])
    if ans=='other':
        ans2=input('do u want to transfer, print records or other')
        if ans2=='transfer':
            transfee=input('whr do u wanna transfer')
            amount=input("$")
            amount=float(amount)
            ledger[transfee]=ledger.get(transfee,0)+ amount
            ledger[account]=ledger.get(account,0)- amount
            if (ledger[account])<0:
                ledger[transfee]=ledger.get(transfee,0)- amount
                ledger[account]=ledger.get(account,0)+ amount
                print ("Not enough funds")
            else:
                ListOT.append([account,'Transfer to', transfee, '-', amount])
                ListOT.append([transfee,'Transfer from', account, '+', amount])

        if ans2=='print':
            print ('--------------', account, '--------------')
            account=str(account)
            for x in ListOT:
                for y in x:
                    if y!=account:
                        continue
                    else:
                        if x[1]=='Transfer to' or x[1]=='Transfer from':
                            print (x[1:3], ':', '   ', str(x[4:]))
                        elif x[1]=='+':
                            print ('Deposit:              ', str(x[2:]))
                        else:
                            print ('Withdrawal:              ', str(x[2:])
                        
            print ('--------------------------------------')
            print ('$                         ', str(ledger[account]))
            print (ListOT)

            if ans2=='other':
                ans3=input('do you want to see the balance, or want to end')
                if ans3=='show balance':
                    print (str(ledger[account]))
                if ans3=='end':
                    break





