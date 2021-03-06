import pybench, sys


pythons = [
    (1, 'C:\\Users\Brainiac Rawkib\AppData\Local\Programs\Python\Python36\python'),
    (0, 'C:\\Users\Brainiac Rawkib\AppData\Local\Programs\Python\Python36-32\python'),
    (0, 'C:\Python27\python')
]

stmts = [  # (num,rpt,stmt)
    (0, 0, "[x ** 2 for x in range(1000)]"),  # Iterations
    (0, 0, "res=[]\nfor x in range(1000): res.append(x ** 2)"),  # \n=multistmt
    (0, 0, "$listif3(map(lambda x: x ** 2, range(1000)))"),  # \n\t=indent
    (0, 0, "list(x ** 2 for x in range(1000))"),  # $=list or ''
    (0, 0, "s = 'spam' * 2500\nx = [s[i] for i in range(10000)]"),  # String ops
    (0, 0, "s = '?'\nfor i in range(10000): s += '?'"),
]

tracecmd = '-t' in sys.argv
pythons = pythons if '-a' in sys.argv else None
pybench.runner(stmts, pythons, tracecmd)
