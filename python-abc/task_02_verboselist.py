#!/usr/bin/python3
class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f'Added [{item}] to the list.')

    def extend(self, iterable, count=0):
        super().extend(iterable)
        for i in iterable:
            count += 1
        print(f'Extented the list with [{count}] items')

    def remove(self, value):
        super().remove(value)
        print(f'Removed [{value}] from the list.')

    def pop(self, index=-1):
        item = self[index]
        super().pop(index)
        print(f'Popped[{item}] from th list')
