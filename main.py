from kivy.app import App
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup

class MultiCheckBox(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        options = ['brightness', 'contrast', 'flipped' , 'saturation' , 'salt' , 'pepper' , 'salt&pepper']
        y = 500
        x = 100
        for i in range(len(options)):
            lbl = Label(text=options[i], pos=(x, y))
            self.add_widget(lbl)
            chk = CheckBox(pos=(x + 75, y), active=False)
            self.add_widget(chk)
            if ((i+1) % 3 == 0):
                x = 100
                y -= 50
            else:
                x += 220
        
        btn = Button(text='start',pos=(375,50),size = ("75dp","40dp"),background_normal='',background_color=(0,0.8,0.3,1))
        self.add_widget(btn)
        


class CheckBoxApp(App):
    def build(self):
        return MultiCheckBox()

if __name__ == '__main__':
    CheckBoxApp().run()