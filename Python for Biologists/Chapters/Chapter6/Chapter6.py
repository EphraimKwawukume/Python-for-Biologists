print (2+2 == 4) #True
print (2 > 4) #False
print (2 <= 4) #True
print (3 != 4) #True
print ('V' in 'A,B,C') #false #is a value in a list (represented by in)
print ('V' in 'A,B,V,C') #True
print ('a' in ['a','c','b','c','d']) #True
print ('agtt' .endswith('ttt')) #False
print ('agtt' .endswith('tt')) #True
print ('agtt' .islower()) #True
print ('agtt' .isupper()) #False
print ('agtt' .startswith('abc')) #False
print ('agtt' .startswith('ag')) #True
print (len('agtt') == 5) #False
print (len('agtt') == 4) #True
print (len('agtt') > 5) #False
print ('agttctta' .count('t') == 4) #True
print ('agttctta' .count('t') > 4) #False
print ('abcd' == 'abcd') #True
print ('abcd' is 'abcd') #True
print (2+2 is 4) #True

print('\n')
#At first glance, it looks like we're printing the strings "True" and "False", but those strings don't appear anywhere in our code. What is actually being printed is the special built-in values that Python uses to represent true and false – they are capitalized so that we know they're these special values.
print (True)
print (False) #No Errors
   # print (Hello) #Error case not  special value

print('\n')
number = 126
if number > 100:
    print("working") 

accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']
for word in accs:
    if word.startswith("a"):
        print(word)

number = 200
if number > 500:
    print("number is large")
else:
    print('number is small')

file1 = open("one.txt",'w')
file2 = open('two.txt','w')
accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']
for accession in accs:
    if accession.startswith('a'):
        file1.write(accession + "\n")
    else:
        file2.write(accession + '\n')

paper1 = open('apple.txt','w')
paper2 = open('android.txt','w')
apps = ['NOTES', 'CLOCK', 'multi', 'ALERT', 'under', 'KLOE', 'number', 'orange', 'lanky'] #every letter has to be upper otherwise python would consider it as lower
for applications in apps:
    if applications.isupper(): 
        paper1.write(applications + "\n")
    else:
        paper2.write(applications  + '\n')

file1 = open("one.txt", "w")
file2 = open("two.txt", "w")
file3 = open("three.txt", "w")
accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']
for accession in accs:
    if accession.startswith('a'):
        file1.write(accession + "\n")
    else:
        if accession.startswith('b'):
            file2.write(accession + '\n')
        else:
            file3.write(accession + '\n')
    #but as we can see this bnlock has too much indentations hence python has a function called elif think of it as (and-if)

file1 = open("one.txt", "w")
file2 = open("two.txt", "w")
file3 = open("three.txt", "w")
file4 = open("four.txt", "w")
accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72', 'db67']
for accession in accs:
    if accession.startswith('a'):
        file1.write(accession + "\n")
    elif accession.startswith('b'):
        file2.write(accession + '\n')
    elif accession.startswith('d'):
        file4.write(accession + "\n")
    else:
        file3.write(accession + '\n')
#while loops
count = 0
while count < 10:
    print ("count is: " + str(count))
    count = count + 1

#Imagine we want to go through our list of accessions and print out only the ones that start with "a" and end with "3"
accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72', 'db67']
for accession in accs:
    if accession.startswith('a'):
        if accession.endswith('3'):
            print(accession)
# this nested if statements brings in an extra, unneeded level of indention os we join them using *and*
print('\n')
accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72', 'db67']
for accession in accs:
    if accession.startswith('a') and accession.endswith('3'): #this reduces the level of indentation
        print(accession)

#We can also use *or* to join up two conditions, to produce a complex condition that will be true if either of the two simple conditions are true:
accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72', 'db67']
for accession in accs:
    if accession.startswith('h') or accession.endswith('3'): #this reduces the level of indentation
        print(accession)
print('\n')
accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72', 'db67']
for accession in accs:
    if ((accession.startswith('a') or accession.startswith('d')) and accession.endswith('7')): 
        print(accession)
print('\n')
accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72', 'db67']
for accession in accs:
    if accession.startswith('a') and not accession.endswith('3'):
        print(accession)

def at_rich(dna):
    lenght = len(dna)
    A_count = dna.upper().count('A')
    T_count = dna.upper().count('T')
    AT_count = (A_count + T_count)/lenght
    #print(AT_count)
    if AT_count > 0.65:
        return True
    else:
        return False

print(at_rich('ATAGCTCGACTA'))
print(at_rich('atcggaatacacacattt'))
print(at_rich('AtatTAGCATtacatTATATATGC'))
print('\n')
#Because the last four lines of our function are devoted to evaluating a condition and returning True or False, we can write a slightly more compact version. In this example we evaluate the condition, and then return the result right away
def at_rich(dna):
    lenght = len(dna)
    A_count = dna.upper().count('A')
    T_count = dna.upper().count('T')
    AT_content = (A_count + T_count)/lenght
    #print(AT_content)
    return AT_content > 0.65

print(at_rich('ATAGCTCGACTA'))
print(at_rich('atcggaatacacacattt'))
print(at_rich('AtatTAGCATtacatTATATATGC'))