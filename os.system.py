import os

x = os.system('systeminfo')


# print(x)

# for line in os.popen('systeminfo'):
#     print(line.rstrip())

# for i, line in enumerate(os.popen('systeminfo')):
#     if i == 4:
#         break
#     print('{:05} {:}'.format(i, line.rstrip()))


# for line in os.popen('systeminfo'):
#     parts = line.split(':')
#     if parts and parts[0].lower() == 'system type':
#         print(parts[1].strip())

# try:
#     for val in [line.split()[6] for line in open('datafile_2.txt')]:
#         print(val)
# except FileNotFoundError:
#     print('File does not exists...')
#
# col7 = []
# for line in open('datafile_2.txt'):
#     cols = line.split()
#     col7.append(cols[6])
#
# for item in col7:
#     print(item)

try:
    def awker(file, col):
        return [line.rstrip().split()[col - 1] for line in open(file)]

except FileNotFoundError:
    print('File not found...')

else:
    print(awker('datafile_2.txt', 7))
    print(','.join(awker('datafile_2.txt', 7)))


# print(awker('datafile_2.txt', 7))






