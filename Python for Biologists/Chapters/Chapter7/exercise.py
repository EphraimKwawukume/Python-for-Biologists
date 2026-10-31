import re
#xkn59438, yhdck2, eihd39d9, chdsye847, hedle3455, xjhd53e, 45da, de37dp
#1.contain the number 5
accession = ['xkn59438', 'yhdck2','eihd39d9','chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp']
print('1.contain the number 5')
for accs in accession:
    if re.search(r'5',accs):
        print(accs)#xkn59438, hedle3455, xjhd53e, 45da
#2.contain the letter d or e
print('\n2.contain the letter d or e')
for accs in accession:
    if re.search(r'[de]',accs):
        print(accs)
#3.contain the letters d and e in that order
print('\n3.contain the letters d and e in that order')
for accs in accession:
    if re.search(r'd.*e',accs):#what this means is that any accs that has d and . means floowed by any other charcater ,the * means the any other charcter can be optional and repeated then the e ,so it can hbe sfhjdeff or sfhjdhguge
        print(accs)
#4.contain the letters d and e in that order with a single letter between them
print('\n4.contain the letters d and e in that order with a single letter between them')
for accs in accession:
    if re.search(r'd.e',accs): #means d then one random character then re
        print(accs)
#5.contain both the letters d and e in any order
print('\n5.contain both the letters d and e in any order')
for accs in accession:
    if re.search(r'd.*e',accs) or re.search(r'e.*d',accs):
    #if re.search(r'd.*e|e.*d',accs):#will work
        print(accs)
#6.start with x or y
print('\n6.start with x or y')
for accs in accession:
    if re.search(r'^x',accs) or re.search(r'^y',accs):
    #if re.search(r'^[xy],accs): #will work
        print(accs)
#7.start with x or y and end with e
print('\n7.start with x or y and end with e')
for accs in accession:
    if (re.search(r'^x',accs) or re.search(r'^y',accs)) and re.search(r'e$',accs):
    #if re.search(r'^xe$',accs) or re.search(r'^ye$',accs):#wont work cause it means ye or xe
    #if re.search(r'^x.*e$',accs) or re.search(r'^y.*e$',accs):#will work
    #if re.search(r'^[xy].*e$',accs):#will also work
        print(accs)
#8.contain three or more numbers in a row
print('\n8.contain three or more numbers in a row')
for accs in accession:
    #if re.search(r'[1234567890]{3,}',accs):
    #instead of writng all the numbers down we can use the character group of all digits = \d.
    if re.search(r'\d{3,}',accs):
        print(accs)
#9.end with d followed by either a, r or p
print('\n9.end with d followed by either a, r or p')
for accs in accession:
    if re.search(r'd[arp]$',accs):
        print(accs)

print('\n')
dna = open('dna.txt').read().rstrip()\
#AbcI:  ANT*AAT = A[AGTC]TAAT
#AbcII: GCRW*TG = GC[AG][AT]TG ......R is A or G ,,W is A or T
abc1 = r'A[AGTC]TAAT'
abc2 = r'GC[AG][AT]TG' 
all_cuts = [0]
print ('AbcI cuts at: ')
for match in re.finditer(abc1,dna):
    all_cuts.append((match.start() + 3))
print(all_cuts)
print ('AbcII cuts at: ')
for match in re.finditer(abc2,dna):
    all_cuts.append((match.start() + 4))
print(all_cuts)
all_cuts.append(len(dna))
print('All cuts: ' + str(all_cuts))
all_cuts.sort()
print('All cuts sorted: ' + str(all_cuts))
#calculating the length of the fragments
for i in range(1,len(all_cuts)):
    current_cut = all_cuts[i]
    previous_cut = all_cuts[i-1]
    fragment_size = current_cut - previous_cut
    print("Fragment size: " + str(fragment_size))

