import random
import string


class Robot:
    names = []

    def __init__(self):
        self.name = self.name_generator()
        self.names.append(self.name)

    def reset(self):
        new_name = self.name_generator()
        if new_name in self.names:
            new_name = self.name_generator()
        self.name = new_name
        self.names.append(new_name)

    @staticmethod
    def name_generator(letters=string.ascii_uppercase, digits=string.digits):
        chars = ''.join(random.choice(letters) for _ in range(2))
        digits = ''.join(random.choice(digits) for _ in range(3))
        return chars + digits
