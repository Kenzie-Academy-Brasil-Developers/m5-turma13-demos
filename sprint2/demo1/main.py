from persons import Person


def class_attr():
    # objeto -> instancia de uma classe
    # new NomeDaClasse()
    p1 = Person()
    p2 = Person()
    p3 = Person()

    # print(id(p1))
    # print(hex(id(p1)))
    # print(p1)
    # print(p2)
    # print(p3)
    # print()

    # Atributo Imútavel (int)
    p1.life_expectancy = 1000
    print(p1.life_expectancy)
    print(p2.life_expectancy)
    print(p3.life_expectancy)
    print()

    # Atributo mútavel (list)
    p1.wishlist.append('Poltrona Gamer RGB')
    print(p1.wishlist)
    print(p2.wishlist)
    print(p3.wishlist)


def intance_attr():
    p1 = Person("person1", "111")
    p2 = Person("person2", "222")
    p3 = Person("person3", "333")

    p1.append('Cavaquinho')
    print(p1.instruments)
    print(p2.instruments)
    print(p3.instruments)
    print()


def dunder_methods():
    p1 = Person("person1", "111")
    p2 = Person("person2", "222")
    p3 = Person("person3", "333")

    # print(p1)
    # print(p2)
    # print(p3)
    # print()

    # print(p1.__repr__())
    # print(p2.__repr__())
    # print(p3.__repr__())
    # print()

    # print(type(p1))
    # print(p1)
    print()
    # print(type(p1.__dict__))
    # print(p1.__dict__)
    # print(vars(p1))

    # print(dir(p1))
    # print(len([1, 2]))
    # print(len(p1))
    # p1.instruments.append('Cavaquinho')
    # print(len(p1))
    # print(p1.__len__())
    print(p1)


def methods():
    p1 = Person("person1", "111")
    p2 = Person("person2", "222")
    p3 = Person("person3", "333")

    # Metodo de instancia
    print('Adição de usuarios:')
    print(p1.save_person())
    print(p2.save_person())
    # print(p3.save_person())
    print(p1.save_person())
    # print(Person.save_person())
    # print(p1.persons_list)
    # print(Person.persons_list)
    # Incomum
    # print(Person.save_person(p1))
    print()

    # print(p1.name)

    # Métodos de classes
    # p1.delete_person()
    print('Deleção:')
    print(Person.persons_list)
    print(Person.delete_person('999'))
    print(Person.delete_person('111'))
    print(Person.persons_list)


def main():
    # class_attr()
    # intance_attr()
    # dunder_methods()
    methods()


if __name__ == '__main__':
    main()
