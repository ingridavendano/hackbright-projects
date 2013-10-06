'''
mystery1 rounds a float up to an int if the decimal is above 0.5 or rounds down
if decimal is below 0.5
'''
def mystery1(inp):
    base = int(inp)
    if inp - base >= 0.5:
        return base+1
    else:
        return base


'''
mystery2 returns how many new lines are in a string
'''
def mystery2(inp):
    if not inp:
        return 0
    num = 1
    for c in inp:
        if c == "\n":
           num  += 1    
    return num


'''
mystery3 is the Pythagorean theorem and returns c in a^2 + b^2 = c^2
'''
def mystery3(a, b):
    c = a * a + b * b
    return Math.sqrt(c)

    
'''
myster4 reverses order of values in a list 
'''
def mystery4(inp):
    size = len(inp)
    for i in range(len(inp)/2):
        temp = inp[i]
        inp[i] = inp[size-i-1]
        inp[size-i-1] = temp
        
    return inp


'''
mystery5 goes through a text file and creates a dict of words and how
many times each word appears and then prints the results
'''
def mystery5():
    inp = open("sample_input.txt")
    ws = inp.split()
    h = dict()
    for w in ws:
        num = h.get(w, 0)
        num += 1
        h[w] = num
    
    for k, v in h.iteritems():
        print "%s:\t%d"%(k, v)


'''
mystery6 goes through a list of numbers and sorts the list from values
going low to high
'''
def mystery6(inp):
    swapped = True
    while swapped == True:
        swapped = False
        for i in range(len(inp)-1):
            if inp[i] > inp[i+1]:
                tmp = inp[i]
                inp[i] = inp[i+1]
                inp[i+1] = inp[i]
                swapped = True

