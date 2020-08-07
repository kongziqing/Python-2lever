import random
def get_num(num):
    lists=[]
    for i in range(num):
        lists.append(random.randint(0,100))
    return lists

def quick_sort(lists,low,high):
    if(low<high):
        index = partition(lists,low,high)
        quick_sort(lists,low,index-1)
        quick_sort(lists,index+1,high)
def partition(lists,low,high):
    values = lists[low]
    i=low
    j=high
    while i<j:
        while i<j and lists[j]>=values:
            j-=1
        while i<j and lists[i]<=values:
            i+=1
        if(i!=j):
            swap(lists,i,j)
    swap(lists,i,low)
    return i

def swap(lists,i,j):
    lists[i],lists[j] = lists[j],lists[i]

lists=get_num(10)
quick_sort(lists,0,len(lists)-1)
print(lists)

