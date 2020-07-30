import sys
dnasqnc = sys.argv[1]

complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'} 

def reverseCompliment(dnasqnc):
    s =''
    for i in dnasqnc.upper():
        if (i in complement):
            s+=complement[i]
        else:
            return "Not Valid DNA sequence"
    return  f"Original:\t{dnasqnc}\nReverse Compliment:\t{s}"  


rc = reverseCompliment(dnasqnc)

print(rc)