#1.Printing out the AT content of a sequence

dna='ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT'
A_count=dna.count('A')
T_count=dna.count('T')
AT_count=A_count+T_count
AT_content=AT_count/len(dna)

print(dna+'\nsize of dna: '+ str(len(dna)))
print("A+T count: "+ str(AT_count) +"\nAT content: " + str(AT_content))


#2.Complementing DNA 

dna2="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
print(dna2)

A_replace=dna2.replace('A','t')
print(A_replace)

T_replace=A_replace.replace('T','a')
print(T_replace)

G_replace=T_replace.replace('G','c')
print(G_replace)

C_replace=G_replace.replace('C','g')
print(C_replace)
print(C_replace.upper())

#this is becauee the replace fucntion is case sensitive

#3.Restriction fragment lengths

dna3='ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT'
print(dna3)

#E.CORI enzyme cleaves at G_AATTC so we have to find the location of that motif,but first lets count 

print(len(dna3))
print(dna3.count('AATTC'))
#luckily its only ONE
 
print(dna3.find('AATTC'))
#at position 22
#now we have to find the substring and size of it or we just find the size of dna3 and subtract from 21 as the second fragment

#print('size of fragment one: '+ str(len(dna3)-21)) this works for the fragment but doing the other fragment would require too much thinking....instead 
#lets extract the substrings

fragment1=dna3[0:22]
fragment2=dna3[22:55]
print('fragment1: '+fragment1 +'\nsize of fragment1: '+ str(len(fragment1)))
print('fragment2: '+fragment2 +'\nsize of fragment2: '+ str(len(fragment2)))


#4.Splicing out introns

dna4='ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT'

print(dna4+'\ndna4 size: '+str(len(dna4)))
#1.dna4 size is 123

#first exon from the first to 63 and second exon 91 to end ,goal is to print out only the coding regions

coding_regions=dna4[0:62]+dna4[90:123]
print("coding regions: " + coding_regions)

#2.calculate what percentage of the DNA sequence is coding.
percentCoding=(len(coding_regions)/len(dna4))*100
print('Percentage of the DNA sequence which is coding: ' + str(percentCoding)+'%')

#3.Using the data from part one, write a program that will print out the original genomic DNA sequence with coding bases in uppercase and non-coding bases in lowercase
exon1=dna4[0:62]
exon2=dna4[90:123]
intron=dna4[62:90]
print(exon1+intron+exon2)



#TESTING MY INDEX KNOWLEDGE
#Exon 1: Starts at the 1st base and ends at the 16th base
#Intron 1: Sits between Exon 1 and Exon 2.
#Exon 2: Starts at the 35th base and ends at the 58th base.
#Intron 2: Sits between Exon 2 and Exon 3.
#Exon 3: Starts at the 73rd base and runs to the end of the sequence.

gene_seq = "ATGAAAGTCGGTACCAAGGTGAGTTTTAGCGATCGATAGCTACGATCGATCGCCATCGTAGCTAGCTAAGGTTCCAAGGTAC"
exon1 = gene_seq[0:16]
intron1 = gene_seq[16:34]
exon2 = gene_seq[34:58]
intron2 = gene_seq[58:72]
exon3 = gene_seq[72:]

print(len(gene_seq))
print('exon1: ' + exon1)
print('intron1: ' + intron1)
print('exon2: ' + exon2)
print('intron2: ' + intron2)
print('exon3: ' + exon3)
mature_mrna = exon1 + exon2 + exon3
print('mature_mrna: ' + mature_mrna)
print(len(exon1) + len(intron1)+len(exon2) + len(intron2) + len(exon3) == len(gene_seq))
print(exon1+intron1.lower()+exon2+intron2.lower()+exon3)



















