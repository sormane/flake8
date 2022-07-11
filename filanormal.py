from fila_base import FilaBase

class filanormal(FilaBase):

    def gerasenhaatual(self)->None: #isso significa que não retorna nada
        self.senhatual = f'NM{self.codigo}'

    def atualizafila(self)->None:
        self.resetafila()
        self.gerasenhaatual()
        self.fila.append(self.senhatual)

    def chamacliente(self, caixa:int)->str:
        cliente_atual:str = self.fila.pop(0)
        self.clientesatendidos.append(cliente_atual)
        return(f'Cliente atual: {cliente_atual}, dirija-se ao caixa: {caixa}')