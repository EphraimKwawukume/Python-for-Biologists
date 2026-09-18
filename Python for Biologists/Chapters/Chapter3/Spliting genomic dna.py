#Splitting genomic text into exons and introns and writing to two different files

my_file = open("genomic_dna.txt")
genomic_dna = my_file.read().rstrip("\n")
print(genomic_dna + "\nlength of sequence:  " +str(len(genomic_dna)))
exons = genomic_dna[:62] +genomic_dna[90:123]
print("exons: " + exons)
introns = genomic_dna[62:90]
print("introns: " + introns)
print(len(exons) + len(introns) == len(genomic_dna))
my_file1 = open("exons.txt","w")
my_file1.write(exons)
print("\n")
my_file2 = open('introns.txt','w')
my_file2.write(introns)

my_file.close()
my_file2.close()
my_file1.close()
#