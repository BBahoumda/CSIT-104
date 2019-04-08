from random import randint
def BubbleSort(l):
    e=0
    for i in range(len(l)-1):
        for j in range(len(l)-1):
            if l[j]>l[j+1]:
                e=l[j+1]
                l[j+1]=l[j]
                l[j]=e
    return l
def MyPrint(L,pb):
        BubbleSort(L)
        print "Your numbers: %d %d %d %d %d Powerball: %d" %(L[0],L[1],L[2],L[3],L[4],pb)

print "Official (but fruitless) Powerball number generator"
No=int(raw_input("How many sets of numbers? "))
for i in range(No):
    numbers=[]
    powerball=randint(1,42)
    i=0
    while (i!=5):
        numbers.append(randint(1,53))
        i+=1
    for i in range(len(numbers)-1):
        for j in range(len(numbers)-1):
            if i==j:
                j+=1
            if numbers[i]==numbers[j] or powerball==numbers[j]:
                numbers[j]=randint(1,53)
                j-=1
    MyPrint(numbers,powerball)
