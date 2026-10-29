

from usuario import Usuario
from tecnico import Tecnico
from chamado import Chamado
from sistema_chamado import SistemaChamados

def main():
    usuario_um = Usuario("Ana", "ana@email.com")
    usuario_dois = Usuario("Joao", "ajoao@email.com")
    tecnico_um = Tecnico("valdemir")

    chamado_um = Chamado("PC não liga", "Tela azul", "Alta", usuario_um) 
    chamado_dois = Chamado("login", "problema senha", "Alta", usuario_dois) 





    sistema = SistemaChamados()
    sistema.abrir_chamado(chamado_um)
    sistema.abrir_chamado(chamado_dois)
  

    chamado_um.atribuir_tecnico(tecnico_um)
    chamado_dois.atribuir_tecnico(tecnico_um)


    chamado_um.fechar_chamado()

    sistema.listar_chamado()


if __name__ == "__main__":
    main()