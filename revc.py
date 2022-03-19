
s='AAAACCCGGT'
d={'A':'T', 'T':'A', 'G':'C', 'C':'G'}
for i in reversed(s): 
    print(d[i], end='')

print('\n')

# Solution 2
s='AAAACCCGGT'
d={'A':'T', 'T':'A', 'G':'C', 'C':'G'}
sc=[]
for i in reversed(s): 
    sc.append(d[i])

print(''.join(sc))

# Solution 3
with open('rosalind_revc.txt', 'r') as f:
    s=f.readline().strip()
    print(s.replace('A','t').replace('T','a').replace('G','c').replace('C','g').upper()[::-1])