# class Person(object) -> python 2

# PascalCase
class Person:
    # Atributo de classe
    life_expectancy = 90
    wishlist = ["Faca Ginzu 2000"]
    persons_list = []

    # Inicializador de atributos de instancia
    # self -> this
    # __new__ -> construtor
    # É um método
    # Método de instancia
    # Método mágico (dunder method)
    def __init__(self, name: str, cpf: str) -> None:
        self.name = name
        self.cpf = cpf
        self.instruments = ["Violão"]

    # Método de instancia, classe, estático
    def save_person(self):
        # for person in self.persons_list:
        #     # print(type(person))
        #     if person.cpf == self.cpf:
        #         return 'CPF já cadastrado!!'

        person_found = self.retrieve_person(self.cpf)

        # Truty or Falsy values
        if person_found:
            return 'CPF já cadastrado!!'

        self.persons_list.append(self)

        return "Cadastro feito com sucesso!!"

    @classmethod
    def delete_person(cls, person_cpf: str):
        # for person in cls.persons_list:
        #     if person.cpf == person_cpf:
        #         cls.persons_list.remove(person)
        #         return 'Pessoa removida!'

        person_found = cls.retrieve_person(person_cpf)

        # Truty or Falsy values
        if not person_found:
            return 'Pessoa não encontrada!'

        cls.persons_list.remove(person_found)

        return 'Pessoa removida!'

    @classmethod
    def retrieve_person(cls, person_cpf: str):
        for person in cls.persons_list:
            if person.cpf == person_cpf:
                return person

    # Sobrescrita
    def __repr__(self) -> str:
        # return 'Olá __repr__ de Person'
        return f'<{self.cpf} - {self.name}>'
        # return self.__dict__

    def __len__(self) -> int:
        return len(self.instruments)
        # return 'olá __len__'
