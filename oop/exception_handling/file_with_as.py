with open('data.txt') as fin, open('result.txt', 'w') as fout:
    for line in fin:
        if 'class' in line:
            fout.write(line)


with open('data2.txt') as fin, open('result2.txt', 'r') as fout:
    for line in zip(fin, fout):
        print(line)

sep = '-' * 45 + '\n'

print(sep)

with open('data3.txt') as f1, open('result3.txt') as f2:
    for (linenum, (line1, line2)) in enumerate(zip(f1, f2)):
        if line1 != line2:
            print('%s:  %r != %r' % (linenum, line1, line2))
        else:
            print('%s:  %r == %r' % (linenum, line1, line2))

sep = '-' * 45 + '\n'
print(sep)

with open('data3.txt') as fin, open('result3.txt') as fout:
    for line in zip(fin, fout):
        print(line)


