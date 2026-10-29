from usuario import Usuario
from tecnico import Tecnico

class Chamado :
    def __init__(self, titulo, descricao, prioridade, usuario ):
        self.titulo =  titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.usuario = usuario
        self.status = "Aberto"
        self.tecnico = None


    def atribuir_tecnico(self, tecnico):
        self.tecnico = tecnico
        self.status = "Em atendimento"

    def fechar_chamado(self):
        self.status = "Fechado"