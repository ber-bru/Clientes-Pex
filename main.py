from kivy.app import App
from kivy.core.text import LabelBase
from kivy.lang import Builder

KV = """
Screen:
    
    FloatLayout:
        
        Label:
            text: "Hello World"
            font_name: "BalooDa2Bold"
            pos_hint: {"center_y": .5}
"""


class MainApp(App):

    def build(self):
        return Builder.load_string(KV)


if __name__ == "__main__":
    LabelBase.register(name="BalooDa2Bold", fn_regular="assets/fonts/BalooDa2-Bold.ttf")

    MainApp().run()
