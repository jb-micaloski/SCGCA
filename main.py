import os, sys

from ctypes import windll, c_int64
windll.user32.SetProcessDpiAwarenessContext(c_int64(-4))

from kivy.resources import resource_add_path, resource_find
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty,ObjectProperty
import pandas as pd
from funcoes_aspirante import *
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from datetime import datetime
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.config import Config
import sqlite3

class DadosPrincipais(BoxLayout):
    pass


class Consulta(BoxLayout):
    pass

class Consulta_Licenca(BoxLayout):
    pass


class MenuScreen(Screen):
    pass

class PbenScreen(Screen):
    chave_pesquisa = ObjectProperty(None)
    

class LicencaScreen(Screen):
    chave_pesquisa = ObjectProperty(None)
    
class RegistroLicencasScreen(Screen):
    pass

class ResumoLicencasScreen(Screen):
    pass

class ChavesScreen(Screen):
    pass

class RegistroChavesScreen(Screen):
    pass

class ParteAltaScreen(Screen):
    pass

class ResumoParteAltaScreen(Screen):
    pass

class ChefeDiaScreen(Screen):
    pass

class VerChefesDiaScreen(Screen):
    pass

class ControleGeral(App):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        Window.size = (1920,1080)
        Window.fullscreen = True

        self.pben = pd.read_excel('teste.ods', engine = 'odf', sheet_name= 'PBEN')

        self.aspirantes = cria_aspirantes(self.pben)

        self.licencas = pd.read_excel('teste.ods', engine = 'odf', sheet_name= 'Licenças')
        self.licencas['Última Alteração'] = self.licencas['Última Alteração'].astype('str')
        self.licencas['Número Interno'] = self.licencas['Número Interno'].astype('str')

        self.popup_content= Label(text='Salvando...',color = (0.18, 0.28, 0.40, 1), bold= True)
        self.popup_salvando_licenca = Popup(title ='Salvando',content = self.popup_content,
        size_hint=(None, None), size=(300, 300))

        self.organiza_controle_geral_licenca()
        self.organiza_primeiro_licenca()
        self.organiza_segundo_licenca()
        self.organiza_terceiro_licenca()
        self.organiza_quarto_licenca()

        self.chaves = pd.read_excel('teste.ods', engine = 'odf', sheet_name= 'Chaves')
        self.chaves['Última Alteração'] = self.chaves['Última Alteração'].astype('str')
        self.chaves['Anterior'] = self.chaves['Anterior'].astype('str')
        self.chaves['Atual'] = self.chaves['Atual'].astype('str')
        self.organiza_claviculario()

        self.partealta = pd.read_excel('teste.ods', engine = 'odf', sheet_name= 'ParteAlta')
        self.partealta['Última Alteração'] = self.partealta['Última Alteração'].astype('str')
        self.partealta['Número Interno'] = self.partealta['Número Interno'].astype('str')

        self.organiza_controle_geral_partealta()
        self.organiza_primeiro_partealta()
        self.organiza_segundo_partealta()
        self.organiza_terceiro_partealta()
        self.organiza_quarto_partealta()

        self.chefedia = pd.read_excel('teste.ods', engine = 'odf', sheet_name= 'ChefeDia')

    nome_guerra = StringProperty()
    numero_atual = StringProperty()

    #Alterar datas
    numero_interno_2022 = StringProperty()
    numero_interno_2021 = StringProperty()
    numero_interno_2020 = StringProperty()
    numero_interno_2019 = StringProperty()
    nome_completo = StringProperty()
    nascimento = StringProperty()
    telefone = StringProperty()
    celular = StringProperty()
    email = StringProperty()
    companhia = StringProperty()
    pelotao = StringProperty()
    camarote = StringProperty()
    quarto = StringProperty()
    nip = StringProperty()
    sangue = StringProperty()

    #Licenca
    situacao_atual_licenca = StringProperty()
    ultima_alteracao_licenca = StringProperty()
    texto_input_licenca = StringProperty()
    licenca_salvou = StringProperty('Sem alterações')
    #LicencaGeral
    abordo_licenca = StringProperty('0')
    baixado_licenca = StringProperty('0')
    crestricao_licenca = StringProperty('0')
    dispdomiciliar_licenca = StringProperty('0')
    hnmd_licenca = StringProperty('0')
    lts_licenca = StringProperty('0')
    licenciados_licenca = StringProperty('0')
    stgt_licenca = StringProperty('0')
    #LicencaPrimeiroAno
    abordo_licenca1 = StringProperty('0')
    baixado_licenca1 = StringProperty('0')
    crestricao_licenca1 = StringProperty('0')
    dispdomiciliar_licenca1 = StringProperty('0')
    hnmd_licenca1 = StringProperty('0')
    lts_licenca1 = StringProperty('0')
    licenciados_licenca1 = StringProperty('0')
    stgt_licenca1 = StringProperty('0')
    #LicencaSegundoAno
    abordo_licenca2 = StringProperty('0')
    baixado_licenca2 = StringProperty('0')
    crestricao_licenca2 = StringProperty('0')
    dispdomiciliar_licenca2 = StringProperty('0')
    hnmd_licenca2 = StringProperty('0')
    lts_licenca2 = StringProperty('0')
    licenciados_licenca2 = StringProperty('0')
    stgt_licenca2 = StringProperty('0')
    #LicencaTerceiroAno
    abordo_licenca3 = StringProperty('0')
    baixado_licenca3 = StringProperty('0')
    crestricao_licenca3 = StringProperty('0')
    dispdomiciliar_licenca3 = StringProperty('0')
    hnmd_licenca3 = StringProperty('0')
    lts_licenca3 = StringProperty('0')
    licenciados_licenca3 = StringProperty('0')
    stgt_licenca3 = StringProperty('0')
    #LicencaQuartoAno
    abordo_licenca4 = StringProperty('0')
    baixado_licenca4 = StringProperty('0')
    crestricao_licenca4 = StringProperty('0')
    dispdomiciliar_licenca4 = StringProperty('0')
    hnmd_licenca4 = StringProperty('0')
    lts_licenca4 = StringProperty('0')
    licenciados_licenca4 = StringProperty('0')
    stgt_licenca4 = StringProperty('0') 
    #Licencas Registro
    registro_licencas_texto = StringProperty()
    numero_input_registroLicenca = StringProperty()
    data_input_registroLicenca = StringProperty()
    horario_input_registroLicenca = StringProperty()
    #Licencas Resumo
    resumo1_licencas_texto = StringProperty()
    resumo2_licencas_texto = StringProperty()
    resumo3_licencas_texto = StringProperty()
    resumo4_licencas_texto = StringProperty()
    numero_input_resumoLicenca = StringProperty()
    data_input_resumoLicenca = StringProperty()
    horario_input_resumoLicenca = StringProperty()


    #Claviculário
    chaves_salvou = StringProperty('Sem alterações')
    chave_input = StringProperty()
    chave_atualmente_com = StringProperty()
    chave_anteriormente_com = StringProperty()
    chave_ultima_alteracao = StringProperty()
    chaves_claviculario = StringProperty()
    chaves_fora = StringProperty()
    #Claviculario Registro
    registro_chaves_texto = StringProperty()
    chave_input_registroChave = StringProperty()
    data_input_registroChave = StringProperty()
    horario_input_registroChave = StringProperty()


    #Parte Baixa
    partealta_salvou = StringProperty('Sem alterações')
    situacao_atual_partealta =  StringProperty()
    ultima_alteracao_partealta = StringProperty()
    partealta_input = StringProperty()
    #ParteBaixa1Ano
    partealta_partealta1 = StringProperty()
    tfm_partealta1 = StringProperty()
    saladeestado_partealta1 = StringProperty()
    enfermaria_partealta1 = StringProperty()
    banco_partealta1 = StringProperty()
    biblioteca_partealta1 = StringProperty()
    #ParteBaixa2Ano
    partealta_partealta2 = StringProperty()
    tfm_partealta2 = StringProperty()
    saladeestado_partealta2 = StringProperty()
    enfermaria_partealta2 = StringProperty()
    banco_partealta2 = StringProperty()
    biblioteca_partealta2 = StringProperty()
    #ParteBaixa3Ano
    partealta_partealta3 = StringProperty()
    tfm_partealta3 = StringProperty()
    saladeestado_partealta3 = StringProperty()
    enfermaria_partealta3 = StringProperty()
    banco_partealta3 = StringProperty()
    biblioteca_partealta3 = StringProperty()
    #ParteBaixa4Ano
    partealta_partealta4 = StringProperty()
    tfm_partealta4 = StringProperty()
    saladeestado_partealta4 = StringProperty()
    enfermaria_partealta4 = StringProperty()
    banco_partealta4 = StringProperty()
    biblioteca_partealta4 = StringProperty()
    #ParteBaixaGeral
    partealta_partealta = StringProperty()
    tfm_partealta = StringProperty()
    saladeestado_partealta = StringProperty()
    enfermaria_partealta = StringProperty()
    banco_partealta = StringProperty()
    biblioteca_partealta = StringProperty()
    #ParteAlta Registro
    registro_partealta_texto = StringProperty()
    numero_input_registroPartealta = StringProperty()
    data_input_registroPartealta = StringProperty()
    horario_input_registroPartealta = StringProperty()
    #ParteAlta Resumo
    resumo1_partealta_texto = StringProperty()
    resumo2_partealta_texto = StringProperty()
    resumo3_partealta_texto = StringProperty()
    resumo4_partealta_texto = StringProperty()
    numero_input_resumoParteAlta = StringProperty()
    data_input_resumoParteAlta = StringProperty()
    horario_input_resumoParteAlta = StringProperty()


    #Chefe do Dia
    chefedodia_registrando1 = StringProperty()
    chefedodia_registrando2 = StringProperty()
    numero_ajosca_cd = StringProperty()
    quarto_de_serviço_cd = StringProperty()
    numero_chefe_cd = StringProperty()
    companhia_cd = StringProperty()
    pelotao_cd = StringProperty()
    cintos_cd = StringProperty()
    computador_cd = StringProperty()
    mapamundi_cd = StringProperty()
    bandeira_cd = StringProperty()
    licenciados_cd = StringProperty()
    regressos_cd = StringProperty()

    def build(self):
        # Create the screen manager
        self.sm = ScreenManager()
        self.sm.add_widget(MenuScreen(name='menu'))
        self.sm.add_widget(PbenScreen(name='pben'))
        self.sm.add_widget(LicencaScreen(name='licenca'))
        self.sm.add_widget(RegistroLicencasScreen(name='registrolicencas'))
        self.sm.add_widget(ResumoLicencasScreen(name='resumolicencas'))
        self.sm.add_widget(ChavesScreen(name='chaves'))
        self.sm.add_widget(RegistroChavesScreen(name='registrochaves'))
        self.sm.add_widget(ParteAltaScreen(name='partealta'))
        self.sm.add_widget(ResumoParteAltaScreen(name='resumopartealta'))
        self.sm.add_widget(ChefeDiaScreen(name='chefedia'))
        self.sm.add_widget(VerChefesDiaScreen(name='verchefesdia'))

        self.dados_principais = DadosPrincipais()
        self.consulta_licenca = Consulta_Licenca()

        return self.sm
    
    def consulta_pben(self, chave_pesquisa):
        aspirante = busca_aspirante(self.aspirantes,chave_pesquisa)
        self.numero_atual = str(aspirante.numero_interno_atual)
        self.nome_guerra = str(aspirante.nome_guerra)
        #Alterar datas
        self.numero_interno_2022 = str(aspirante.numero_interno_2022)
        self.numero_interno_2021 = str(aspirante.numero_interno_2021)
        self.numero_interno_2020 = str(aspirante.numero_interno_2020)
        self.numero_interno_2019 = str(aspirante.numero_interno_2019)
        self.nascimento = str(aspirante.data_nascimento)
        self.celular = str(aspirante.celular)
        self.telefone = str(aspirante.telefone)
        self.email = str(aspirante.email)
        self.companhia = str(aspirante.companhia)
        self.pelotao = str(aspirante.pelotao)
        self.camarote = str(aspirante.alojamento)
        self.quarto = str(aspirante.quarto_habilitacao)
        self.nip = str(aspirante.nip)
        self.sangue = str(aspirante.sangue)
        self.nome_completo = str(aspirante.nome_completo)    

    BOTAO_PRESSIONADO = StringProperty('')

    def consultar_licenca(self, chave_pesquisa):
        self.consulta_pben(chave_pesquisa)
        
        info_licencas = busca_licenca(self.numero_atual, self.licencas)
        self.situacao_atual_licenca = info_licencas[0]
        self.ultima_alteracao_licenca = info_licencas[1]
        print("Botão pressionado: " + self.BOTAO_PRESSIONADO)

    def atualiza_licenca(self, button_text):
        #print("Botão pressionado: " + button_text)
        if button_text == "":
            pass
        else:
            try:
                index = self.licencas.query('`Número Interno` == @self.numero_atual').index.tolist()[0]
                if button_text == 'Regresso':
                    self.licencas['Situação'][index] = 'A bordo'
                else:
                    self.licencas['Situação'][index] = button_text
                self.licencas['Última Alteração'][index] = datetime.now().strftime('%d/%m/%Y %H:%M')
                self.licenca_salvou = 'Alterações pendentes'
            except:
                self.numero_atual = 'Selecione um aspirante'
                self.nome_guerra = ''

        info_licencas = busca_licenca(self.numero_atual, self.licencas)
        self.situacao_atual_licenca = info_licencas[0]
        self.ultima_alteracao_licenca = info_licencas[1]

        self.registro_licencas()
        self.organiza_controle_geral_licenca()
        self.organiza_primeiro_licenca()
        self.organiza_segundo_licenca()
        self.organiza_terceiro_licenca()
        self.organiza_quarto_licenca()
    
    def salvar_alteracoes(self):

        writer = pd.ExcelWriter('teste.ods', engine='odf')
        self.licencas.to_excel(writer, sheet_name ='Licenças' ,encoding='utf-8', engine='odf', index=False, )
        self.pben.to_excel(writer, sheet_name ='PBEN' ,encoding='utf-8', engine='odf', index=False)
        self.chaves.to_excel(writer, sheet_name ='Chaves' ,encoding='utf-8', engine='odf', index=False)
        self.partealta.to_excel(writer, sheet_name ='ParteAlta' ,encoding='utf-8', engine='odf', index=False)
        self.chefedia.to_excel(writer, sheet_name ='ChefeDia' ,encoding='utf-8', engine='odf', index=False)
        writer.save()

        self.licencas = pd.read_excel('teste.ods', engine = 'odf', sheet_name= 'Licenças')
        self.chaves = pd.read_excel('teste.ods', engine = 'odf', sheet_name= 'Chaves')
        self.partealta = pd.read_excel('teste.ods', engine = 'odf', sheet_name= 'ParteAlta')
        self.chefedia = pd.read_excel('teste.ods', engine = 'odf', sheet_name= 'ChefeDia')

        self.licencas['Última Alteração'] = self.licencas['Última Alteração'].astype('str')
        self.licencas['Número Interno'] = self.licencas['Número Interno'].astype('str')
        self.partealta['Última Alteração'] = self.partealta['Última Alteração'].astype('str')
        self.partealta['Número Interno'] = self.partealta['Número Interno'].astype('str')

        self.chaves_salvou = 'Sem alterações'
        self.licenca_salvou = 'Sem alterações'
        self.partealta_salvou = 'Sem alterações'

        self.registra_salvou()
        self.popup_salvando_licenca.dismiss()

    def organiza_controle_geral_licenca(self):
        dicionario_licencas_geral = dict(self.licencas['Situação'].value_counts())
        try:
            self.abordo_licenca = str(dicionario_licencas_geral['A bordo'])
        except:
            self.abordo_licenca = '0'
        try:
            self.baixado_licenca = str(dicionario_licencas_geral['Baixado'])
        except:
            self.baixado_licenca = '0'
        try:
            self.crestricao_licenca = str(dicionario_licencas_geral['C/ Restrição'])
        except:
            self.crestricao_licenca = '0'
        try:
            self.dispdomiciliar_licenca = str(dicionario_licencas_geral['Disp. Domiciliar'])
        except:
            self.dispdomiciliar_licenca = '0'
        try:
            self.hnmd_licenca = str(dicionario_licencas_geral['HNMD'])
        except:
            self.hnmd_licenca = '0'
        try:
            self.lts_licenca = str(dicionario_licencas_geral['LTS'])
        except:
            self.lts_licenca = '0'
        try:
            self.licenciados_licenca = str(dicionario_licencas_geral['Licença'])
        except:
            self.licenciados_licenca = '0'
        try:
            self.stgt_licenca = str(dicionario_licencas_geral['ST/GT'])
        except:
            self.stgt_licenca = '0'

    def organiza_primeiro_licenca(self):
        query = self.licencas.query('`Ano` == 1')
        dicionario_primeiro_licenca = dict(query['Situação'].value_counts())
        try:
            self.abordo_licenca1 = str(dicionario_primeiro_licenca['A bordo'])
        except:
            self.abordo_licenca1 = '0'
        try:
            self.baixado_licenca1 = str(dicionario_primeiro_licenca['Baixado'])
        except:
            self.baixado_licenca1 = '0'
        try:
            self.crestricao_licenca1 = str(dicionario_primeiro_licenca['C/ Restrição'])
        except:
            self.crestricao_licenca1 = '0'
        try:
            self.dispdomiciliar_licenca1 = str(dicionario_primeiro_licenca['Disp. Domiciliar'])
        except:
            self.dispdomiciliar_licenca1 = '0'
        try:
            self.hnmd_licenca1 = str(dicionario_primeiro_licenca['HNMD'])
        except:
            self.hnmd_licenca1 = '0'
        try:
            self.lts_licenca1 = str(dicionario_primeiro_licenca['LTS'])
        except:
            self.lts_licenca1 = '0'
        try:
            self.licenciados_licenca1 = str(dicionario_primeiro_licenca['Licença'])
        except:
            self.licenciados_licenca1 = '0'
        try:
            self.stgt_licenca1 = str(dicionario_primeiro_licenca['ST/GT'])
        except:
            self.stgt_licenca1 = '0'
    
    def organiza_segundo_licenca(self):
        query = self.licencas.query('`Ano` == 2')
        dicionario_segundo_licenca = dict(query['Situação'].value_counts())
        try:
            self.abordo_licenca2 = str(dicionario_segundo_licenca['A bordo'])
        except:
            self.abordo_licenca2 = '0'
        try:
            self.baixado_licenca2 = str(dicionario_segundo_licenca['Baixado'])
        except:
            self.baixado_licenca2 = '0'
        try:
            self.crestricao_licenca2 = str(dicionario_segundo_licenca['C/ Restrição'])
        except:
            self.crestricao_licenca2 = '0'
        try:
            self.dispdomiciliar_licenca2 = str(dicionario_segundo_licenca['Disp. Domiciliar'])
        except:
            self.dispdomiciliar_licenca2 = '0'
        try:
            self.hnmd_licenca2 = str(dicionario_segundo_licenca['HNMD'])
        except:
            self.hnmd_licenca2 = '0'
        try:
            self.lts_licenca2 = str(dicionario_segundo_licenca['LTS'])
        except:
            self.lts_licenca2 = '0'
        try:
            self.licenciados_licenca2 = str(dicionario_segundo_licenca['Licença'])
        except:
            self.licenciados_licenca2 = '0'
        try:
            self.stgt_licenca2 = str(dicionario_segundo_licenca['ST/GT'])
        except:
            self.stgt_licenca2 = '0'
        
    def organiza_terceiro_licenca(self):
        query = self.licencas.query('`Ano` == 3')
        dicionario_terceiro_licenca = dict(query['Situação'].value_counts())
        try:
            self.abordo_licenca3 = str(dicionario_terceiro_licenca['A bordo'])
        except:
            self.abordo_licenca3 = '0'
        try:
            self.baixado_licenca3 = str(dicionario_terceiro_licenca['Baixado'])
        except:
            self.baixado_licenca3 = '0'
        try:
            self.crestricao_licenca3 = str(dicionario_terceiro_licenca['C/ Restrição'])
        except:
            self.crestricao_licenca3 = '0'
        try:
            self.dispdomiciliar_licenca3 = str(dicionario_terceiro_licenca['Disp. Domiciliar'])
        except:
            self.dispdomiciliar_licenca3 = '0'
        try:
            self.hnmd_licenca3 = str(dicionario_terceiro_licenca['HNMD'])
        except:
            self.hnmd_licenca3 = '0'
        try:
            self.lts_licenca3 = str(dicionario_terceiro_licenca['LTS'])
        except:
            self.lts_licenca3 = '0'
        try:
            self.licenciados_licenca3 = str(dicionario_terceiro_licenca['Licença'])
        except:
            self.licenciados_licenca3 = '0'
        try:
            self.stgt_licenca3 = str(dicionario_terceiro_licenca['ST/GT'])
        except:
            self.stgt_licenca3 = '0'

    def organiza_quarto_licenca(self):
        query = self.licencas.query('`Ano` == 4')
        dicionario_quarto_licenca = dict(query['Situação'].value_counts())
        try:
            self.abordo_licenca4 = str(dicionario_quarto_licenca['A bordo'])
        except:
            self.abordo_licenca4 = '0'
        try:
            self.baixado_licenca4 = str(dicionario_quarto_licenca['Baixado'])
        except:
            self.baixado_licenca4 = '0'
        try:
            self.crestricao_licenca4 = str(dicionario_quarto_licenca['C/ Restrição'])
        except:
            self.crestricao_licenca4 = '0'
        try:
            self.dispdomiciliar_licenca4 = str(dicionario_quarto_licenca['Disp. Domiciliar'])
        except:
            self.dispdomiciliar_licenca4 = '0'
        try:
            self.hnmd_licenca4 = str(dicionario_quarto_licenca['HNMD'])
        except:
            self.hnmd_licenca4 = '0'
        try:
            self.lts_licenca4 = str(dicionario_quarto_licenca['LTS'])
        except:
            self.lts_licenca4 = '0'
        try:
            self.licenciados_licenca4 = str(dicionario_quarto_licenca['Licença'])
        except:
            self.licenciados_licenca4 = '0'
        try:
            self.stgt_licenca4 = str(dicionario_quarto_licenca['ST/GT'])
        except:
            self.stgt_licenca4 = '0'

    def input_texto_chave(self,textbox):
        self.chave_input = textbox.text
        info_chaves = busca_chave(self.chave_input,self.chaves)
        self.chave_input = info_chaves[0]
        self.chave_atualmente_com = info_chaves[2]
        self.chave_anteriormente_com = info_chaves[1]
        self.chave_ultima_alteracao = info_chaves[3]
    
    def dar_chave(self,textbox):
        try:
            index = self.chaves.query('`Numero da Chave` == @self.chave_input').index.tolist()[0]

            self.chaves['Anterior'][index] = self.chaves['Atual'][index]
            self.chaves['Atual'][index] = textbox.text
            self.chaves['Última Alteração'][index] = datetime.now().strftime('%d/%m/%Y %H:%M')

            busca_chave(self.chave_input,self.chaves)
            self.chaves_salvou = 'Alterações pendentes'

            info_chaves = busca_chave(self.chave_input,self.chaves)
            self.chave_input = info_chaves[0]
            self.chave_atualmente_com = info_chaves[2]
            self.chave_anteriormente_com = info_chaves[1]
            self.chave_ultima_alteracao = info_chaves[3]
        except:
            self.chave_input = 'Chave não encontrada'
            self.chave_atualmente_com = 'Chave não encontrada'
            self.chave_anteriormente_com = 'Chave não encontrada'
            self.chave_ultima_alteracao = 'Chave não encontrada'
        
        self.registro_chave()
        self.organiza_claviculario()

    def retorna_chave(self):
        try:
            index = self.chaves.query('`Numero da Chave` == @self.chave_input').index.tolist()[0]

            self.chaves['Anterior'][index] = self.chaves['Atual'][index]
            self.chaves['Atual'][index] = 'Claviculário'
            self.chaves['Última Alteração'][index] = datetime.now().strftime('%d/%m/%Y %H:%M')

            busca_chave(self.chave_input,self.chaves)
            self.chaves_salvou = 'Alterações pendentes'

            info_chaves = busca_chave(self.chave_input,self.chaves)
            self.chave_input = info_chaves[0]
            self.chave_atualmente_com = info_chaves[2]
            self.chave_anteriormente_com = info_chaves[1]
            self.chave_ultima_alteracao = info_chaves[3]
        except:
            self.chave_input = 'Chave não encontrada'
            self.chave_atualmente_com = 'Chave não encontrada'
            self.chave_anteriormente_com = 'Chave não encontrada'
            self.chave_ultima_alteracao = 'Chave não encontrada'
        
        self.registro_chave()
        self.organiza_claviculario()

    def organiza_claviculario(self):
        dicionario = dict(self.chaves.Atual.value_counts())
        self.chaves_claviculario = str(dicionario['Claviculário'])
        self.chaves_fora = str(len(self.chaves.Atual) - dicionario['Claviculário'])

    def consultar_partealta(self,chave_pesquisa):
        self.consulta_pben(chave_pesquisa)
        
        info_partealta = busca_licenca(self.numero_atual, self.partealta)
        self.situacao_atual_partealta = info_partealta[0]
        self.ultima_alteracao_partealta = info_partealta[1]

    botao_parte_alta = StringProperty('')

    def atualiza_partealta(self, button_text):
        if button_text == '':
            pass
        else:
            try:
                index = self.partealta.query('`Número Interno` == @self.numero_atual').index.tolist()[0]
                self.partealta['Situação'][index] = button_text
                self.partealta['Última Alteração'][index] = datetime.now().strftime('%d/%m/%Y %H:%M')
                self.partealta_salvou = 'Alterações pendentes'
            except:
                self.numero_atual = 'Selecione um aspirante'
                self.nome_guerra = ''

        info_partealta = busca_licenca(self.numero_atual, self.partealta)
        self.situacao_atual_partealta = info_partealta[0]
        self.ultima_alteracao_partealta = info_partealta[1]

        self.organiza_controle_geral_partealta()
        self.organiza_primeiro_partealta()
        self.organiza_segundo_partealta()
        self.organiza_terceiro_partealta()
        self.organiza_quarto_partealta()

    def organiza_controle_geral_partealta(self):
        dicionario_partealta_geral = dict(self.partealta['Situação'].value_counts())

        try:
            self.partealta_partelta = str(dicionario_partealta_geral['Parte Alta'])
        except:
            self.partealta_partelta = '0'
        try:
            self.tfm_partealta = str(dicionario_partealta_geral['TFM'])
        except:
            self.tfm_partealta = '0'
        try:
            self.saladeestado_partealta = str(dicionario_partealta_geral['Sala de Estado'])
        except:
            self.saladeestado_partealta = '0'
        try:
            self.enfermaria_partealta = str(dicionario_partealta_geral['Enfermaria'])
        except:
            self.enfermaria_partealta = '0'
        try:
            self.banco_partealta = str(dicionario_partealta_geral['Banco'])
        except:
            self.banco_partealta = '0'
        try:
            self.biblioteca_partealta = str(dicionario_partealta_geral['Biblioteca'])
        except:
            self.biblioteca_partealta = '0'

    def organiza_primeiro_partealta(self):
        query = self.partealta.query('`Ano` == 1')
        dicionario_primeiro_partealta = dict(query['Situação'].value_counts())
        try:
            self.partealta_partelta1 = str(dicionario_primeiro_partealta['Parte Alta'])
        except:
            self.partealta_partelta1 = '0'
        try:
            self.tfm_partealta1 = str(dicionario_primeiro_partealta['TFM'])
        except:
            self.tfm_partealta1 = '0'
        try:
            self.saladeestado_partealta1 = str(dicionario_primeiro_partealta['Sala de Estado'])
        except:
            self.saladeestado_partealta1 = '0'
        try:
            self.enfermaria_partealta1 = str(dicionario_primeiro_partealta['Enfermaria'])
        except:
            self.enfermaria_partealta1 = '0'
        try:
            self.banco_partealta1 = str(dicionario_primeiro_partealta['Banco'])
        except:
            self.banco_partealta1 = '0'
        try:
            self.biblioteca_partealta1 = str(dicionario_primeiro_partealta['Biblioteca'])
        except:
            self.biblioteca_partealta1 = '0'

    def organiza_segundo_partealta(self):
        query = self.partealta.query('`Ano` == 2')
        dicionario_segundo_partealta = dict(query['Situação'].value_counts())
        try:
            self.partealta_partelta2 = str(dicionario_segundo_partealta['Parte Alta'])
        except:
            self.partealta_partelta2 = '0'
        try:
            self.tfm_partealta2 = str(dicionario_segundo_partealta['TFM'])
        except:
            self.tfm_partealta2 = '0'
        try:
            self.saladeestado_partealta2 = str(dicionario_segundo_partealta['Sala de Estado'])
        except:
            self.saladeestado_partealta2 = '0'
        try:
            self.enfermaria_partealta2 = str(dicionario_segundo_partealta['Enfermaria'])
        except:
            self.enfermaria_partealta2 = '0'
        try:
            self.banco_partealta2 = str(dicionario_segundo_partealta['Banco'])
        except:
            self.banco_partealta2 = '0'
        try:
            self.biblioteca_partealta2 = str(dicionario_segundo_partealta['Biblioteca'])
        except:
            self.biblioteca_partealta2 = '0'

    def organiza_terceiro_partealta(self):
        query = self.partealta.query('`Ano` == 3')
        dicionario_terceiro_partealta = dict(query['Situação'].value_counts())
        try:
            self.partealta_partelta3 = str(dicionario_terceiro_partealta['Parte Alta'])
        except:
            self.partealta_partelta3 = '0'
        try:
            self.tfm_partealta3 = str(dicionario_terceiro_partealta['TFM'])
        except:
            self.tfm_partealta3 = '0'
        try:
            self.saladeestado_partealta3 = str(dicionario_terceiro_partealta['Sala de Estado'])
        except:
            self.saladeestado_partealta3 = '0'
        try:
            self.enfermaria_partealta3 = str(dicionario_terceiro_partealta['Enfermaria'])
        except:
            self.enfermaria_partealta3 = '0'
        try:
            self.banco_partealta3 = str(dicionario_terceiro_partealta['Banco'])
        except:
            self.banco_partealta3 = '0'
        try:
            self.biblioteca_partealta3 = str(dicionario_terceiro_partealta['Biblioteca'])
        except:
            self.biblioteca_partealta3 = '0'

    def organiza_quarto_partealta(self):
        query = self.partealta.query('`Ano` == 4')
        dicionario_quarto_partealta = dict(query['Situação'].value_counts())
        try:
            self.partealta_partelta4 = str(dicionario_quarto_partealta['Parte Alta'])
        except:
            self.partealta_partelta4 = '0'
        try:
            self.tfm_partealta4 = str(dicionario_quarto_partealta['TFM'])
        except:
            self.tfm_partealta4 = '0'
        try:
            self.saladeestado_partealta4 = str(dicionario_quarto_partealta['Sala de Estado'])
        except:
            self.saladeestado_partealta4 = '0'
        try:
            self.enfermaria_partealta4 = str(dicionario_quarto_partealta['Enfermaria'])
        except:
            self.enfermaria_partealta4 = '0'
        try:
            self.banco_partealta4 = str(dicionario_quarto_partealta['Banco'])
        except:
            self.banco_partealta4 = '0'
        try:
            self.biblioteca_partealta4 = str(dicionario_quarto_partealta['Biblioteca'])
        except:
            self.biblioteca_partealta4 = '0'

    def atualiza_chefedodia_registrando(self):
        self.chefedodia_registrando1 = (
        f'AjOSCA: {self.numero_ajosca_cd} | Quarto de Serviço: {self.quarto_de_serviço_cd} | Chefe de dia: {self.numero_chefe_cd} | '
        )+(
        f'Cia.: {self.companhia_cd} | Pelotão: {self.pelotao_cd} | '
        )

        self.chefedodia_registrando2 = (
        f'Computador/Alarme: {self.computador_cd} | Mapa-Mundi: {self.mapamundi_cd} | Bandeira Asp. Nasc.: {self.bandeira_cd} | ' 
        )+(
        f'Cintos: {self.cintos_cd} | Licenciados: {self.licenciados_cd} | Regressos: {self.regressos_cd}')

    def att_numero_ajosca_cd(self,textinput):
        self.numero_ajosca_cd = textinput.text
        self.atualiza_chefedodia_registrando()
    
    def att_quarto_de_serviço_cd(self,textinput):
        self.quarto_de_serviço_cd = textinput.text
        self.atualiza_chefedodia_registrando()

    def att_numero_chefe_cd(self,textinput):
        self.numero_chefe_cd = textinput.text

        aspirante = busca_aspirante(self.aspirantes,self.numero_chefe_cd)

        self.numero_chefe_cd = str(aspirante.numero_interno_atual)
        self.pelotao_cd = aspirante.pelotao
        self.companhia_cd = aspirante.companhia

        self.atualiza_chefedodia_registrando()

    def att_cintos_cd(self,textinput):
        self.cintos_cd = textinput.text
        self.atualiza_chefedodia_registrando()

    def att_regressos_cd(self,textinput):
        self.regressos_cd = textinput.text
        self.atualiza_chefedodia_registrando()
    
    def att_licenciados_cd(self,textinput):
        self.licenciados_cd = textinput.text
        self.atualiza_chefedodia_registrando()

    def att_computador_cd(self,textinput):
        self.computador_cd = textinput.text
        self.atualiza_chefedodia_registrando()

    def att_mapamundi_cd(self,textinput):
        self.mapamundi_cd = textinput.text
        self.atualiza_chefedodia_registrando()

    def att_bandeira_cd(self,textinput):
        self.bandeira_cd = textinput.text
        self.atualiza_chefedodia_registrando()

    def registra_chefe_dia(self):
        agora = datetime.now().strftime('%d/%m/%Y %H:%M')
        self.chefedia.loc[self.chefedia.index.max() + 1] = [agora,self.numero_ajosca_cd, self.numero_chefe_cd,self.quarto_de_serviço_cd,
        self.companhia_cd,self.pelotao_cd, self.cintos_cd, self.bandeira_cd, self.licenciados_cd, self.regressos_cd,
        self.computador_cd, self.mapamundi_cd]

        self.salvar_alteracoes()
        self.popup_salvando_licenca.dismiss()

    def registro_chave(self):
        registro_chave = open("log_chave.txt", "a", encoding='utf-8')
        registro_chave.write(f"Chave: {self.chave_input}, Atualmente com: {self.chave_atualmente_com}, Anteriormente com: {self.chave_anteriormente_com}, Última alteração: {self.chave_ultima_alteracao}\n")
        registro_chave.close()

    def atualiza_registro_chaves(self, chave="", data="", horario=""):
        with open("log_chave.txt", "r", encoding='utf-8') as registro_chave:
            linhas = registro_chave.readlines()
            resultado = ""
            for linha in linhas:
                if 'Salvou' in linha:
                    resultado += linha
                else:
                    if chave and f"Chave: {chave}," not in linha:
                        continue
                    if data:
                        try:
                            data_linha = datetime.strptime(linha.split(", Última alteração: ")[-1].strip(), "%d/%m/%Y %H:%M")
                            data_argumento = datetime.strptime(data, "%d/%m/%Y")
                            if data_argumento != data_linha.replace(hour=0, minute=0, second=0, microsecond=0):
                                continue
                        except ValueError:
                            continue
                    if horario:
                        try:
                            horario_linha = datetime.strptime(linha.split(", Última alteração: ")[-1].strip(), "%d/%m/%Y %H:%M")
                            if horario != horario_linha.strftime("%H:%M"):
                                continue
                        except ValueError:
                            continue
                resultado += linha
            self.registro_chaves_texto = resultado

    def atualiza_registro_licencas(self, numero="", data="", horario=""):
        with open("log_licencas.txt", "r", encoding='utf-8') as registro_licencas:
            linhas = registro_licencas.readlines()
            resultado = ""
            for linha in linhas:
                if 'Salvou' in linha:
                    resultado += linha
                else:
                    if numero and f"Número interno: {numero}," not in linha:
                        continue
                    if data:
                        try:
                            data_linha = datetime.strptime(linha.split(", Última alteração: ")[-1].strip(), "%d/%m/%Y %H:%M")
                            data_argumento = datetime.strptime(data, "%d/%m/%Y")
                            if data_argumento != data_linha.replace(hour=0, minute=0, second=0, microsecond=0):
                                continue
                        except ValueError:
                            continue
                    if horario:
                        try:
                            horario_linha = datetime.strptime(linha.split(", Última alteração: ")[-1].strip(), "%d/%m/%Y %H:%M")
                            if horario != horario_linha.strftime("%H:%M"):
                                continue
                        except ValueError:
                            continue
                    resultado += linha
            self.registro_licencas_texto = resultado

    def atualiza_registro_partealta(self, numero="", data="", horario=""):
        with open("log_partealta.txt", "r", encoding='utf-8') as registro_partealta:
            linhas = registro_partealta.readlines()
            resultado = ""
            for linha in linhas:
                if 'Salvou' in linha:
                    resultado += linha
                else:
                    if numero and f"Número interno: {numero}," not in linha:
                        continue
                    if data:
                        try:
                            data_linha = datetime.strptime(linha.split(", Última alteração: ")[-1].strip(), "%d/%m/%Y %H:%M")
                            data_argumento = datetime.strptime(data, "%d/%m/%Y")
                            if data_argumento != data_linha.replace(hour=0, minute=0, second=0, microsecond=0):
                                continue
                        except ValueError:
                            continue
                    if horario:
                        try:
                            horario_linha = datetime.strptime(linha.split(", Última alteração: ")[-1].strip(), "%d/%m/%Y %H:%M")
                            if horario != horario_linha.strftime("%H:%M"):
                                continue
                        except ValueError:
                            continue
                    resultado += linha
            self.registro_partealta_texto = resultado
  
    def atualiza_resumo_licencas(self):
        resultado1 = ""
        resultado2 = ""
        resultado3 = ""
        resultado4 = ""

        conn = sqlite3.connect('dados.db')
        cursor = conn.cursor()
        
        cursor.execute('SELECT NumeroInt,Situacao FROM dados_lic WHERE Ano = 1')
        resultado1 = cursor.fetchall()

        cursor.execute('SELECT NumeroInt,Situacao FROM dados_lic WHERE Ano = 2')
        resultado2 = cursor.fetchall()

        cursor.execute('SELECT NumeroInt,Situacao FROM dados_lic WHERE Ano = 3')
        resultado3 = cursor.fetchall()

        cursor.execute('SELECT NumeroInt,Situacao FROM dados_lic WHERE Ano = 4')
        resultado4 = cursor.fetchall()

        df1 = pd.DataFrame(resultado1, columns=['Número Interno','Situação'])
        df2 = pd.DataFrame(resultado2, columns=['Número Interno','Situação'])
        df3 = pd.DataFrame(resultado3, columns=['Número Interno','Situação'])
        df4 = pd.DataFrame(resultado4, columns=['Número Interno','Situação'])

        self.resumo1_licencas_texto = df1.to_string(index=False)
        self.resumo2_licencas_texto = df2.to_string(index=False)
        self.resumo3_licencas_texto = df3.to_string(index=False)
        self.resumo4_licencas_texto = df4.to_string(index=False)

    def atualiza_resumo_partealta(self):
        resultado1 = ""
        resultado2 = ""
        resultado3 = ""
        resultado4 = ""

        conn = sqlite3.connect('dados.db')
        cursor = conn.cursor()
        
        cursor.execute('SELECT NumeroInt,Situacao FROM dados_partealta WHERE Ano = 1')
        resultado1 = cursor.fetchall()

        cursor.execute('SELECT NumeroInt,Situacao FROM dados_partealta WHERE Ano = 2')
        resultado2 = cursor.fetchall()

        cursor.execute('SELECT NumeroInt,Situacao FROM dados_partealta WHERE Ano = 3')
        resultado3 = cursor.fetchall()

        cursor.execute('SELECT NumeroInt,Situacao FROM dados_partealta WHERE Ano = 4')
        resultado4 = cursor.fetchall()

        df1 = pd.DataFrame(resultado1, columns=['Número Interno','Situação'])
        df2 = pd.DataFrame(resultado2, columns=['Número Interno','Situação'])
        df3 = pd.DataFrame(resultado3, columns=['Número Interno','Situação'])
        df4 = pd.DataFrame(resultado4, columns=['Número Interno','Situação'])

        self.resumo1_partealta_texto = df1.to_string(index=False)
        self.resumo2_partealta_texto = df2.to_string(index=False)
        self.resumo3_partealta_texto = df3.to_string(index=False)
        self.resumo4_partealta_texto = df4.to_string(index=False)

    def registro_licencas(self):
        registro_licencas = open("log_licencas.txt", "a", encoding='utf-8')
        registro_licencas.write(f"Número interno: {self.numero_atual}, Situação atual: {self.situacao_atual_licenca}, Última alteração: {self.ultima_alteracao_licenca}\n")
        registro_licencas.close()

        conn = sqlite3.connect('dados.db')
        cursor = conn.cursor()

        numero_int = self.numero_atual
        nova_situacao = self.situacao_atual_partealta
        consulta_sql = 'UPDATE dados SET Situacao = ? WHERE NumeroInt = ?'
        cursor.execute(consulta_sql, (nova_situacao, numero_int))

        conn.commit()
        conn.close()

    def registro_partealta(self):

        conn = sqlite3.connect('dados.db')
        cursor = conn.cursor()

        numero_int = self.numero_atual
        nova_situacao = self.situacao_atual_licenca
        consulta_sql = 'UPDATE dados_partealta SET Situacao = ? WHERE NumeroInt = ?'
        cursor.execute(consulta_sql, (nova_situacao, numero_int))

        conn.commit()
        conn.close()

    def registra_salvou(self):
        agora = datetime.now().strftime('%d/%m/%Y %H:%M')
        texto = f'Alterações Salvas em: {agora}\n'
        registro_chave = open("log_licencas.txt", "a", encoding='utf-8')
        registro_chave.write(texto)
        registro_chave.close()
        registro_chave = open("log_chave.txt", "a", encoding='utf-8')
        registro_chave.write(texto)
        registro_chave.close()
    
if __name__ == '__main__':
    ControleGeral().run()
