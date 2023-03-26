from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from funcoes_aspirante import cria_aspirantes, busca_aspirante
import pandas as pd
import os, sys
from kivy.resources import resource_add_path, resource_find

class ControleGeralApp(App):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        pben = pd.read_excel('teste.ods', engine = 'odf')
        self.aspirantes = cria_aspirantes(pben)

    nome_guerra = StringProperty()
    numero_atual = StringProperty()
    #Alterar datas
    numero_interno_2021 = StringProperty()
    numero_interno_2020 = StringProperty()
    numero_interno_2019 = StringProperty()
    numero_interno_2018 = StringProperty()
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

    def build(self):
        self.consulta = Consulta()
        self.dados_principais = DadosPrincipais()

    def on_button_click(self):
        aspirante = busca_aspirante(self.aspirantes,self.consulta.text_box)
        with open('temp.txt','w',encoding = 'utf-8') as temp:
            temp.writelines(str(aspirante.numero_interno_atual)+'\n')
            temp.writelines(str(aspirante.nome_guerra)+'\n')
            #Alterar datas
            temp.writelines(str(aspirante.numero_interno_2021)+'\n')
            temp.writelines(str(aspirante.numero_interno_2020)+'\n')
            temp.writelines(str(aspirante.numero_interno_2019)+'\n')
            temp.writelines(str(aspirante.numero_interno_2018)+'\n')
            temp.writelines(str(aspirante.companhia)+'\n')
            temp.writelines(str(aspirante.pelotao)+'\n')
            temp.writelines(str(aspirante.alojamento)+'\n')
            temp.writelines(str(aspirante.quarto_habilitacao)+'\n')
            temp.writelines(str(aspirante.nip)+'\n')
            temp.writelines(str(aspirante.sangue)+'\n')
            temp.writelines(str('TBD')+'\n')
            temp.writelines(str('TBD')+'\n')
            temp.writelines(str(aspirante.nome_completo)+'\n')
            temp.writelines(str(aspirante.data_nascimento)+'\n')
            temp.writelines(str(aspirante.telefone)+'\n')
            temp.writelines(str(aspirante.celular)+'\n')
            temp.writelines(str(aspirante.email)+'\n')

        with open('temp.txt','r',encoding = 'utf-8') as temp:
            lista = temp.readlines()
            self.numero_atual = lista[0].strip()
            self.nome_guerra = lista[1].strip()
            #Alterar datas
            self.numero_interno_2021 = lista[2].strip()
            self.numero_interno_2020 = lista[3].strip()
            self.numero_interno_2019 = lista[4].strip()
            self.numero_interno_2018 = lista[5].strip()
            self.nascimento = lista[15].strip()
            self.celular = lista[17].strip()
            self.telefone = lista[16].strip()
            self.email = lista[18].strip()
            self.companhia = lista[6].strip()
            self.pelotao = lista[7].strip()
            self.camarote = lista[8].strip()
            self.quarto = lista[9].strip()
            self.nip = lista[10].strip()
            self.sangue = lista[11].strip()
            self.nome_completo = lista[14].strip()

    def on_text_validate(self,textbox):
        self.consulta.text_box = textbox.text

class Consulta(BoxLayout):
    text_box = StringProperty('4001')

class DadosPrincipais(BoxLayout):
    pass

class NumerosAnteriores(BoxLayout):
    pass

class Contatos(BoxLayout):
    pass

class Organizacao(GridLayout):
    pass

class Relacional(GridLayout): 
    pass

if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    ControleGeralApp().run()