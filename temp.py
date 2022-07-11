def estatistica(self, dia: str, agencia: int, flag: str) -> dict:
    estatistica: Dict[str, Union[List[str], str, int]] = {}
    if flag != 'detail':
        estatistica[f'{agencia} - {dia}'] = len(self.cliente_atendidos)
    else:
        estatistica['dia'] = dia
        estatistica['agencia'] = agencia
        estatistica['clientes atendidos'] = self.cliente_atendidos
        estatistica['quantidade clientes atendidos'] = (
            len(self.cliente_atendidos)
        )  # Colocou dentro dos parenteses para diminuir a linha

    return estatistica