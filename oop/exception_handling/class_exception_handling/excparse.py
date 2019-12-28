class FormatError(Exception):
    logfile = 'formaterror.txt'

    def __init__(self, line, file):
        self.line = line
        self.file = file

    def logerror(self):
        log = open(self.logfile, 'a')
        print('Error in {} at line {}'.format(self.file, self.line), file=log)


def parser():
    raise FormatError(40, 'scammer.txt')


if __name__ == '__main__':
    try:
        parser()
    except FormatError as exc:
        exc.logerror()


