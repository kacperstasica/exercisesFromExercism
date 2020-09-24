import string

class PhoneNumber:
    def __init__(self, number):
        self.number = ''.join(i for i in number if i.isdigit())
        self.area_code = self.number[:3]

        if len(self.number) > 11 or len(self.number) <= 9:
            raise ValueError('Invalid phone number.')

        if len(self.number) == 10:
            if self.number[0] == '1' or self.number[0] == '0':
                raise ValueError('Area code invalid.')
            elif self.number[3] == '0' or self.number[3] == '1':
                raise ValueError('Exchange Code invalid.')

        if len(self.number) == 11:
            if self.number[1] == '0' or self.number[1] == '1':
                raise ValueError('Full number area code invalid.')
            elif self.number[4] == '0' or self.number[4] == '1':
                raise ValueError('Full number exchange code invalid.')
            elif self.number[0] != '1':
                raise ValueError('Full number invalid.')
            self.number = self.number[1:]


    def pretty(self):
        return  f"({self.number[:3]})-{self.number[3:6]}-{self.number[6:10]}"
