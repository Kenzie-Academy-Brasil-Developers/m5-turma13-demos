from heranca import Moradia, Apartamento, Casa
from heranca.exc import WrongDateFormat


def main():
    m1_data = {
        "alugado_em": "26/01/2023",
        "num_quartos": 3,
        "area": 72.1,
        "endereco": "Rua das Laranjas",
        "preco": 1599,
    }

    m1 = Moradia(**m1_data)
    print(m1)
    print()
    # print(m1.gerar_relatorio())

    m2 = Moradia(5, 32, "Rua das Macieiras", 2000, "15/09/2022")
    print(m2)
    print()
    # print(m2.gerar_relatorio())

    apt1_data = {
        "num_quartos": 5,
        "area": 50.1,
        "endereco": "Rua dos Astronautas",
        "preco": 2344,
        "preco_condominio": 800,
        "num_elevadores": 6,
        "alugado_em": "12/01/2023",
        "andar": 25,
    }

    apt1 = Apartamento(**apt1_data)
    print(apt1)
    # print(apt1.gerar_relatorio())
    print()

    c1_data = {
        "num_quartos": 5,
        "area": 230,
        "endereco": "Rua das Petalas",
        "preco": 4500,
        "alugado_em": "12/01/2023",
        "tam_jardim": 30,
    }
    c1 = Casa(**c1_data)
    print(c1)
    # print(c1.gerar_relatorio())
    print()

    c2_data = {
        "num_quartos": 15,
        "area": 2300,
        "endereco": "Rua 1",
        "preco": 4500,
        "alugado_em": "11/01/2023",
        "tam_jardim": 30,
    }
    c2 = Casa(**c2_data)
    print(c2)
    # print(c2.gerar_relatorio())
    print()

    apt2_data = {
        "num_quartos": 15,
        "area": 112.1,
        "endereco": "Rua dos Astronautas",
        "preco": 3344,
        "preco_condominio": 800,
        "num_elevadores": 6,
        "alugado_em": "12/01/2023",
        "andar": 25,
    }

    apt2 = Apartamento(**apt2_data)
    print(apt2)
    print()

    m3_data = {
        "alugado_em": "26-01-2023",
        "num_quartos": 3,
        "area": 72.1,
        "endereco": "Rua das Laranjas",
        "preco": 1599,
    }

    try:
        m3 = Moradia(**m3_data)
        print(m3)
        print()
    except WrongDateFormat as error:
        print(type(error))
        print(error)


if __name__ == "__main__":
    main()
