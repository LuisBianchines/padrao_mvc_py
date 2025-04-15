
import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from controller.pessoa import PessoaController
from models.pessoa import Pessoa


while True:
    decisao = int(input('Digite 1 para salvar e 2 para listar: '))
    if decisao == 1:
        nome = input('Nome: ')
        sobrenome = input('sobrenome: ')
        idade = input('idade: ')
        cpf = input('cpf: ')
        
        p1 = Pessoa(nome=nome, sobrenome=sobrenome, idade=idade, cpf=cpf)
        PessoaController.salvar_pessoa(p1)
        
    elif decisao == 2:
        for i in PessoaController.listar_pessoas():
            print(f'Nome: {i.nome}')
        
    