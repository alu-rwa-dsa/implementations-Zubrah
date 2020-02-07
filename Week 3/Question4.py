"""Space complexity
To  add, remove, modify and lookup will have O(1)  due to the fact that we are not storing and using any new space
while Time complexity since its a  dictionary, all  available methods will have O(1)"""


class Associative_list:
    def __init__(self):
        self.associate_list = {}

    def add(self, key, value):
        if hasattr(self, 'associative_list'):
            self.associate_list[key] = value
            return self.associate_list
        else:
            return 'Not initialized as required'

    def lookup(self, key):
        if hasattr(self, 'associative_list'):
            if key in self.associate_list.keys():
                return True
        else:
            return 'Not initialized as required'

    def remove(self, key):
        if hasattr(self, 'associative_list'):
            self.associate_list.pop(key)
            return self.associate_list
        else:
            return 'Not initialized as required'

    def modify(self, key, extravalue):
        if hasattr(self, 'associative_list'):
            self.associate_list[key] = extravalue
            return self.associate_list
        else:
            return 'Not initialized as required'
