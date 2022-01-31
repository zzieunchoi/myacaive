class Person:
    def __init__(self, age):
        self.__age = age
    @property
    def age(self):
        return self.__age

    @age.setter # @변경하고싶은변수.setter
    def age(self, new_age):
        if new_age < 0:
            raise TypeError('invalid range')
        print(new_age)
        self.__age = new_age

p1 = Person(10)
p1.age = -100