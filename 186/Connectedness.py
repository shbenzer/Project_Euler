import sys #io

def s(k): #sequence generator
    if k < 56:
        return (100003 - 200003*k + (300007*pow(k,3))) % 1000000

def S(k):
    if k < 56:
        return ks[k-1]
    else: 
        return(S(k-24) + S(k-55)) % 1000000

""" Solution 1: Brute force method, do not recommend
def findMutualFriends(caller):
    for caller in record[1]:
        stats[1]+=1
        temp = record[1].index(caller)
        findMutualFriends(record[0][temp])
    for caller in record[1]:
        record[1].remove(caller)
    for caller in record[0]:
        record[0].remove(caller)
    return

def makeCall(count):
    caller = s(2*count-1)
    called = s(2*count)
    print(count)
    print(caller)
    print(called)
    stats[0]+=2
    if(caller in friends and called in friends):
        stats[1]+=2
        return
    elif((called or caller) in friends):
        record[0].append(caller)
        record[1].append(called)
        findMutualFriends(caller)
        return
    else:
        record[0].append(caller)
        record[1].append(called)
        return
"""  

""" Solution 2: Brute Force Method with Classes; more memory efficient
class User:
    number = 0;
    friends = []; #list of users
    
    def __init__(self,number):
        self.number = number
    
    def add_friend(self,friend):
        self.friends.append(friend)
    
    def getFriends(self):
        return friends

class PrimeMinister:
    number = 0;
    friends = []; #list of user numbers
    
    def __init__(self, number):
        self.number = number
    
    def add_friend(self,friend_number):
        self.friends.append(friend_number)
    
    def getFriends(self):
        return friends
        
def makeCall(n,calls,friends):
    caller = s(2*n[0]-1)
    called = s(2*n[0])
    
    if(caller == called): #misdial
        n[0]+=1
        return
    
    caller = User(caller)
    called = User(called)

    for user in users:
        if user.number == caller.number:
            caller = user
            break
    for user in users:
        if user.number == called.number:
            called = user
            break
    caller.add_friend(called)
    called.add_friend(caller)
    
    
    #check for prime minister
    if caller.number == pm.number:
        pm.add_friend(called.number)
        findMyFriends(called)
        n[0]+=1
        friends[0]+=1
        calls[0]+=1
        return
    if called.number == pm.number:
        pm.add_friend(caller.number)
        findMyFriends(caller)
        n[0]+=1
        friends[0]+=1
        calls[0]+=1
        return
    
    #check for prime minister's friends
    if caller.number in pm.friends:
        if(called.number in pm.friends): #if they're both in there, no point
            n[0]+=1
            friends[0]+=1
            calls[0]+=1
            return
        else:
            findMyFriends(called,pm)
            n[0]+=1
            calls[0]+=1
            return
    elif called.number in pm.friends:
        if(caller.number in pm.friends):
            n[0]+=1
            friends[0]+=1
            calls[0]+=1
            return
        else:
            findMyFriends(caller,pm)
            n[0]+=1
            calls[0]+=1
            return
    else:
        users.append(caller)
        users.append(called)
        n[0]+=1
        calls[0]+=1
        return
        
            
        
def findMyFriends(user,pm):  #I'm very funny
    for friend in user.friends:
        findMyFriends(friend,pm)
        if friend.number not in pm.friends:
            pm.add_friend(friend)
            friends[0]+=1
        else:
            friends[0]+=1
"""

inputs = sys.stdin.readline() #read input
inputs = inputs.split(" ") #format input
pm = int(inputs[0]) #push prime minister into parameter
p = int(inputs[1]) #push desired percentage into parameter
n = 0 #record number
normiesIn = [] #list of callers
normiesOut = [] #list of calleds
calls = 0 #count of successful calls; 2*count = total users for percentage calc
friends = [0] #count friends
ks = []
cool_kids = [pm]

""" Solution 3: Brute Force, but even better
def coolNow(number):
    for number in normiesIn:
        temp = normiesIn.index(number)
        tempIn = normiesIn.pop(temp) #remove caller from log
        tempOut = normiesOut.pop(temp) #remove called from log
        friends[0]+=1
        if tempIn not in cool_kids:
            cool_kids.append(tempIn)
        if tempOut in cool_kids:
            friends[0]+=1
        else:
            coolNow(normiesOut[temp])
    for number in normiesOut:
        temp = normiesOut.index(number)
        tempIn = normiesIn.pop(temp) #remove caller from log
        tempOut = normiesOut.pop(temp) #remove called from log
        friends[0]+=1
        if tempOut not in cool_kids:
            cool_kids.append(tempOut)
        if tempIn in cool_kids:
            friends[0]+=1
        else:
            coolNow(normiesIn[temp])
    return
    
for i in range (1,56):
    ks.append(s(i))

while (calls == 0) or (friends[0]/2*calls < p):
    print(cool_kids)
    n+=1
    caller = S(2*n)
    called = S(2*n-1)
    
    if caller == called:
        continue
    
    if caller in cool_kids:
        friends[0]+=1
        calls+=1
        if called in cool_kids:
            friends[0]+=1
            continue
        else:
            coolNow(called)
    elif called in cool_kids:
        friends[0]+=1
        calls+=1
        if caller in cool_kids:
            friends[0]+=1
            continue
        else:
            coolNow(caller)
    calls+=1
    normiesIn.append(caller)
    normiesOut.append(called)

print(calls)

"""
    
    
    
    

    






