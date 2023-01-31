class Moradia:
    id_count = 0

    def __init__(
        self,
        num_quartos: int,
        area: float,
        endereco: str,
        preco: float,
    ):
        self.id = self.gerar_novo_id()
        self.num_quartos = num_quartos
        self.area = area
        self.endereco = endereco
        self.preco = preco

    @staticmethod
    def gerar_novo_id():
        """
        Se quero inicializar um id unico compartilhado para qualquer instancia
        que herde de moradia
        (Só preciso ter o atributo de classe id_count em Moradia)
        """
        # print(f"NOME DA CLASSE {cls.__name__}")
        # print(f"PRÉ ID _> {cls.id_count}")
        # cls.id_count += 1
        # cls.id_count = cls.id_count + 1
        Moradia.id_count += 1
        # print(f"PÓS ID _> {cls.id_count}")

        return Moradia.id_count

    # @classmethod
    # def gerar_novo_id(cls):
    #     """
    #     Se quero inicializar um id unico para cada classe distinta
    #     (Obrigatório ter o atributo de classe id_count em TODAS as filhas)
    #     """
    #     cls.id_count += 1

    #     return cls.id_count

    def __repr__(self) -> str:
        return f"<[{self.id}] Moradia {self.endereco} {self.preco}>"


class Apartamento(Moradia):
    # id_count = 0

    def __init__(
        self,
        num_quartos: int,
        area: float,
        endereco: str,
        preco: float,
        andar: int,
    ):
        super().__init__(num_quartos, area, endereco, preco)
        self.andar = andar

    def __repr__(self) -> str:
        return f"<[{self.id}] Apartamento {self.endereco} {self.andar}>"


class Casa(Moradia):
    # id_count = 0

    def __init__(
        self,
        num_quartos: int,
        area: float,
        endereco: str,
        preco: float,
        tam_jardim: float,
    ):
        super().__init__(num_quartos, area, endereco, preco)
        self.tam_jadim = tam_jardim

    def __repr__(self) -> str:
        return f"<[{self.id}] Casa {self.endereco} {self.tam_jadim}>"
