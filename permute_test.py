def permute1(seq):
    if not seq:  # Shuffle any sequence
        return [seq]  # Empty Sequence
    else:
        res = []
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]  # Delete current node
            for x in permute1(rest):  # Permute the others
                res.append(seq[i:i+1] + x)  # Add node at front
        return res


def permute2(seq):
    if not seq:
        yield seq
    else:
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]
            for x in permute2(rest):
                yield seq[i:i+1] + x


print(permute1('abc'))


x = list(map(pow, [1, 2, 3, 4], [5, 6, 7, 8]))

print(x)

