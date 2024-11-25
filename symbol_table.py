
class tabela_de_simbolos:
    def __init__(self):
        self.tabela = []
        
    def install_id(self, id):
        if len(self.tabela) == 0:
            self.tabela.append({'id': id, 'tipo': None, 'valor': None})
            return
        else:
            for el in self.tabela:
                if el['id'] == id:
                    return
            self.tabela.append({'id': id, 'tipo': None, 'valor': None})
            return
    def install_type(self, id, tipo):
        for el in self.tabela:
            if el['id'] == id:
                el['tipo'] = tipo
                return
        return 'ID não encontrado'
    
    def install_value(self, id, valor):
        for el in self.tabela:
            if el['id'] == id:
                el['valor'] = valor
                return
        return 'ID não encontrado'

    def get_tabela(self):
        return self.tabela