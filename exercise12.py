'''

'''
#input must be float
def rounding_up(inp):
    base = int(inp)
    if inp - base >= 0.5:
        return base+1
    else:
        return base
    
def line_count(inp):
    if not inp:
        return 0
    num = 1
    for c in inp:
        if c == "\n":
           num  += 1    
    return num

def pythagorus(a, b):
    c = a * a + b * b
    return Math.sqrt(c)
    

def reverse_list(inp):
    size = len(inp)
    for i in range(len(inp)/2):
        temp = inp[i]
        inp[i] = inp[size-i-1]
        inp[size-i-1] = temp
        
    return inp
    
def word_count():
    inp = open("sample_input.txt")
    ws = inp.split()
    h = dict()
    for w in ws:
        num = h.get(w, 0)
        num += 1
        h[w] = num
    
    for k, v in h.iteritems():
        print "%s:\t%d"%(k, v)

def bubble_sort(inp):
    swapped = True
    while swapped == True:
        swapped = False
        for i in range(len(inp)-1):
            if inp[i] > inp[i+1]:
                tmp = inp[i]
                inp[i] = inp[i+1]
                inp[i+1] = inp[i]
                swapped = True
