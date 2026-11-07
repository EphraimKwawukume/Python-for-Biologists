counts = {}
trinucleotide = []
for base1 in ['A', 'T', 'G', 'C']:
    for base2 in ['A', 'T', 'G', 'C']:
        for base3 in ['A', 'T', 'G', 'C']:
            tri = base1 + base2 + base3
            trinucleotide.append(tri)
            count = trinucleotide.count(tri)
            counts[tri] = count
print(counts)
print(trinucleotide)
