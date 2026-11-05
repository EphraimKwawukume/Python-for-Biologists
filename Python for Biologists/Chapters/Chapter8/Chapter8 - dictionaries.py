enzymes = { 'EcoRI':r'GAATTC', 'AvaII':r'GG(A|T)CC', 'BisI':r'GC[ATGC]GC' }
#OR to make it easier to read
enzymes = {
    'EcoRI':r'GAATTC',
    'AvaII':r'GG(A|T)CC',
    'BisI':r'GC[ATGC]GC' 
} 
print(enzymes['BisI'])
#The code looks very similar to using a list, but instead of giving the index of the element we want, we're giving the key for the value that we want to retrieve.
#the EcoRi is known as Key
#and the GAATTC is known as Value
#Dictionaries are a very useful way to store data, but they come with some restrictions. The only types of data we are allowed to use as keys are strings and numbers2, so we can't, for example, create a dictionary where the keys are file objects. Values can be whatever type of data we like. Also, keys must be unique – we can't store multiple values for the same key.

#creating an empry dictionary and adding elemets to it
enzymes = {} #similar to lists but instead of [],we use {}
enzymes['EcoRI'] = r'GAATTC'
enzymes['AvaII'] = r'GG(A|T)CC'
enzymes['BisI']  = r'GC[AGTC]GC'
enzymes['AbsI']  = r'GC[AT][AG]GG'
print(enzymes['AbsI'])
#We can delete a key from a dictionary using the pop method. pop actually returns the value and deletes the key at the same time:
removed = enzymes.pop('EcoRI')#because it returns a value ,which is the value is has deleted ,so we can store it in a variable
print('removed enzyme: ' + removed)#Output: removed enzyme: GAATTC
print(enzymes)#Output: {'AvaII': 'GG(A|T)CC', 'BisI': 'GC[AGTC]GC', 'AbsI': 'GC[AT][AG]GG'}
dna = "AATGATCGATCGTACGCTGA"
counts = {}
for base1 in ['A', 'T', 'G', 'C']:
    for base2 in ['A', 'T', 'G', 'C']:
        for base3 in ['A', 'T', 'G', 'C']:
            trinucleotide = base1 + base2 + base3
            count = dna.count(trinucleotide)
            counts[trinucleotide] = count
print(counts)
#now we can find the counts for any trinucloetide easily comapred to using lists
print('TGA counts: ' + str(counts['TGA']))
#if we want to remove the plenty zeros in the output
dna = "AATGATCGATCGTACGCTGA"
counts = {}
for base1 in ['A', 'T', 'G', 'C']:
    for base2 in ['A', 'T', 'G', 'C']:
        for base3 in ['A', 'T', 'G', 'C']:
            trinucleotide = base1 + base2 + base3
            count = dna.count(trinucleotide)
            if count > 0:
                counts[trinucleotide] = count
print(counts)
print('ATC counts: ' + str(counts['ATC']))#Output :TGA counts: 2
#print('AAA counts: ' + str(counts['AAA']))#Output :Key Error 
# Due to the fact we removed the zero count trinucleotides now when the count is zero, the trinucleotide doesn't appear as a key in the dictionary
#To get around this we can use the dictionary's get method. get usually works just like using square brackets: the following two lines do exactly the same thing:
print(counts['TGA'])
print(counts.get('TGA'))
#The thing that makes get really useful, however, is that it can take an optional second argument, which is the default value to be returned if the key isn't present in the dictionary. In this case, we know that if a given trinucleotide doesn't appear in the dictionary then its count is zero, so we can give zero as the default value and use get to print out the count for any trinucleotide:
print('count for TGA is: ' + str(counts.get('TGA','0')))
print('count for AAA is: ' + str(counts.get('AAA','0')))
print('count for CGT is: ' + str(counts.get('CGT','0')))
print('count for TCG is: ' + str(counts.get('TCG','0')))
print('count for ACA is: ' + str(counts.get('ACA','0')))