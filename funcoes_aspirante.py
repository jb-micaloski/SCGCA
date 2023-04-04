import pandas as pd
from aspirante import Aspirante
import re

aspirante_nulo = Aspirante()

aspirante_nulo.numero_interno_atual = 'XXXX'
aspirante_nulo.nome_guerra = 'Nome não encontrado'
aspirante_nulo.pelotao = 'NA'
aspirante_nulo.companhia = 'NA'

def cria_aspirantes(pben):
    aspirantes = []
    '''
    Adiciona no array aspirante todos os aspirantes como objetos, assim como suas propriedades
    '''
    for i in range(len(pben)):
        aspirante = Aspirante()

        aspirante.numero_interno_atual = pben['NúmeroInternoAtual'][i]
        #Alterar datas
        aspirante.numero_interno_2022 = pben['NúmeroInterno2022'][i]
        aspirante.numero_interno_2021 = pben['NúmeroInterno2021'][i]
        aspirante.numero_interno_2020 = pben['NúmeroInterno2020'][i]
        aspirante.numero_interno_2019 = pben['NúmeroInterno2019'][i]
        aspirante.nome_guerra = pben['NomedeGuerra'][i]
        aspirante.nome_completo = pben['NomeCompleto'][i]
        aspirante.companhia = pben['Companhia'][i]
        aspirante.pelotao = pben['Pelotão'][i]
        aspirante.alojamento = pben['Alojamento/Camarote'][i]
        aspirante.nip = pben['N.I.P.'][i]
        aspirante.id_militar = pben['NúmerodaID.Militar'][i]
        aspirante.quarto_habilitacao = pben['Quarto/Habilitação'][i]
        aspirante.telefone = pben['TelefonedeContato'][i]
        aspirante.celular = pben['CelulardeContato'][i]
        aspirante.data_nascimento = pben['DatadeNascimento'][i]
        aspirante.sangue = pben['TipoSanguíneo+FatorRH'][i]
        aspirante.equipe = pben['Equipe'][i]
        aspirante.email = pben['E-mail'][i]
        aspirante.religiao = pben['Religião'][i]
        aspirante.cidade = pben['Cidade'][i]
        aspirante.estado = pben['Estado'][i]
        aspirante.bairro = pben['Bairro'][i]
        aspirante.endereco = pben['Endereço'][i]
        aspirante.cep = pben['CEP'][i]
        aspirante.nome_pai = pben['NomedoPai'][i]
        aspirante.profissao_pai = pben['ProfissãodoPai'][i]
        aspirante.forca_militar_pai = pben['CasooPaiSejaMilitar-ForçaArmada/ForçaAuxiliar'][i]
        aspirante.cargo_militar_pai = pben['CasooPaiSejaMilitar-PostoouGraduação'][i]
        aspirante.nome_mae = pben['NomedaMãe'][i]
        aspirante.profissao_mae = pben['ProfissãodaMãe'][i]
        aspirante.forca_militar_mae = pben['CasoaMãeSejaMilitar-ForçaArmada/ForçaAuxiliar'][i]
        aspirante.cargo_militar_mae = pben['CasoaMãeSejaMilitar-PostoouGraduação'][i]
        aspirante.adicional = pben['Descrição'][i]

        aspirantes.append(aspirante)
    
    return aspirantes

def busca_aspirante(aspirantes, valor_buscado):
    '''Retorna o objeto do aspirante desejado'''
    padrao_numero = '([0-9]{4})'
    padrao_im = '(IM[0-9]{3})'
    padrao_fn = '(FN[0-9]{3})'
    valor_buscado = valor_buscado.upper()

    '''
    Verifica se o valor buscado bate com uma RE de número de aspirante
    Se não bater, considera que é o nome de um aspirante
    '''
    if re.search(padrao_numero,valor_buscado) or re.search(padrao_im,valor_buscado) or re.search(padrao_fn,valor_buscado):
        for aspirante in aspirantes:
            if str(aspirante.numero_interno_atual) == str(valor_buscado):
                return aspirante
        return aspirante_nulo
    else: 
        for aspirante in aspirantes:
            if aspirante.nome_guerra == str(valor_buscado).upper():
                return aspirante
        return aspirante_nulo

