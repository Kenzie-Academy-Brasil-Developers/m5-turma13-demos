from heranca import Moradia, Apartamento, Casa


def main():
    # Moradia 1
    m1 = Moradia(3, 72.1, "Rua das Laranjas", 1599)
    print(m1)
    print()

    # Moradia 2
    m2 = Moradia(5, 32, "Rua das Macieiras", 2000)
    print(m2)
    print()

    # Casa 1
    c1 = Casa(5, 230, "Rua das Petalas", 4500, 30)
    print(c1)
    print()

    # Apartamento 1
    apt1 = Apartamento(5, 50.1, "Rua dos Astros", 2344, 25)
    print(apt1)
    print()

    # Casa 2
    c2 = Casa(15, 2300, "Rua das Rosas", 4500, 30)
    print(c2)
    print()

    # Apartamento 2
    apt2 = Apartamento(15, 112.1, "Rua Plutao", 3344, 6)
    print(apt2)
    print()

    # Moradia 3
    m3 = Moradia(3, 72.1, "Rua Limoeiro", 1200)
    print(m3)
    print()


if __name__ == "__main__":
    main()
