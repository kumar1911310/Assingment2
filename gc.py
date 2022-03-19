def GCcontent(seq):
    return(seq.count('G') + seq.count('C'))/len(seq)

sseq={}
mid=None
mgc=0
with open('rosalind_gc.txt', 'r') as f:
    sid = None
    seq = None
    while True:
        ff=f.readline().strip()
        if not ff:
            sseq[sid]=GCcontent(seq)
            if sseq[sid] > mgc:
                mid = sid
                mgc = sseq[sid]
            break
        else:
            if ff.startswith('>'):
                if sid is not None:
                    sseq[sid]=GCcontent(seq)
                    if sseq[sid] > mgc:
                        mid = sid
                        mgc = sseq[sid]
                sid = ff[1:]
                seq = ''
            else:
                seq += ff

print(mid,f'{sseq[mid]*100}',sep = '\n')