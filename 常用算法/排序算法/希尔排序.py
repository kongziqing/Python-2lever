#希尔排序
def shell_sort(seq):
    index = len(seq)//2
    n=len(seq)
    while(index>=1):
        for i in range(index,n):
            j=i
            while(j-index>=0):
                if seq[j]<seq[j-index]:
                    seq[j],seq[j-index]=seq[j-index],seq[j]
                    j=j-index
                else:
                    break
        index=index//2
seq = [9,7,6,-1,39,10]
shell_sort(seq)
print(seq)