class SkipObject:

    def __init__(self, wrapped):
        self.wrapped = wrapped

    def __iter__(self):
        offset = 0
        while offset < len(self.wrapped):
            item = self.wrapped[offset]
            offset += 2
            yield item


skipper = SkipObject('abcdef')

i = iter(skipper)

print(next(i))
print(next(i))
print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))


