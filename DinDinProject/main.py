from kivymd.app import MDApp
from kivy.lang import Builder

KV = '''
Screen:
    BoxLayout:
        MDToolbar:
        
<FloatLayout>:
    MDRaisedButton:
        text: 'Clica em mim!'
        size_hint_x: 0.5
        size_hint_y: 0.12
        pos_hint: {'center_x': .5, 'center_y': .5}
    MDTextField:
        hint_text: 'Informe o valor de uma fonte de renda'
    MDLabel:
        pos_hint: {'center_y': .3}
        halign: 'center'
        text:'Esqueceu sua senha?'
'''

class MyApp(MDApp):
    def build(self):

        return Builder.load_string(KV)

MyApp().run()
