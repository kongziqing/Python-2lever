#插入排序
def insertsort(mylist):
    #获取列表长度
    length = len(mylist)
    for i in range(1,length):
        j=i-1
        if (mylist[i]<mylist[j]):
            temp=mylist[i]
            mylist[i] = mylist[j]
            j=j-1
            while j>=0 and mylist[j]>temp:
                mylist[j+1] = mylist[j]
                j=j-1
            mylist[j+1]=temp
mylist = [3,4,6,72,2,5,-1,5]
insertsort(mylist)
print(mylist)