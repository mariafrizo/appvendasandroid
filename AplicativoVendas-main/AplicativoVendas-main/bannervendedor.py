from botoes import ImageButton, LabelButton
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
import requests

class BannerVendedor(FloatLayout):

    def __init__(self, **kwargs):
        super().__init__()

        with self.canvas:
            Color(rgb=(0, 0, 0, 1))
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.atualizar_rect, pos=self.atualizar_rect)

        id_vendedor = kwargs["id_vendedor"]

        link = f'https://aplicativovendashash-95608-default-rtdb.firebaseio.com/.json?orderBy="id_vendedor"&egualTo="{id_vendedor}"'
        requisicao = requests.get(link)
        requisicao_dic = requisicao.json()
        valor = list(requisicao_dic.values())[0]
        avatar = valor["avatar"]
        total_vendas = valor["total_vendas"]

        imagem = ImageButton(source=f"icones/fotos_perfil/{avatar}",
                  pos_hint={"right": 0.4, "top": 0.9}, size_hint=(0.3, 0.8))
        label_id = LabelButton(text=f"ID Vendedor: {id_vendedor}",
                    pos_hint={"right": 0.9, "top": 0.9}, size_hint=(0.5, 0.5))
        label_total = LabelButton(text=f"Total de Vendas: R${total_vendas}",
                       pos_hint={"right": 0.9, "top": 0.6}, size_hint=(0.5, 0.5))

        self.add_widget(imagem)
        self.add_widget(label_id)
        self.add_widget(label_total)

    def atualizar_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
