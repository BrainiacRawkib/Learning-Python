def myzip(*seq):
    seq = [list(s) for s in seq]
    res = []
    while all(seq):
        res.append(tuple(s.pop(0) for s in seq))
    return res


def mymappad(*seqs, pad=None):
    seqs = [list(s) for s in seqs]
    res = []
    while any(seqs):
        res.append(tuple((s.pop(0) if s else pad) for s in seqs))
    return res


def myzip2(*seq):
    minlen = min(len(s) for s in seq)
    print(minlen)
    return [tuple(s[i] for s in seq) for i in range(minlen)]


def mymappad2(*seqs, pad=None):
    maxlen = max(len(s) for s in seqs)
    index = range(maxlen)
    return [tuple((s[i] if len(s) > i else pad) for s in seqs) for i in index]


S1, S2 = 'abc', 'xyz123'
print(myzip2(S1, S2))
print(mymappad2(S1, S2))




