#!/usr/bin/env python3

#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = None
        self.size = size
        self.condition = 'New'

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer\n", end="")
        else:
            self._size = value

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = 'New'

