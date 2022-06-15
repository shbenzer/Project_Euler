import sys #io functionality

""" Solution 1: Far too slow and memory intensive; creates every fibonacci string
def fibIt(a,b,n):
    
    #checks for easy out
    if (len(a) >= n):
        return a
    elif (len(b) >= n):
        return b
    elif (len(a+b) >= n):
        return a+b
    else:
        temp_arr = [a+b,b+a+b] #temp array to hold n-1 and n-2; starts at n=3,n=4 for optimization
        while(len(temp_arr[1]) < n):
            temp = temp_arr[0]+temp_arr[1]
            temp_arr[0] = temp_arr[1]
            temp_arr[1] = temp
            del(temp)
        return temp_arr[1]
"""
"""Solution 2; uses 'a' and 'b' as string representation to decrease memory cost
def fibIt(a,b,n):
    lenA = len(a)
    lenB = len(b)
    #checks for easy out
    if (len(a) >= n):
        return indexIt('a',n,a,b)
    elif (len(b) >= n):
        return indexIt('b',n,a,b)
    elif (len(a+b) >= n):
        return indexIt('ab',n,a,b)
    else:
        temp_arr = ['ab','bab'] #temp array to hold n-1 and n-2; starts at n=3,n=4 for optimization
        while(((temp_arr[1].count('a')*lenA)+(temp_arr[1].count('b')*lenB) < n)):
            temp = temp_arr[0]+temp_arr[1]
            temp_arr[0] = temp_arr[1]
            temp_arr[1] = temp
            del(temp)
        return indexIt(temp_arr[1],n,a,b)
            
def indexIt(fib,index,a,b):
    lenA = len(a)
    lenB = len(b)
    while(index > (lenA or lenB)):
        if fib[0] == 'a':
            fib = fib[1:]
            index -= lenA
        elif fib[0] == 'b':
            fib = fib[1:]
            index -= lenB
        else:
            print('Incorrect parameter provided')
            return
    if(fib[0] == 'a'):
        return a[index-1]
    elif(fib[0] == 'b'):
        return b[index-1]
    else:
        print('Incorrect parameter provided')
        return
"""

""" Solution 3 (UNFINISHED); calculates the length of the sequence needed, then attempts to figure out if it index is in string 'a' or 'b'; much less memory intensive; much faster
def fibIt(a,b,n):
    lenA = len(a)
    lenB = len(b)
    temp_arr = [lenA,lenB] #temp array to calculate further sequences
    while (temp_arr[-1] < n):
        temp_arr.append(temp_arr[-2]+temp_arr[-1])
    #print(temp_arr)
    seqNum = len(temp_arr)-1
    while(n > (lenA+lenB)):
        if(temp_arr[seqNum]<n):
            n = n - temp_arr[seqNum]
            seqNum -= 1
        else:
            n = temp_arr[seqNum] - n
        seqNum -= 1
    if(n > lenA):
        n -= lenB
        temp = a
    else:
        temp = b
    #print(n)
    return temp[n-1]
"""

#populate parameters
inputs = []
a = []
b = []
n = []

for lines in sys.stdin: #read inputs to array
    inputs.append(lines.replace("\n","")) #remove formatting

q = int(inputs[0])

for i in range (1,q+1):
    temp = inputs[i].split(" ")
    a.append(temp[0])
    b.append(temp[1])
    n.append(int(temp[2]))

for i in range (0,q):
    print(fibIt(a[i],b[i],n[i]))
