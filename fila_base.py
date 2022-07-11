class FilaBase:
    codigo: int = 0
    fila = []
    cliente_atendidos = []
    senha_atual: str = ""

    def reseta_fila(self) -> None:
        if self.codigo >= 200:
            self.codigo = 0
        else:
            self.codigo += 1
