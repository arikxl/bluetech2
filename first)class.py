class Animal:
    names =['ogry', 'loola']

    def add_name(self, name):
        self.names.append(name)
        return self.names

the_animal = Animal()
the_animal.add_name('Yehonatan')
print(the_animal.names)
