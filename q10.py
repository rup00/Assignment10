for i in range(15,45):
    count=0
    for j in range(2,i):
        if(i%j==0):
            count+=1
        else:
            pass
    if(count==0):
        print(i)
