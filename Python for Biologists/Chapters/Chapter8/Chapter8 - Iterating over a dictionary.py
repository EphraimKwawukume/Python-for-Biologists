#What if, instead of looking up a single item from a dictionary, we want to do something for all items? For example, imagine that we wanted to take our counts dictionary variable from the code above and print out all trinucleotides where the count was 2. One way to do it would be to use our three nested loops again to generate all possible trinucleotides, then look up the count for each one and decide whether or not to print it
dna = "AATGATCGATCGTACGCTGA"
counts = {}
for base1 in ['A', 'T', 'G', 'C']:
    for base2 in ['A', 'T', 'G', 'C']:
        for base3 in ['A', 'T', 'G', 'C']:
            trinucleotide = base1 + base2 + base3
            count = dna.count(trinucleotide)
            if count == 2:
                 counts[trinucleotide] = count
print(counts)
#but this is inefficient
#Iterating over keysWhen used on a dictionary, the keys method returns a list of all the keys in the dictionary:
print(counts.keys())