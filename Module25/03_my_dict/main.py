class MyDict(dict):

    def __init__(self, data):
        super().__init__()
        self.__data = data

    def get_value(self, key):
        if key in self.__data:
            return self.__data[key]
        else:
            return 0


some_data = {1: 'number 1', 2: 'number 2', 3: 'number 3', 4: 'number 4'}
mydict = MyDict(some_data)
value_1 = mydict.get_value(1)
value_2 = mydict.get_value(6)

print(value_1)
print(value_2)
