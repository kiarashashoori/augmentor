from kivy.app import App
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
# from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.image import Image
from kivy.core.window import Window

import os

class app(App):
    def on_start(self):
        Window.size = (1100, 600)
        Window.minimum_width = 800
        Window.minimum_height = 600

    def build(self):
        options = ['increase brightness', 'decrease brightness' ,'increase contrast',
                   'decrease contrast','decrease saturation' , 'increase saturation' ,
                   'salt&pepper', 'blur', 'vertical motion blur', 'horizental motion blur',
                   'shadow', 'sunlight', 'rotate' , 'flipped' , 'hue']

        checkbox_layout = StackLayout(orientation ='lr-tb')
        for i in range(len(options)):
            lbl = Label(text=options[i],size_hint = (None,None),size = ("150dp", "100dp"), halign='left',valign='middle',pos_hint = (None,None))
            chk = CheckBox(active=False,size_hint = (None,None),pos_hint = (None,None))
            checkbox_layout.add_widget(lbl)
            checkbox_layout.add_widget(chk)



        
        confirm_layout = AnchorLayout(anchor_x='center', anchor_y='bottom')
        confirm_btn = Button(text='start',size_hint = (None,None),size = ("75dp","40dp"),background_normal='',background_color=(0,0.8,0.3,1))
        confirm_layout.add_widget(confirm_btn)

        image_layout = AnchorLayout(anchor_x='right', anchor_y='bottom')
        auriga_image = Image(source = 'Auriga.png',size_hint = (None,None))
        image_layout.add_widget(auriga_image)

        screen_layout = FloatLayout()
        screen_layout.add_widget(confirm_layout)
        screen_layout.add_widget(checkbox_layout)
        screen_layout.add_widget(image_layout)
        return screen_layout

if __name__ == '__main__':
    root = app()
    root.run()