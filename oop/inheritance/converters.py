from oop.inheritance.file_streams import Processor


class UpperCase(Processor):
    def converter(self, data):
        return data.upper()


if __name__ == '__main__':
    import sys
    obj = UpperCase(open('trispam.txt'), sys.stdout)
    obj.process()


