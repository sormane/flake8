from fila_base import FilaBase
from constantes import CODIGO_PRIORITARIO

from typing import Dict, Union, List


class FilaPrioritaria(FilaBase):

    def gera_senha_atual(self) -> None:
        self.senha_atual = f'{CODIGO_PRIORITARIO}{self.codigo}'

    def chama_cliente(self, caixa: int) -> None:
        display = []
        cliente_atual = self.fila.pop(0)
        display.append(f'Cliente: ]{cliente_atual} - Caixa {caixa}')

        if len(self.fila) >= 3:
            display.append(f'Próximo: {self.fila[0]}')
            display.append(f'Fique atento: {self.fila[1]}')

        self.cliente_atendidos.append(cliente_atual)

        return display

    def estatistica(self, dia: str, agencia: int, retorna_estatistica) -> dict:
        estatistica = retorna_estatistica(dia, agencia)

        return estatistica.roda_estatistica(self.cliente_atendidos)