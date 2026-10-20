import re #thias allows me to use the regualr expression module: which is something that contains some special functions and data types

#Searching for a pattern in a string 
# re.serach(pattern, string)
dna = "ATTATATATCGATTAA"
if re.search(r'TTACTTGA', dna):
    #the 'r' there is raw notation we have seen it right, it is when we want python to ignore special characters like '\n', '\t' 
    print('restriction site found!') #nothing will show on terminal 
if re.search('TATATA', dna):
    print('restriction site found! 10') #this wil be outputed


#Alternation
#Say the sequence has variation or two restriction sites
dna = 'ATCGCGAATTCAC'
if re.search(r'GGACC', dna) or re.search(r'GGTCC', dna):
    print('restriction site found!') 
    #we could do this with a conditional statement OR USE another regular expression
dna = 'ATCGCGAATTCAC'
if re.search(r'GG(A|T)CC', dna): #GGACC or GGTCC
    print('restriction site found!') #no output because motif not present
# alternation feature of regular expressions. Inside parentheses, we write the alternatives separated by a pipe character, so (A|T) means either A or T. This lets us write a single pattern – GG(A|T)CC – which captures the variation 

#Character groups
#The BisI restriction enzyme cuts at an even wider range of motifs – the pattern is GCNGC, where N represents any base. We can use the same alternation technique 
dna = 'ATCGCTGCAATTCAC'
if re.search(r'GC(A|T|C|G)GC', dna): #GCAGC or GCTGC or GCGGC or GCCGC.
    print('restriction site found! 28') #no output because motif not present
# GC[ATCG]GC = GGCAGC or GCTGC or GCGGC or GCCGC....we can use charceter groups instead of || everytime
dna = 'ATCGCTGCAATTCAC'
if re.search(r'GC[ATCG]GC', dna):
    print('restriction site found! 32')

#WE can also use GC.GC and the period . indicates fopr any character betwwen them so GCTGC, GC9GC, GCPGC, GCNGC, GC7GC, GC&GC would all be regarded as true.
# Although not for two characters between them like GC9TGC is not true
if re.search(r'GC.GC', dna):
    print('restriction site found! 37')
#Sometimes it's easier, rather than listing all the acceptable characters, to specify the characters that we don't want to match. Putting a caret ^ at the start of a character group like this [^XYZ] will negate it, and match any character that isn't inthe group. 
dna = 'ATCGC9GCTGCAAGCTGCTTCAC' #THIS HAS A GC9GC AND GCTGC
if re.search('GC[^9T]GC', dna):
    print("restriction site found! 41") #no output because we dont wanna match GC9GC or GCTGC
if re.search('GC[AT]GC', dna):
    print('restriction site found! 43') #there would be an output cus there is GCTGC