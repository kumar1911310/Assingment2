with open('rosalind_iev.txt') as f:
    couple = [int(i) for i in f.readline().strip().split()]
    probs = [1, 1, 1, 3/4, 1/2, 0]
    print(sum(2*[couple[i]*probs[i] for i in range(len(probs))]))