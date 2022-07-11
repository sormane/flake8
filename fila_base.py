import abc

from constantes import TAMANHO_PADRAO_MAXIMO, TAMANHO_PADRAO_MINIMO

class FilaBase(metaclass=abc.ABCMeta): #classe abstrada
    codigo: int = 0
    fila = []
    cliente_atendidos = []
    senha_atual: str = ""

    def reseta_fila(self) -> None:
        if self.codigo >= TAMANHO_PADRAO_MAXIMO:
            self.codigo = TAMANHO_PADRAO_MINIMO
        else:
            self.codigo += 1

    def insere_cliente(self):
        self.fila.append(self.senha_atual)

    @abc.abstractmethod #esses metodo só obriga as classes filhar executarem esse metodo (classe abstrada)
    def gera_senha_atual(self):
        ...

    def atualiza_fila(self):
        self.reseta_fila()
        self.gera_senha_atual()
        self.insere_cliente()

    @abc.abstractmethod
    def chama_cliente(self, caixa: int):
        ...