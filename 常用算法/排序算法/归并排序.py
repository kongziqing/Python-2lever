#归并排序算法
#三步：分解，求解，组合
def mergesort(data):
    if len(data)<=1:
        return data
    mid = int(len(data)/2)
    left = mergesort(data[:mid])
    right = mergesort(data[mid:])
    return merge(left,right)

def merge(left,right):
    i,j=0,0
    result=[]
    while i<len(left) and j<len(right):
        if left[i] >=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result+=left[i:]
    result+=right[j:]
    return result
data=[2,4,5,6,1,3,-1,-3,-4]
print(mergesort(data))



