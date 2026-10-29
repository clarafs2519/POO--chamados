

from chamado import Chamado

class SistemaChamados:
    def __init__(self):
        self.chamados = []
    

    #esse chamado tem aquelas propriedades de Chamado 
    def abrir_chamado(self, chamado):
        self.chamados.append(chamado)

    def listar_chamado(self):
        for chamado in self.chamados:
            print(f"Titúlo {chamado.titulo}")
            #{chamado.titulo} pegando titulo da classse Chamado
            print(f"Status {chamado.status}")

            if chamado.tecnico:
                print(f"Tecnico {chamado.tecnico.nome}")
            else:
                print("Tecnico nao encontrado") 
            print(f"Usuario {chamado.usuario.nome}")
            print("-"*30)