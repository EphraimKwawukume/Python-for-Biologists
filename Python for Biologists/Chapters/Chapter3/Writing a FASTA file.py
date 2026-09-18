my_file = open('sequenceseli.fasta','w')
header1 = "ABC123"
header2 = "DEF456"
header3 = "HIJ789"
sequence1 = 'ATCGTACGATCGATCGATCGCTAGACGTATCG'
sequence2 = 'actgatcgacgatcgatcgatcacgact'
sequence3 = 'ACTGAC-ACTGT--ACTGTA----CATGTG'

my_file.write(">" + header1 + '\n' + sequence1) 
my_file.write("\n>" + header2 + '\n' + sequence2.upper()) 
my_file.write("\n>" + header3 + "\n" + sequence3.replace('-',''))
my_file.close()

#Writing multiple fasta files
my_file = open(header1 + '.fasta','w')
my_file.write(">" + header1 + '\n' + sequence1) 

my_file = open(header2 + '.fasta','w')
my_file.write(">" + header2 + '\n' + sequence2.upper())

my_file = open(header3 + '.fasta','w')
my_file.write(">" + header3 + '\n' + sequence3.replace('-',''))
