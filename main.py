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

import os

class app(App):
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


        screen_layout = FloatLayout()
        screen_layout.add_widget(confirm_layout)
        screen_layout.add_widget(checkbox_layout)
        return screen_layout
        # return confirm_layout
        # check_box_layout = []
        # check_box_rows_layout = []
        # for _ in range(3):
        #     check_box_layout.append(BoxLayout(orientation = 'horizontal'))
        # for _ in range(5):
        #     check_box_rows_layout.append(BoxLayout(orientation = 'vertical'))
        # y = 500
        # x = 100
        # for i in range(len(options)):
        #     lbl = Label(text=options[i], pos=(x, y))
        #     self.add_widget(lbl)
        #     chk = CheckBox(pos=(x + 85, y), active=False)
        #     self.add_widget(chk)
        #     if ((i+1) % 3 == 0):
        #         x = 100
        #         y -= 50
        #     else:
        #         x += 220
        # for i in range(len(options)):
        #     lbl = Label(text=options[i])
        #     chk = CheckBox(active=False)
        #     print (i // 3)
        #     if ((i+1) % 3 == 0):
        #         check_box_layout[i%3].add_widget(lbl)
        #         check_box_layout[i%3].add_widget(chk)
        #         for a in range(3):
        #             check_box_rows_layout[i // 3].add_widget(check_box_layout[a])
                
        #     else :
        #         check_box_layout[i%3].add_widget(lbl)
        #         check_box_layout[i%3].add_widget(chk)
        # for i in range(5):

        #     screen_layout.add_widget(check_box_rows_layout[i])
        
        # return screen_layout

if __name__ == '__main__':
    root = app()
    root.run()