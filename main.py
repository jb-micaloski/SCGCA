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
    chave_pesquisa = ObjectProperty(None)
    chave_pesquisa2 = ObjectProperty(None)

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

        conn = sqlite3.connect('dados.db')
        cursor = conn.cursor()
        
        cursor.execute('SELECT NumeroInt, Situacao FROM dados_lic')
        licencas_num_sit = cursor.fetchall()

        self.licencas = pd.DataFrame(licencas_num_sit, columns=['Número Interno','Situação'])

        self.popup_content= Label(text='Salvando...',color = (0.18, 0.28, 0.40, 1), bold= True)
        self.popup_salvando_licenca = Popup(title ='Salvando',content = self.popup_content,
        size_hint=(None, None), size=(300, 300))

        self.popup_content2= Label(text='O Número/Nome não foi encontrado! Tente novamente',color = (0.18, 0.28, 0.40, 1), bold= True)
        self.popup_verica_numero = Popup(title ='Erro!',content = self.popup_content2,
        size_hint=(None, None), size=(300, 300))

        self.organiza_controle_geral_licenca()
        self.organiza_primeiro_licenca()
        self.organiza_segundo_licenca()
        self.organiza_terceiro_licenca()
        self.organiza_quarto_licenca()
        
        conn = sqlite3.connect('dados.db')
        cursor = conn.cursor()
        
        cursor.execute('SELECT NumerodaChave,Anterior, Atual FROM dados_chave')
        chaves_num_sit = cursor.fetchall()

        self.licencas = pd.DataFrame(chaves_num_sit, columns=['Número da Chave','Situação Anterior','Situação Atual'])

        self.organiza_claviculario()

        conn = sqlite3.connect('dados.db')
        cursor = conn.cursor()
        
        cursor.execute('SELECT NumeroInt, Situacao FROM dados_partealta')
        partealta_num_sit = cursor.fetchall()

        self.partealta = pd.DataFrame(partealta_num_sit, columns=['Número Interno','Situação'])

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

        conn = sqlite3.connect('dados.db')
        cursor = conn.cursor()

        numero_int = str(self.numero_atual)

        cursor.execute('SELECT Situacao, UltimaAlt FROM dados_lic WHERE NumeroInt = ?', (numero_int,))

        info_licencas = cursor.fetchone()

        self.situacao_atual_licenca = str(info_licencas[0])
        self.ultima_alteracao_licenca = str(info_licencas[1])

        conn.commit()
        conn.close()

    def atualiza_licenca(self, button_text):
        if button_text == "":
            pass
        else:
            try:
                conn = sqlite3.connect('dados.db')
                cursor = conn.cursor()

                numero_int = self.numero_atual
                nova_sit = str(self.BOTAO_PRESSIONADO)
                nova_ultimaalt = datetime.now().strftime('%d/%m/%Y %H:%M')
                consulta_sql = 'UPDATE dados_lic SET Situacao = ?, UltimaAlt = ? WHERE NumeroInt = ?'
                cursor.execute(consulta_sql, (nova_sit, nova_ultimaalt, numero_int))
                conn.commit()

            except:
                self.numero_atual = 'Selecione um aspirante'
                self.nome_guerra = ''
        
        cursor.execute("SELECT Situacao, UltimaAlt FROM dados_lic WHERE NumeroInt = ?", (numero_int,))
        info_licencas = cursor.fetchone()
        self.situacao_atual_licenca = str(info_licencas[0])
        self.ultima_alteracao_licenca = str(info_licencas[1])

        conn.commit()
        conn.close()

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

        conn = sqlite3.connect('dados.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_lic WHERE Situacao = 'A bordo'")
        result = cursor.fetchone()
        self.abordo_licenca = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_lic WHERE Situacao = 'Baixado'")
        result = cursor.fetchone()
        self.baixado_licenca = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_lic WHERE Situacao = 'C/ Restrição'")
        result = cursor.fetchone()
        self.crestricao_licenca = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_lic WHERE Situacao = 'Disp. Domiciliar'")
        result = cursor.fetchone()
        self.dispdomiciliar_licenca = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_lic WHERE Situacao = 'LTS'")
        result = cursor.fetchone()
        self.lts_licenca = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_lic WHERE Situacao = 'HNMD'")
        result = cursor.fetchone()
        self.hnmd_licenca = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_lic WHERE Situacao = 'Licença'")
        result = cursor.fetchone()
        self.licenciados_licenca = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_lic WHERE Situacao = 'ST/GT'")
        result = cursor.fetchone()
        self.stgt_licenca = str(result[0])

        conn.commit()
        conn.close()

    def organiza_primeiro_licenca(self):
        conn = sqlite3.connect('dados.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_lic WHERE Situacao = 'A bordo' AND Ano = 1")
        result = cursor.fetchone()
        self.abordo_licenca1 = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_lic WHERE Situacao = 'Baixado' AND Ano = 1")
        result = cursor.fetchone()
        self.baixado_licenca1 = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_lic WHERE Situacao = 'C/ Restrição' AND Ano = 1")
        result = cursor.fetchone()
        self.crestricao_licenca1 = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_lic WHERE Situacao = 'Disp. Domiciliar' AND Ano = 1")
        result = cursor.fetchone()
        self.dispdomiciliar_licenca1 = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_lic WHERE Situacao = 'LTS' AND Ano = 1")
        result = cursor.fetchone()
        self.lts_licenca1 = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_lic WHERE Situacao = 'HNMD' AND Ano = 1")
        result = cursor.fetchone()
        self.hnmd_licenca1 = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_lic WHERE Situacao = 'Licença' AND Ano = 1")
        result = cursor.fetchone()
        self.licenciados_licenca1 = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_lic WHERE Situacao = 'ST/GT' AND Ano = 1")
        result = cursor.fetchone()
        self.stgt_licenca1 = str(result[0])

        conn.commit()
        conn.close()
          
    def organiza_segundo_licenca(self):
        conn = sqlite3.connect('dados.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_lic WHERE Situacao = 'A bordo' AND Ano = 2")
        result = cursor.fetchone()
        self.abordo_licenca2 = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_lic WHERE Situacao = 'Baixado' AND Ano = 2")
        result = cursor.fetchone()
        self.baixado_licenca2 = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_lic WHERE Situacao = 'C/ Restrição' AND Ano = 2")
        result = cursor.fetchone()
        self.crestricao_licenca2 = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_lic WHERE Situacao = 'Disp. Domiciliar' AND Ano = 2")
        result = cursor.fetchone()
        self.dispdomiciliar_licenca2 = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_lic WHERE Situacao = 'LTS' AND Ano = 2")
        result = cursor.fetchone()
        self.lts_licenca2 = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_lic WHERE Situacao = 'HNMD' AND Ano = 2")
        result = cursor.fetchone()
        self.hnmd_licenca2 = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_lic WHERE Situacao = 'Licença' AND Ano = 2")
        result = cursor.fetchone()
        self.licenciados_licenca2 = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_lic WHERE Situacao = 'ST/GT' AND Ano = 2")
        result = cursor.fetchone()
        self.stgt_licenca2 = str(result[0])

        conn.commit()
        conn.close()
        
    def organiza_terceiro_licenca(self):
        conn = sqlite3.connect('dados.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_lic WHERE Situacao = 'A bordo' AND Ano = 3")
        result = cursor.fetchone()
        self.abordo_licenca3 = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_lic WHERE Situacao = 'Baixado' AND Ano = 3")
        result = cursor.fetchone()
        self.baixado_licenca3 = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_lic WHERE Situacao = 'C/ Restrição' AND Ano = 3")
        result = cursor.fetchone()
        self.crestricao_licenca3 = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_lic WHERE Situacao = 'Disp. Domiciliar' AND Ano = 3")
        result = cursor.fetchone()
        self.dispdomiciliar_licenca3 = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_lic WHERE Situacao = 'LTS' AND Ano = 3")
        result = cursor.fetchone()
        self.lts_licenca3 = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_lic WHERE Situacao = 'HNMD' AND Ano = 3")
        result = cursor.fetchone()
        self.hnmd_licenca3 = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_lic WHERE Situacao = 'Licença' AND Ano = 3")
        result = cursor.fetchone()
        self.licenciados_licenca3 = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_lic WHERE Situacao = 'ST/GT' AND Ano = 3")
        result = cursor.fetchone()
        self.stgt_licenca3 = str(result[0])

        conn.commit()
        conn.close()

    def organiza_quarto_licenca(self):
        conn = sqlite3.connect('dados.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_lic WHERE Situacao = 'A bordo' AND Ano = 4")
        result = cursor.fetchone()
        self.abordo_licenca4 = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_lic WHERE Situacao = 'Baixado' AND Ano = 4")
        result = cursor.fetchone()
        self.baixado_licenca4 = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_lic WHERE Situacao = 'C/ Restrição' AND Ano = 4")
        result = cursor.fetchone()
        self.crestricao_licenca4 = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_lic WHERE Situacao = 'Disp. Domiciliar' AND Ano = 4")
        result = cursor.fetchone()
        self.dispdomiciliar_licenca4 = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_lic WHERE Situacao = 'LTS' AND Ano = 4")
        result = cursor.fetchone()
        self.lts_licenca4 = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_lic WHERE Situacao = 'HNMD' AND Ano = 4")
        result = cursor.fetchone()
        self.hnmd_licenca4 = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_lic WHERE Situacao = 'Licença' AND Ano = 4")
        result = cursor.fetchone()
        self.licenciados_licenca4 = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_lic WHERE Situacao = 'ST/GT' AND Ano = 4")
        result = cursor.fetchone()
        self.stgt_licenca4 = str(result[0])

        conn.commit()
        conn.close()

    def input_texto_chave(self,textbox):
        self.chave_input = textbox
    
        conn = sqlite3.connect('dados.db')
        cursor = conn.cursor()

        numero_chave = str(self.chave_input)

        cursor.execute('SELECT NumerodaChave, Anterior, Atual, ÚltimaAlteração FROM dados_chave WHERE NumerodaChave = ?', (numero_chave,))

        info_licencas = cursor.fetchone()

        self.chave_input = str(info_licencas[0])
        self.chave_anteriormente_com = str(info_licencas[1])
        self.chave_atualmente_com = str(info_licencas[2])
        self.chave_ultima_alteracao = str(info_licencas[3])

        conn.commit()
        conn.close()

    def dar_chave(self,chave_pesquisa2):
        try:
            conn = sqlite3.connect('dados.db')
            cursor = conn.cursor()

            numero_chave = self.chave_input
            cursor.execute('SELECT Atual FROM dados_chave WHERE NumerodaChave = ?', (numero_chave,))
            antiga_sit = cursor.fetchone()
            antiga_sit = str(antiga_sit[0])

            nova_sit = str(chave_pesquisa2)
            nova_ultimaalt = datetime.now().strftime('%d/%m/%Y %H:%M')
            consulta_sql = 'UPDATE dados_chave SET Anterior = ?, Atual = ?, ÚltimaAlteração = ? WHERE NumerodaChave = ?'
            cursor.execute(consulta_sql, (antiga_sit, nova_sit, nova_ultimaalt, numero_chave))
            conn.commit()

            self.chaves_salvou = 'Alterações pendentes'
            
            cursor.execute('SELECT NumerodaChave, Anterior, Atual, ÚltimaAlteração FROM dados_chave WHERE NumerodaChave = ?', (numero_chave,))

            info_licencas = cursor.fetchone()

            self.chave_input = str(info_licencas[0])
            self.chave_anteriormente_com = str(info_licencas[1])
            self.chave_atualmente_com = str(info_licencas[2])
            self.chave_ultima_alteracao = str(info_licencas[3])

        except:
            self.chave_input = 'Chave não encontrada'
            self.chave_atualmente_com = 'Chave não encontrada'
            self.chave_anteriormente_com = 'Chave não encontrada'
            self.chave_ultima_alteracao = 'Chave não encontrada'
        
        self.registro_chave()
        self.organiza_claviculario()

    def retorna_chave(self):
        try:
            conn = sqlite3.connect('dados.db')
            cursor = conn.cursor()

            numero_chave = self.chave_input
            cursor.execute('SELECT Atual FROM dados_chave WHERE NumerodaChave = ?', (numero_chave,))
            antiga_sit = cursor.fetchone()
            antiga_sit = str(antiga_sit[0])

            nova_sit = "Claviculário"
            nova_ultimaalt = datetime.now().strftime('%d/%m/%Y %H:%M')
            consulta_sql = 'UPDATE dados_chave SET Anterior = ?, Atual = ?, ÚltimaAlteração = ? WHERE NumerodaChave = ?'
            cursor.execute(consulta_sql, (antiga_sit, nova_sit, nova_ultimaalt, numero_chave))
            conn.commit()

            self.chaves_salvou = 'Alterações pendentes'
            
            cursor.execute('SELECT NumerodaChave, Anterior, Atual, ÚltimaAlteração FROM dados_chave WHERE NumerodaChave = ?', (numero_chave,))

            info_licencas = cursor.fetchone()

            self.chave_input = str(info_licencas[0])
            self.chave_anteriormente_com = str(info_licencas[1])
            self.chave_atualmente_com = str(info_licencas[2])
            self.chave_ultima_alteracao = str(info_licencas[3])

        except:
            self.chave_input = 'Chave não encontrada'
            self.chave_atualmente_com = 'Chave não encontrada'
            self.chave_anteriormente_com = 'Chave não encontrada'
            self.chave_ultima_alteracao = 'Chave não encontrada'
        
        self.registro_chave()
        self.organiza_claviculario()

    def organiza_claviculario(self):

        conn = sqlite3.connect('dados.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(Atual) AS Valor FROM dados_chave WHERE Atual = 'Claviculário'")
        result = cursor.fetchone()
        self.chaves_claviculario = str(result[0])

        cursor.execute("SELECT COUNT(Atual) AS Valor FROM dados_chave")
        result = cursor.fetchone()
        self.chaves_fora = str(int(str(result[0])) - int(self.chaves_claviculario))

    botao_parte_alta = StringProperty('')
    
    def consultar_partealta(self,chave_pesquisa):
        
        self.consulta_pben(chave_pesquisa)

        conn = sqlite3.connect('dados.db')
        cursor = conn.cursor()

        numero_int = str(self.numero_atual)

        cursor.execute('SELECT Situacao, UltimaAlt FROM dados_partealta WHERE NumeroInt = ?', (numero_int,))

        info_partealta = cursor.fetchone()
        print(info_partealta)
        self.situacao_atual_partealta = info_partealta[0]
        self.ultima_alteracao_partealta = info_partealta[1]

        conn.commit()
        conn.close()

    def atualiza_partealta(self, button_text):
        if button_text == "":
            pass
        else:
            try:
                conn = sqlite3.connect('dados.db')
                cursor = conn.cursor()

                numero_int = self.numero_atual
                nova_sit = str(self.botao_parte_alta)
                nova_ultimaalt = datetime.now().strftime('%d/%m/%Y %H:%M')
                consulta_sql = 'UPDATE dados_partealta SET Situacao = ?, UltimaAlt = ? WHERE NumeroInt = ?'
                cursor.execute(consulta_sql, (nova_sit, nova_ultimaalt, numero_int))
                conn.commit()

            except:
                self.numero_atual = 'Selecione um aspirante'
                self.nome_guerra = ''
        
        cursor.execute("SELECT Situacao, UltimaAlt FROM dados_partealta WHERE NumeroInt = ?", (numero_int,))
        info_partealta = cursor.fetchone()
        self.situacao_atual_partealta = str(info_partealta[0])
        self.ultima_alteracao_partealta = str(info_partealta[1])
        print(info_partealta)

        conn.commit()
        conn.close()

        self.registro_partealta()
        self.organiza_controle_geral_partealta()
        self.organiza_primeiro_partealta()
        self.organiza_segundo_partealta()
        self.organiza_terceiro_partealta()
        self.organiza_quarto_partealta()

    def organiza_controle_geral_partealta(self):
        conn = sqlite3.connect('dados.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_partealta WHERE Situacao = 'Parte Alta'")
        result = cursor.fetchone()
        print(result)
        self.partealta_partealta = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_partealta WHERE Situacao = 'TFM'")
        result = cursor.fetchone()
        self.tfm_partealta = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_partealta WHERE Situacao = 'Sala de Estado'")
        result = cursor.fetchone()
        self.saladeestado_partealta = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_partealta WHERE Situacao = 'Enfermaria'")
        result = cursor.fetchone()
        self.enfermaria_partealta = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_partealta WHERE Situacao = 'Banco'")
        result = cursor.fetchone()
        self.banco_partealta = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_partealta WHERE Situacao = 'Biblioteca'")
        result = cursor.fetchone()
        self.biblioteca_partealta = str(result[0])

        conn.commit()
        conn.close()
    
    def organiza_primeiro_partealta(self):
        conn = sqlite3.connect('dados.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_partealta WHERE Situacao = 'Parte Alta' AND Ano = 1")
        result = cursor.fetchone()
        self.partealta_partealta1 = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_partealta WHERE Situacao = 'TFM' AND Ano = 1")
        result = cursor.fetchone()
        self.tfm_partealta1 = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_partealta WHERE Situacao = 'Sala de Estado' AND Ano = 1")
        result = cursor.fetchone()
        self.saladeestado_partealta1 = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_partealta WHERE Situacao = 'Enfermaria' AND Ano = 1")
        result = cursor.fetchone()
        self.enfermaria_partealta1 = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_partealta WHERE Situacao = 'Banco' AND Ano = 1")
        result = cursor.fetchone()
        self.banco_partealta1 = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_partealta WHERE Situacao = 'Biblioteca' AND Ano = 1")
        result = cursor.fetchone()
        self.biblioteca_partealta1 = str(result[0])

        conn.commit()
        conn.close()

    def organiza_segundo_partealta(self):
        conn = sqlite3.connect('dados.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_partealta WHERE Situacao = 'Parte Alta' AND Ano = 2")
        result = cursor.fetchone()
        self.partealta_partealta2 = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_partealta WHERE Situacao = 'TFM' AND Ano = 2")
        result = cursor.fetchone()
        self.tfm_partealta2 = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_partealta WHERE Situacao = 'Sala de Estado' AND Ano = 2")
        result = cursor.fetchone()
        self.saladeestado_partealta2 = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_partealta WHERE Situacao = 'Enfermaria' AND Ano = 2")
        result = cursor.fetchone()
        self.enfermaria_partealta2 = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_partealta WHERE Situacao = 'Banco' AND Ano = 2")
        result = cursor.fetchone()
        self.banco_partealta2 = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_partealta WHERE Situacao = 'Biblioteca' AND Ano = 2")
        result = cursor.fetchone()
        self.biblioteca_partealta2 = str(result[0])

        conn.commit()
        conn.close()

    def organiza_terceiro_partealta(self):
        conn = sqlite3.connect('dados.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_partealta WHERE Situacao = 'Parte Alta' AND Ano = 3")
        result = cursor.fetchone()
        self.partealta_partealta3 = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_partealta WHERE Situacao = 'TFM' AND Ano = 3")
        result = cursor.fetchone()
        self.tfm_partealta3 = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_partealta WHERE Situacao = 'Sala de Estado' AND Ano = 3")
        result = cursor.fetchone()
        self.saladeestado_partealta3 = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_partealta WHERE Situacao = 'Enfermaria' AND Ano = 3")
        result = cursor.fetchone()
        self.enfermaria_partealta3 = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_partealta WHERE Situacao = 'Banco' AND Ano = 3")
        result = cursor.fetchone()
        self.banco_partealta3 = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_partealta WHERE Situacao = 'Biblioteca' AND Ano = 3")
        result = cursor.fetchone()
        self.biblioteca_partealta3 = str(result[0])

        conn.commit()
        conn.close()

    def organiza_quarto_partealta(self):
        conn = sqlite3.connect('dados.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_partealta WHERE Situacao = 'Parte Alta' AND Ano = 4")
        result = cursor.fetchone()
        self.partealta_partealta4 = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_partealta WHERE Situacao = 'TFM' AND Ano = 4")
        result = cursor.fetchone()
        self.tfm_partealta4 = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_partealta WHERE Situacao = 'Sala de Estado' AND Ano = 4")
        result = cursor.fetchone()
        self.saladeestado_partealta4 = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_partealta WHERE Situacao = 'Enfermaria' AND Ano = 4")
        result = cursor.fetchone()
        self.enfermaria_partealta4 = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_partealta WHERE Situacao = 'Banco' AND Ano = 4")
        result = cursor.fetchone()
        self.banco_partealta4 = str(result[0])


        cursor.execute("SELECT COUNT(Situacao) AS Valor FROM dados_partealta WHERE Situacao = 'Biblioteca' AND Ano = 4")
        result = cursor.fetchone()
        self.biblioteca_partealta4 = str(result[0])

        conn.commit()
        conn.close()

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

        conn.commit()
        conn.close()

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
        nova_situacao = self.situacao_atual_licenca
        nova_ultimaalt = self.ultima_alteracao_licenca
        consulta_sql = 'UPDATE dados_lic SET Situacao = ?,UltimaAlt = ? WHERE NumeroInt = ?'
        cursor.execute(consulta_sql, (nova_situacao,nova_ultimaalt,numero_int))

        conn.commit()
        conn.close()

    def registro_partealta(self):
        registro_licencas = open("log_partealta.txt", "a", encoding='utf-8')
        registro_licencas.write(f"Número interno: {self.numero_atual}, Situação atual: {self.situacao_atual_licenca}, Última alteração: {self.ultima_alteracao_licenca}\n")
        registro_licencas.close()

        conn = sqlite3.connect('dados.db')
        cursor = conn.cursor()

        numero_int = self.numero_atual
        nova_situacao = self.situacao_atual_partealta
        nova_ultimaalt = self.ultima_alteracao_partealta
        consulta_sql = 'UPDATE dados_partealta SET Situacao = ?,UltimaAlt = ? WHERE NumeroInt = ?'
        cursor.execute(consulta_sql, (nova_situacao,nova_ultimaalt,numero_int))

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
        registro_chave = open("log_partealta.txt", "a", encoding='utf-8')
        registro_chave.write(texto)
        registro_chave.close()
        
    def registro_chave(self):
        registro_chave = open("log_chave.txt", "a", encoding='utf-8')
        registro_chave.write(f"Chave: {self.chave_input}, Atualmente com: {self.chave_atualmente_com}, Anteriormente com: {self.chave_anteriormente_com}, Última alteração: {self.chave_ultima_alteracao}\n")
        registro_chave.close() 

        conn = sqlite3.connect('dados.db')
        cursor = conn.cursor()

        numero_chave = self.chave_input
        antiga_situacao = self.chave_anteriormente_com
        nova_situacao = self.chave_atualmente_com
        nova_ultimaalt = self.chave_ultima_alteracao
        consulta_sql = 'UPDATE dados_chave SET Anterior = ?, Atual = ?, ÚltimaAlteração = ? WHERE NumerodaChave = ?'
        cursor.execute(consulta_sql, (antiga_situacao, nova_situacao, nova_ultimaalt, numero_chave))

        conn.commit()
        conn.close()   
    
if __name__ == '__main__':
    ControleGeral().run()
