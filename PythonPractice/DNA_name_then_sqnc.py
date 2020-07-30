seqs = [
 'CAT',
 'ATAGCTGATCGTAGCTACGTACGATCG',
 'DOG',
 'CATCGTACATGC',
 'ELEPHANT',
 'TATGTGT',
 'RAT',
 'GCTGATCGTGACTGTAC',
 'MOUSE',
 'ACTGT'
]

name_seqs = list(seqs[::2]) #copied
dna_seqs = list(seqs[::-2]) #copied
dna_seqs =dna_seqs[::-1] #revesed

dna_dict = dict(zip(name_seqs,dna_seqs))

dna_num = list()

for k,v in dna_dict.items():
    dna_num.append(len(v))

max_lnght = max(dna_num)
lngst = name_seqs[dna_num.index(max_lnght)]

print(f"Name:\t{lngst}\nSequence:\t{dna_dict[lngst]}\nLength:\t{max_lnght}")

