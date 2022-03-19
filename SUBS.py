from os.path import dirname


def problem(dataset=None):

    if not dataset:
        dataset = open(dirname(__file__) + "/rosalind_subs.txt").read()
    s, t = dataset.strip().splitlines()
    acids = [(s[i:i + len(t)], i + 1) for i in range(0, len(s) - len(t) + 1, 1)]
    return [acid[1] for acid in acids if acid[0] == t]

if __name__ == '__main__':
    #print(''.join(map(str, problem())))
    print(' '.join(map(str, problem())))