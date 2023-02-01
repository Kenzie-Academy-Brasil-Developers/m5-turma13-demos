from datetime import datetime as dt
from .exc import WrongDateFormat


class Moradia:
    # print("CLASSE MORADIA INICIALIZADA")
    id_count = 0

    def __init__(
        self,
        num_quartos: int,
        area: float,
        endereco: str,
        preco: float,
        alugado_em: str,
    ):
        self.id = self.gerar_novo_id()
        self.num_quartos = num_quartos
        self.area = area
        self.endereco = endereco
        self.preco = preco
        self.alugado_em = self.valida_alugado_em_formato(alugado_em)

    def valida_alugado_em_formato(self, data_para_validar: str):
        try:
            dt.strptime(data_para_validar, "%d/%m/%Y")
        except ValueError:
            raise WrongDateFormat("formato de data errado")

        return data_para_validar

    @staticmethod
    def gerar_novo_id():
        Moradia.id_count += 1

        return Moradia.id_count

    def gerar_relatorio(self) -> str:
        # \n -> pular linha

        log = "Relatório:" + "\n"
        log += f"Endereço: {self.endereco}" + "\n"
        log += f"Numero de quartos: {self.num_quartos}" + "\n"
        log += f"Area: {self.area}m2" + "\n"
        log += f"Preco: R$ {self.preco}" + "\n"

        return log

    # SOBRESCRITA
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
        alugado_em: str,
        andar: int,
        preco_condominio: float,
        num_elevadores: int,
    ):
        super().__init__(num_quartos, area, endereco, preco, alugado_em)
        self.andar = andar
        self.preco_condominio = preco_condominio
        self.num_elevadores = num_elevadores

    def gerar_relatorio(self) -> str:
        log = super().gerar_relatorio()
        log += f"Andar: {self.andar}" + "\n"
        log += f"Condominio: {self.preco_condominio}" + "\n"
        log += f"Elevadores: {self.num_elevadores}" + "\n"

        return log

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
        alugado_em: str,
        tam_jardim: float,
    ):
        super().__init__(num_quartos, area, endereco, preco, alugado_em)
        self.tam_jadim = tam_jardim

    def gerar_relatorio(self) -> str:
        log = super().gerar_relatorio()
        log += f"Tam Jardim: {self.tam_jadim}" + "\n"

        return log

    def __repr__(self) -> str:
        return f"<[{self.id}] Casa {self.endereco} {self.tam_jadim}>"
