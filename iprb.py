def problem(k, m, n):
    k, m, n = map(float, (k, m, n))
    p = [
        k * (k - 1),  # AA, AA pairs
        k * m,  # AA, Aa pairs
        k * n,  # AA, aa pairs
        m * k,  # Aa, AA pairs
        m * (m - 1) * 0.75, # Aa, Aa pairs
        m * n * 0.5, # Aa, aa pairs
        n * k,  # aa, AA pairs
        n * m * 0.5,  # aa, Aa pairs
        0,  # aa, aa pairs
    ]
    t = k + m + n
    return sum(p) / t / (t - 1)


if __name__ == '__main__':
    import doctest
    import os
    doctest.testmod()

    dataset = open(os.path.dirname(__file__) + "/rosalind_iprb.txt").read()
    k, m, n = map(float, dataset.strip().split())
 
    print(problem(k, m, n))
