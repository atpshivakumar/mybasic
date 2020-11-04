def Maxeras(n,list1,list2):
    count=0
    totallist=[]
    for m in list1:
        for n in list2:
            templist=[]
            if(list1.index(m)==list2.index(n)):
                if(int(m)>0 and int(n)>0):
                    templist=list(range(int(m),int(n)+1))
                    
                elif(int(m)<0 and int(n)<0):
                    templist=list(range(int(n),int(m)+1))
                    
                totallist.extend(templist)
                
    finalset=sorted(totallist)
    #print(finalset)
    #print(type(finalset))

    for i in range(0,len(finalset)-2):
        if(finalset[i+1]-finalset[i]>1):
            count=count+1
    print(count+1)        

N=input("enter number")
a=input("enter list with spaces")
b=input("enter list with spaces")
a=list(a.split(" "))
b=list(b.split(" "))
Maxeras(N,a,b)
