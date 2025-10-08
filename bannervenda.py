from kivy.uix.label import  Label
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle

class BannerVenda(GridLayout):

    def __init__(self, **kwargs):
        self.rows = 1
        super().__init__()

        with self.canvas:
            Color(rgb=(0, 0, 0, 1))
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.atualizar_rect, pos=self.atualizar_rect)
        # kwargs = {"cliente": "mundial", "foto_cliente": "mundial.png" ..... }

        cliente = kwargs["cliente"]
        foto_cliente = kwargs["foto_cliente"]
        produto = kwargs["produto"]
        foto_produto = kwargs["foto_produto"]
        data = kwargs["data"]
        preco = float(kwargs["preco"])
        unidade = kwargs["unidade"]
        quantidade = float(kwargs["quantidade"])

        esquerda = FloatLayout()
        esquerda_imagem = Image(pos_hint= {"right": 1,"top": 0.95}, size_hint=(1, 0.75),
                                source=f"icones/fotos_clientes/{foto_cliente}")
        esquerda_label = Label(text=cliente, size_hint=(1, 0.2), pos_hint={"right": 1, "top": 0.2})
        esquerda.add_widget(esquerda_imagem)
        esquerda.add_widget(esquerda_label)

        meio = FloatLayout()
        meio_imagem = Image(pos_hint={"right": 1, "top": 0.95}, size_hint=(1, 0.75),
                           source=f"icones/fotos_produtos/{foto_produto}")
        meio_label = Label(text=produto, size_hint=(1, 0.2), pos_hint={"right": 1, "top": 0.2})
        meio.add_widget(meio_imagem)
        meio.add_widget(meio_label)

        direita = FloatLayout()
        direita_label_data = Label(text=f"Data: {data}",size_hint=(1, 0.33), pos_hint={"right": 1, "top": 0.9} )
        direita_label_preco = Label(text=f"Preço: R${preco:,.2f}", size_hint=(1, 0.33), pos_hint={"right": 1, "top": 0.63})
        direita_label_quantidade = Label(text=f"{quantidade} {unidade}", size_hint=(1, 0.33), pos_hint={"right": 1, "top": 0.4})
        direita.add_widget(direita_label_data)
        direita.add_widget(direita_label_preco)
        direita.add_widget(direita_label_quantidade)

        self.add_widget(esquerda)
        self.add_widget(meio)
        self.add_widget(direita)

    def atualizar_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

