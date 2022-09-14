counts=0
count=dict()
Input=input("enter file name")
fhand=open(Input)
for line in fhand:
    words=line.split()
    for word in words:
        counts=counts+1
        count[word]=count.get(word,0)+1
List=[]
for (k,v) in count.items():
    newtup=(v,k)
    List.append(newtup)

List=sorted(List, reverse=True)
for (v,k) in List[:10]:
    print(v,k)
print (counts)
