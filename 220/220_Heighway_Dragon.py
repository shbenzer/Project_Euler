import sys #io functionality
import copy #deep copy functionality

def convertFromHex(hexVal): #converts from hex to base 10
    sign = 1
    if(hexVal[0] == '-'): #account for negatives
        sign = -1
        hexVal = hexVal.lstrip('-')
    digitCount = len(hexVal)-1
    result = 0
    for digit in hexVal:
        conversion = hexArray.index(str(digit))
        result += (conversion*(16**digitCount))
        digitCount-=1
    return result

def convertToHex(decimalVal): #converts from base 10 to hex
    sign = ""
    if(decimalVal < 0): #account for negatives
        sign = "-"
        decimalVal = abs(decimalVal)
    result = ""
    remainder = None
    if(decimalVal%16 == 0): #check for easy multiples of 16
        return sign+str(int(decimalVal/1.6))
    while (remainder != 0):
        remainder = decimalVal%16
        decimalVal = int(decimalVal/16) #parses result to int
        result = hexArray[remainder] + result
    if(len(result) > 1):
        result = result.lstrip('0')
    return sign+result
        
def derive(derivations,string):
    for n in range (0,derivations):
        temp = ""
        for letter in range(0,len(string)):
            if string[letter] == 'a': #derivation rule 1
                temp += 'aRbFR' 
            elif string[letter] == 'b': #derivation rule 2
                temp += 'LFaLb'
            else:
                temp += string[letter]
        string = copy.deepcopy(temp) #saves derivedString as temp and allows for changing temp in further iterations
    return string

def move(char,currentDirection,currentLocation): #direction based on unit circle
    if char == 'R':
        currentDirection[0]-=90 
        return
    elif char == 'L':
        currentDirection[0]+=90
        return
    elif char == 'F':
        cDmod360 = currentDirection[0] % 360 # calculates current direction on unit circle
        if cDmod360 == 90:
            currentLocation[0]+=1
            return
        elif cDmod360 == 180:
            currentLocation[1]+=1
            return
        elif cDmod360 == 270:
            currentLocation[0]-=1
            return
        elif cDmod360 == 0:
            currentLocation[1]-=1
            return
        else:
            print("currentDirection is invalid") #catch error
            return    
    elif char == 'a':
        return
    elif char == 'b':
        return
    else:
        print("invalid direction read") #catch error
        return
        
def dragon(derivedString,moves):
    currentDirection = [180] #using a list because it's mutable (similar to using pointers in C++)
    currentLocation = [0,0]
    i=0 #times moved forward
    for chars in derivedString:
        if(i<moves):
            if(chars == 'F'):
                i+=1
            move(chars,currentDirection,currentLocation)
        else:
            break
    print(convertToHex(currentLocation[0])) #print final x-coord
    print(convertToHex(currentLocation[1])) #print final y-coord

#populate parameters
inputs = []
n = [] #derivations to perform
m = [] #number of moves to make
startString = "Fa" #underived string
hexArray =['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'] #array of hex values, indices corresponds to decimal equivalence

###main args###

for lines in sys.stdin: #read inputs to array
    inputs.append(lines.replace("\n","")) #remove formatting

q = inputs[0] #processes to run

for x in range (1,len(inputs),2):
    n.append(int(inputs[x]))
    m.append(convertFromHex(inputs[x+1]))

for i in range (0,int(q)):
    dragon(derive(n[i],startString),m[i])
    
    



