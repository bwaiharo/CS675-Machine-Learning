seqs = [
 'ATAGCTGATCGTAGCTACGTACGATCG',
 'CATCGTACATGC',
 'TATGTGT',
 'GCTGATCGTGACTGTAC',
 'ACTGT'
]

def get_length(seq):
    return len(seq)

# How about the second approach, where we write a function that explicitly tells Python which of two elements should go first? According to the docs, we need to write:

# " a custom comparison function of two arguments (iterable elements) which should return a negative, zero or positive number depending on whether the first argument is considered smaller than, equal to, or larger than the second argument. "

# The simplest way to do this is probably with a if/elif/else statement:


# def compare(seq1, seq2):
#     if len(seq1) == len(seq2):
#         return 0
#     elif len(seq1) > len(seq2):
#         return 1
#     else:
#         return -1


print(f'DNA comparison by lenght: {sorted(seqs, key = get_length)}')

# print(f'DNA comparison by order: {sorted(seqs, cmp=compare)}')