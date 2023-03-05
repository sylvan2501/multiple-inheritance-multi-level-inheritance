class BaseClass:
    def __init__(self, property_a, property_b):
        self.property_a = property_a
        self.property_b = property_b

    def __str__(self):
        return f'The BaseClass has two properties: {self.property_a} and {self.property_b}'

    def __repr__(self):
        return f'BaseClass(\'{self.property_a}\', \'{self.property_b}\')'

    def identify(self):
        print('This is a Base class')


class AnotherBaseClass:
    def __init__(self, property_d, property_e):
        self.property_d = property_d
        self.property_e = property_e

    def __str__(self):
        return f'The AnotherBaseClass has two properties: {self.property_d} and {self.property_e}'

    def __repr__(self):
        return f'AnotherBaseClass(\'{self.property_d}\', \'{self.property_e}\')'

    def identify(self):
        print('This is Another Base class.')


class DerivedClass(BaseClass):
    def __init__(self, property_a, property_b, property_c):
        super().__init__(property_a, property_b)
        self.property_c = property_c

    def __str__(self):
        return f'The Derived class has two properties: {self.property_a} , {self.property_b} and {self.property_c}'

    def __repr__(self):
        return f'DerivedClass(\'{self.property_a}\', \'{self.property_b}\', \'{self.property_c}\')'

    def identify(self):
        print('This is a Derived class')


# Multiple inheritance -- MRO (method resolution order)
class AnotherDerivedClass(BaseClass, AnotherBaseClass):
    def __init__(self, property_a, property_b, property_d, property_e, property_f):
        BaseClass.__init__(self, property_a, property_b)
        AnotherBaseClass.__init__(self, property_d, property_e)
        self.property_f = property_f

    def __str__(self):
        return f'The Another Derived class has a property: {self.property_a},' \
               f'{self.property_b}, ' \
               f'{self.property_d}, ' \
               f'{self.property_e}, ' \
               f'{self.property_f}'

    def __repr__(self):
        return f'AnotherDerivedClass(\'{self.property_a}\', ' \
               f'\'{self.property_b}\', ' \
               f'\'{self.property_d}\', ' \
               f'\'{self.property_e}\', ' \
               f'\'{self.property_f}\')'

    # def identify(self):
    #     print('This is another derived class')


# Multi-level Inheritance
class DerivedClassFromDerivedClass(DerivedClass):
    def __init__(self, property_a, property_b, property_c, property_g):
        super().__init__(property_a, property_b, property_c)
        self.property_g = property_g

    def identify(self):
        print('This is a derived class from derived class')


# It seems that Python has implicit type casting
# derived_class = DerivedClass('a', 'b', 'c')
#
# base_class = BaseClass('a', 'b')
# base_class = DerivedClass('c', 'd', 'e')
# base_class.identify()
# print(isinstance(base_class, BaseClass))
# print(isinstance(base_class, DerivedClass))
# base_class = BaseClass('m', 'n')
# base_class.identify()

ad = AnotherDerivedClass('a', 'b', 'd', 'e', 'f')
ad.identify()
