# import os
# import logging

# logging.basicConfig(format="{asctime} - {levelname} - {message}",
#      style="{",
#      datefmt="%Y-%m-%d %H:%M",
#      level=logging.INFO
#  )

# logging.getLogger("kivy").disabled = True
# logging.getLogger("kivy.core").disabled = True
# logging.getLogger("kivy.base").disabled = True
from kivy.app import App
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.slider import Slider
from kivy.uix.progressbar import ProgressBar
import time
from kivy.clock import Clock
from kivy.clock import mainthread
import socket


import shutil
from augmentor import augmentor
import cv2
import threading

import parameters

import os
import logging



# logging.basicConfig(format="{asctime} - {levelname} - {message}",
#      style="{",
#      datefmt="%Y-%m-%d %H:%M",
#      level=logging.INFO
#  )

    
tb_values = parameters.path_values
data_cleaner_paths = parameters.data_cleaner_paths

class appSelectorApp(App):
    def on_start(self):
        Window.minimum_width = 1000
        Window.minimum_height = 600
        Window.size = (1000, 600)
    def build(self):
        Datacleaner_btn = Button(text='Data cleaner',size_hint = (None,None),size=("100dp","20dp")
                                    ,pos=(450,100),on_press=self.btn_clicked)
        Augmentor_btn = Button(text='Augmentor',size_hint = (None,None),size=("100dp","20dp")
                                    ,pos=(450,300),on_press=self.btn_clicked)
        DataAnalysis_btn = Button(text='Data analysis',size_hint = (None,None),size=("100dp","20dp")
                                    ,pos=(450,500),on_press=self.btn_clicked)
        floatlayout = FloatLayout()
        floatlayout.add_widget(Datacleaner_btn)
        floatlayout.add_widget(DataAnalysis_btn)
        floatlayout.add_widget(Augmentor_btn)
        return floatlayout
    def btn_clicked(self,instance):
        if instance.text == "Augmentor":
            logging.info('Augmentor selected')
            self.stop()
            augmentorPathBrowserApp().run()
        elif instance.text == "Data cleaner":
            logging.info('Data cleaner selected')
            self.stop()
            dataCleanerPathBrowserApp().run()
        elif instance.text == "Data analysis":
            pass
class dataCleanerPathBrowserApp(App):
    def on_start(self):
        Window.minimum_width = 1000
        Window.minimum_height = 600
        Window.size = (1000, 600)
    def build(self):
        global data_cleaner_paths
        img_lbl = Label(text='input image path:',size_hint = (None,None),color=(1,1,1,1),pos=(50,415))

        self.img_tb = TextInput(text = data_cleaner_paths[0],size_hint = (None,None),size=("600dp","30dp"),pos=(200,450),
                                 multiline=False,foreground_color=(1,1,1,1),background_normal='',background_color=(0.2,0.2,0.2,1))
        
        browse_img = Button(text='browse',size_hint = (None,None),size=("100dp","20dp"),
                                  pos=(800,455),on_press=self.btn_clicked)
        browse_img.id = 'image'

        label_lbl = Label(text='label path:',size_hint = (None,None),color=(1,1,1,1),pos=(50,315))

        self.label_tb = TextInput(text = data_cleaner_paths[1],size_hint = (None,None),size=("600dp","30dp"),pos=(200,350),
                                   multiline=False,foreground_color=(1,1,1,1),background_normal='',background_color=(0.2,0.2,0.2,1))

        browse_label = Button(text='browse',size_hint = (None,None),size=("100dp","20dp")
                                    ,pos=(800,355),on_press=self.btn_clicked)
        browse_label.id = 'label'

        lbl_layout = AnchorLayout(anchor_x='center', anchor_y='top')
        lbl = Label(text='select your paths :',size_hint = (None,None),color=(1,1,1,1))
        lbl_layout.add_widget(lbl)

        confirm_layout = AnchorLayout(anchor_x='center', anchor_y='bottom')
        confirm_btn = Button(text='confirm',size_hint = (None,None),size = ("75dp","40dp"),background_normal='',
                             background_color=(0,0.8,0.3,1),on_press=self.btn_clicked)
        confirm_layout.add_widget(confirm_btn)

        image_layout = AnchorLayout(anchor_x='right', anchor_y='bottom')
        auriga_image = Image(source = 'Auriga.png',size_hint = (None,None))
        image_layout.add_widget(auriga_image)

        floatlayout = FloatLayout()
        floatlayout.add_widget(img_lbl)
        floatlayout.add_widget(browse_img)
        floatlayout.add_widget(self.img_tb)
        floatlayout.add_widget(label_lbl)
        floatlayout.add_widget(browse_label)
        floatlayout.add_widget(self.label_tb)
        floatlayout.add_widget(confirm_layout)
        floatlayout.add_widget(image_layout)
        floatlayout.add_widget(lbl_layout)
        return floatlayout
    def btn_clicked(self,instance):
        flag = True
        if instance.text == 'confirm':
            for path in parameters.data_cleaner_paths:
                if path == '':
                    flag = False
            
            if flag == True:
                self.dataCleanerProcess()
            else:
                pass
        else :
            popup_layout = BoxLayout(orientation='vertical', spacing=10)

            file_chooser = FileChooserListView(
                            path=os.path.expanduser('~'),  # Start at home directory
                            dirselect=True,  # Allow folder selection
                            # filters=['*.png', '*.jpg', '*.jpeg'],  # Optional: filter for images
                            size_hint=(1, 0.8))
            button_layout = BoxLayout(size_hint=(1, 0.1), spacing=10)
        
            # Select button
            select_btn = Button(
                text='Select',
                on_press=lambda x: self.select_path(file_chooser,instance.id)
            )
            
            # Cancel button
            cancel_btn = Button(
                text='Cancel',
                on_press=self.close_popup
            )
            
            button_layout.add_widget(select_btn)
            button_layout.add_widget(cancel_btn)
            popup_layout.add_widget(file_chooser)
            popup_layout.add_widget(button_layout)
            self.popup = Popup(
            title=f"Select {instance.id} Path",
            content=popup_layout,
            size_hint=(0.9, 0.9),  # Relative to window size
            auto_dismiss=False  # Don't close when clicking outside
            )
            self.popup.open()
        
    
    def select_path(self, filechooser,id):
        """Handle path selection"""
        global data_cleaner_paths
        if filechooser.selection:
            if id == 'image':
                parameters.data_cleaner_paths[0] = filechooser.selection[0]
                data_cleaner_paths = parameters.data_cleaner_paths
                self.img_tb.text = parameters.data_cleaner_paths[0]
                logging.info(f"DATACLEANER : {parameters.data_cleaner_paths[0]} selected for image path")
            elif id == 'label':
                parameters.data_cleaner_paths[1] = filechooser.selection[0]
                data_cleaner_paths = parameters.data_cleaner_paths
                self.label_tb.text = parameters.data_cleaner_paths[1]
                logging.info(f"DATACLEANER : {parameters.data_cleaner_paths[1]} selected for label path")
            self.close_popup()
        else:
            logging.info(f"DATACLEANER : no path selected")
    
    def close_popup(self, *args):
        """Close the popup"""
        if hasattr(self, 'popup'):
            self.popup.dismiss()

    def dataCleanerProcess(self):
        label_filenames = []
        image_filenames = []
        logging.info(f'DATACLEANER: Data cleaning in progress...')
        
        label_path = os.listdir(parameters.data_cleaner_paths[1])
        for filename in label_path:
            if filename.endswith('.txt'):
                label_filenames.append(filename[:len(filename)-4])
        image_path = os.listdir(parameters.data_cleaner_paths[0])
        for filename in image_path:
            if filename.endswith('.jpg'):
                image_filenames.append(filename[:len(filename)-4])
        i = 1
        for imagefile in image_filenames:
            if imagefile in label_filenames:
                pass
            else:
                path = os.path.join(parameters.data_cleaner_paths[0],imagefile)
                path += '.jpg'
                os.remove(path)
                logging.info(f'DATACLEANER: {path} removed!')
            
            i += 1
        
        logging.info(f'DATACLEANER: Your data is now clean.')
        self.stop()
        appSelectorApp().run()

class augmentorPathBrowserApp(App):
    def on_start(self):
        Window.minimum_width = 1000
        Window.minimum_height = 600
        Window.size = (1000, 600)
    
    

    def build(self):
        #tb_values = [input_image,input_label,output_image,output_label]
        global tb_values
        floatlayout = FloatLayout()
        input_img_lbl = Label(text='input image path:',size_hint = (None,None),color=(1,1,1,1),pos=(50,415))

        self.input_img_tb = TextInput(text = tb_values[0],size_hint = (None,None),size=("600dp","30dp"),pos=(200,450),
                                 multiline=False,foreground_color=(1,1,1,1),background_normal='',background_color=(0.2,0.2,0.2,1))
        
        browse_input_img = Button(text='browse',size_hint = (None,None),size=("100dp","20dp"),
                                  pos=(800,455),on_press=self.btn_clicked)
        browse_input_img.id = 'input image'

        input_label_lbl = Label(text='input label path:',size_hint = (None,None),color=(1,1,1,1),pos=(50,315))

        self.input_label_tb = TextInput(text = tb_values[1],size_hint = (None,None),size=("600dp","30dp"),pos=(200,350),
                                   multiline=False,foreground_color=(1,1,1,1),background_normal='',background_color=(0.2,0.2,0.2,1))

        browse_input_label = Button(text='browse',size_hint = (None,None),size=("100dp","20dp")
                                    ,pos=(800,355),on_press=self.btn_clicked)
        browse_input_label.id = 'input label'

        output_img_lbl = Label(text='output image path:',size_hint = (None,None),color=(1,1,1,1),pos=(50,215))

        self.output_img_tb = TextInput(text = tb_values[2],size_hint = (None,None),size=("600dp","30dp"),pos=(200,250),
                                  multiline=False,foreground_color=(1,1,1,1),background_normal='',background_color=(0.2,0.2,0.2,1))

        browse_output_img = Button(text='browse',size_hint = (None,None),size=("100dp","20dp")
                                   ,pos=(800,255),on_press=self.btn_clicked)
        browse_output_img.id = 'output image'
        
        output_label_lbl = Label(text='output label path:',size_hint = (None,None),color=(1,1,1,1),pos=(50,115))

        self.output_label_tb = TextInput(text = tb_values[3],size_hint = (None,None),size=("600dp","30dp"),pos=(200,150),
                                    multiline=False,foreground_color=(1,1,1,1),background_normal='',background_color=(0.2,0.2,0.2,1))

        browse_output_label = Button(text='browse',size_hint = (None,None),size=("100dp","20dp")
                                     ,pos=(800,155),on_press=self.btn_clicked)
        browse_output_label.id = 'output label'

        lbl_layout = AnchorLayout(anchor_x='center', anchor_y='top')
        lbl = Label(text='select your paths :',size_hint = (None,None),color=(1,1,1,1))
        lbl_layout.add_widget(lbl)

        confirm_layout = AnchorLayout(anchor_x='center', anchor_y='bottom')
        confirm_btn = Button(text='confirm',size_hint = (None,None),size = ("75dp","40dp"),background_normal='',
                             background_color=(0,0.8,0.3,1),on_press=self.btn_clicked)
        confirm_layout.add_widget(confirm_btn)

        image_layout = AnchorLayout(anchor_x='right', anchor_y='bottom')
        auriga_image = Image(source = 'Auriga.png',size_hint = (None,None))
        image_layout.add_widget(auriga_image)

        floatlayout.add_widget(input_img_lbl)
        floatlayout.add_widget(browse_input_img)
        floatlayout.add_widget(self.input_img_tb)
        floatlayout.add_widget(input_label_lbl)
        floatlayout.add_widget(browse_input_label)
        floatlayout.add_widget(self.input_label_tb)
        floatlayout.add_widget(output_img_lbl)
        floatlayout.add_widget(browse_output_img)
        floatlayout.add_widget(self.output_img_tb)
        floatlayout.add_widget(output_label_lbl)
        floatlayout.add_widget(browse_output_label)
        floatlayout.add_widget(self.output_label_tb)
        floatlayout.add_widget(confirm_layout)
        floatlayout.add_widget(image_layout)
        floatlayout.add_widget(lbl_layout)
        
        return floatlayout
    
    def btn_clicked(self, instance):
        """Open popup with path chooser"""
        # Create main layout for popup
        flag = True
        if instance.text == 'confirm':
            for path in parameters.path_values:
                if path == '':
                    flag = False
            
            if flag == True:
                self.stop()
                augmentorModeSelectorApp().run()
            else:
                pass

        else :
            popup_layout = BoxLayout(orientation='vertical', spacing=10)

            file_chooser = FileChooserListView(
                            path=os.path.expanduser('~'),  # Start at home directory
                            dirselect=True,  # Allow folder selection
                            # filters=['*.png', '*.jpg', '*.jpeg'],  # Optional: filter for images
                            size_hint=(1, 0.8))
            button_layout = BoxLayout(size_hint=(1, 0.1), spacing=10)
        
            # Select button
            select_btn = Button(
                text='Select',
                on_press=lambda x: self.select_path(file_chooser,instance.id)
            )
            
            # Cancel button
            cancel_btn = Button(
                text='Cancel',
                on_press=self.close_popup
            )
            
            button_layout.add_widget(select_btn)
            button_layout.add_widget(cancel_btn)
            popup_layout.add_widget(file_chooser)
            popup_layout.add_widget(button_layout)
            self.popup = Popup(
            title=f"Select {instance.id} Path",
            content=popup_layout,
            size_hint=(0.9, 0.9),  # Relative to window size
            auto_dismiss=False  # Don't close when clicking outside
            )
            self.popup.open()
        
    
    def select_path(self, filechooser,id):
        """Handle path selection"""
        global tb_values
        if filechooser.selection:
            if id == 'input image':
                parameters.path_values[0] = filechooser.selection[0]
                tb_values = parameters.path_values
                self.input_img_tb.text = parameters.path_values[0]
                logging.info(f'AUGMENTOR : { parameters.path_values[0]} selected for input image path')
            elif id == 'input label':
                parameters.path_values[1] = filechooser.selection[0]
                tb_values = parameters.path_values
                self.input_label_tb.text = parameters.path_values[1]
                logging.info(f'AUGMENTOR : { parameters.path_values[1]} selected for input label path')
            elif id == 'output image':
                parameters.path_values[2] = filechooser.selection[0]
                tb_values = parameters.path_values
                self.output_img_tb.text = parameters.path_values[2]
                logging.info(f'AUGMENTOR : { parameters.path_values[2]} selected for output image path')
            elif id == 'output label':
                parameters.path_values[3] = filechooser.selection[0]
                tb_values = parameters.path_values
                self.output_label_tb.text = parameters.path_values[3]
                logging.info(f'AUGMENTOR : { parameters.path_values[3]} selected for output label path')
            self.close_popup()
        else:
            print("No path selected")
    
    def close_popup(self, *args):
        """Close the popup"""
        if hasattr(self, 'popup'):
            self.popup.dismiss()

class augmentorModeSelectorApp(App):
    def on_start(self):
        Window.size = (1100, 600)
        Window.minimum_width = 800
        Window.minimum_height = 600
    def build(self):
        checkbox_layout = StackLayout(orientation ='lr-tb')
        
        sign_lbl = Label(text='sign',size_hint = (None,None),size = ("150dp", "100dp"), halign='left',valign='middle',pos_hint = (None,None))
        self.sign_chk = CheckBox(active=False,size_hint = (None,None),pos_hint = (None,None))
        self.sign_chk.id = 'sign'
        self.sign_chk.bind(active = self.checkbox_is_active)
        checkbox_layout.add_widget(sign_lbl)
        checkbox_layout.add_widget(self.sign_chk)

        line_lbl = Label(text='line',size_hint = (None,None),size = ("150dp", "100dp"), halign='left',valign='middle',pos_hint = (None,None))
        self.line_chk = CheckBox(active=False,size_hint = (None,None),pos_hint = (None,None))
        self.line_chk.id = 'line'
        self.line_chk.bind(active = self.checkbox_is_active)
        checkbox_layout.add_widget(line_lbl)
        checkbox_layout.add_widget(self.line_chk)
        
        confirm_layout = AnchorLayout(anchor_x='center', anchor_y='bottom')
        confirm_btn = Button(text='start',size_hint = (None,None),size = ("75dp","40dp"),on_press = self.clicked,
                             background_normal='',background_color=(0,0.8,0.3,1))
        confirm_layout.add_widget(confirm_btn)

        image_layout = AnchorLayout(anchor_x='right', anchor_y='bottom')
        auriga_image = Image(source = 'Auriga.png',size_hint = (None,None))
        image_layout.add_widget(auriga_image)

        screen_layout = FloatLayout()
        screen_layout.add_widget(confirm_layout)
        screen_layout.add_widget(checkbox_layout)
        screen_layout.add_widget(image_layout)
        return screen_layout
    def checkbox_is_active(self,checkbox,value):
        if value :
            if checkbox.id == 'sign' and parameters.augmentor_mode != None:
                self.line_chk.active = False
            if checkbox.id == 'line' and parameters.augmentor_mode != None:
                self.sign_chk.active = False
            parameters.augmentor_mode = checkbox.id
    def clicked(self,_):
        if parameters.augmentor_mode != None:
            logging.info(f'AUGMENTOR:augmentor is working for {parameters.augmentor_mode}.')
            self.stop()
            augmentorSpeedApp().run()
        else:
            logging.info(f'AUGMENTOR: Select one mode!')

class augmentorSpeedApp(App):
    def on_start(self):
        Window.size = (1100, 600)
        Window.minimum_width = 800
        Window.minimum_height = 600
    def build(self):
        checkbox_layout = StackLayout(orientation ='lr-tb')
            
        super_slow_lbl = Label(text='super slow',size_hint = (None,None),size = ("150dp", "100dp"), halign='left',valign='middle',pos_hint = (None,None))
        self.super_slow_chk = CheckBox(active=False,size_hint = (None,None),pos_hint = (None,None))
        self.super_slow_chk.id = 'super slow'
        self.super_slow_chk.bind(active = self.checkbox_is_active)
        checkbox_layout.add_widget(super_slow_lbl)
        checkbox_layout.add_widget(self.super_slow_chk)

        slow_lbl = Label(text='slow',size_hint = (None,None),size = ("150dp", "100dp"), halign='left',valign='middle',pos_hint = (None,None))
        self.slow_chk = CheckBox(active=False,size_hint = (None,None),pos_hint = (None,None))
        self.slow_chk.id = 'slow'
        self.slow_chk.bind(active = self.checkbox_is_active)
        checkbox_layout.add_widget(slow_lbl)
        checkbox_layout.add_widget(self.slow_chk)

        fast_lbl = Label(text='fast',size_hint = (None,None),size = ("150dp", "100dp"), halign='left',valign='middle',pos_hint = (None,None))
        self.fast_chk = CheckBox(active=False,size_hint = (None,None),pos_hint = (None,None))
        self.fast_chk.id = 'fast'
        self.fast_chk.bind(active = self.checkbox_is_active)
        checkbox_layout.add_widget(fast_lbl)
        checkbox_layout.add_widget(self.fast_chk)

        super_fast_lbl = Label(text='super fast',size_hint = (None,None),size = ("150dp", "100dp"), halign='left',valign='middle',pos_hint = (None,None))
        self.super_fast_chk = CheckBox(active=False,size_hint = (None,None),pos_hint = (None,None))
        self.super_fast_chk.id = 'super fast'
        self.super_fast_chk.bind(active = self.checkbox_is_active)
        checkbox_layout.add_widget(super_fast_lbl)
        checkbox_layout.add_widget(self.super_fast_chk)

        device_name = socket.gethostname()

        confirm_layout = AnchorLayout(anchor_x='center', anchor_y='bottom')
        confirm_btn = Button(text='start',size_hint = (None,None),size = ("75dp","40dp"),on_press = self.clicked,
                             background_normal='',background_color=(0,0.8,0.3,1))
        confirm_layout.add_widget(confirm_btn)

        image_layout = AnchorLayout(anchor_x='right', anchor_y='bottom')
        auriga_image = Image(source = 'Auriga.png',size_hint = (None,None))
        image_layout.add_widget(auriga_image)
        screen_layout = FloatLayout()
        self.joke_lbl = Label(pos=(200,100),size_hint = (None,None))
        self.joke_lbl.text = ''
        device_name_layout = FloatLayout()
        if self.super_slow_chk.active == True:
            self.joke_lbl.text=f'lets golrizan for {device_name} to buy a new device'
        if self.super_fast_chk.active == True:
            self.joke_lbl.text=f"'{device_name}' please give me some mone \n even a single dollar matters 6280231539841105"
        device_name_layout.add_widget(self.joke_lbl)

        screen_layout.add_widget(device_name_layout)
        screen_layout.add_widget(confirm_layout)
        screen_layout.add_widget(checkbox_layout)
        screen_layout.add_widget(image_layout)
        return screen_layout
    
    def checkbox_is_active(self,checkbox,value):
        if value :
            if checkbox.id == 'super slow' :
                parameters.threads_num = 1
                self.super_fast_chk.active = False
                self.fast_chk.active = False
                self.slow_chk.active = False
                device_name = socket.gethostname()
                self.joke_lbl.text=f'lets golrizan for {device_name} to buy a new device'
                self.joke_lbl.texture_update()

            if checkbox.id == 'slow' :
                parameters.threads_num = 3
                self.super_fast_chk.active = False
                self.fast_chk.active = False
                self.super_slow_chk.active = False
                self.joke_lbl.text=''
                self.joke_lbl.texture_update()
            if checkbox.id == 'super fast' :
                parameters.threads_num = 9
                self.slow_chk.active = False
                self.fast_chk.active = False
                self.super_slow_chk.active = False
                device_name = socket.gethostname()
                self.joke_lbl.text=f"'{device_name}' please give me some money \n even a single dollar matters 6280231539841105"
                self.joke_lbl.texture_update()
            if checkbox.id == 'fast' :
                parameters.threads_num = 6
                self.slow_chk.active = False
                self.super_fast_chk.active = False
                self.super_slow_chk.active = False
                self.joke_lbl.text=''
                self.joke_lbl.texture_update()
                
    def clicked(self,_):
        if parameters.threads_num != -1:
            logging.info(f"AUGMENTOR: augmentor will work with '{parameters.threads_num}' threads!")
            self.stop()
            augmentSelectorApp().run()

class augmentSelectorApp(App):
    def on_start(self):
        Window.size = (1100, 600)
        Window.minimum_width = 800
        Window.minimum_height = 600

    def build(self):
        options = ['increase brightness', 'decrease brightness' ,'increase contrast',
                   'decrease contrast','decrease saturation' , 'increase saturation' ,
                   'salt&pepper', 'blur', 'vertical motion blur', 'horizontal motion blur',
                   'shadow', 'sunlight', 'rotate' , 'flipped' , 'hue']

        checkbox_layout = StackLayout(orientation ='lr-tb')
        for i in range(len(options)):
            lbl = Label(text=options[i],size_hint = (None,None),size = ("150dp", "100dp"), halign='left',valign='middle',pos_hint = (None,None))
            chk = CheckBox(active=False,size_hint = (None,None),pos_hint = (None,None))
            chk.id = options[i]
            chk.bind(active = self.checkbox_is_active)
            checkbox_layout.add_widget(lbl)
            checkbox_layout.add_widget(chk)



        
        confirm_layout = AnchorLayout(anchor_x='center', anchor_y='bottom')
        confirm_btn = Button(text='start',size_hint = (None,None),size = ("75dp","40dp"),on_press = self.clicked,
                             background_normal='',background_color=(0,0.8,0.3,1))
        confirm_layout.add_widget(confirm_btn)

        image_layout = AnchorLayout(anchor_x='right', anchor_y='bottom')
        auriga_image = Image(source = 'Auriga.png',size_hint = (None,None))
        image_layout.add_widget(auriga_image)

        screen_layout = FloatLayout()
        screen_layout.add_widget(confirm_layout)
        screen_layout.add_widget(checkbox_layout)
        screen_layout.add_widget(image_layout)
        return screen_layout
    
    def checkbox_is_active(self,checkbox,value):
        if value :
            parameters.active_checkboxs.append(checkbox.id)
        else :
            parameters.active_checkboxs.remove(checkbox.id)
    
    def clicked(self,instance):
        if (len(parameters.active_checkboxs) >0):
            self.stop()
            augmentViewerApp().run()
        else:
            popup_layout = BoxLayout(orientation='vertical', spacing=10)
            lbl = Label(text='you dont select any augment type')
            popup_layout.add_widget(lbl)
            self.popup = Popup(
            title=f"Error",
            content=popup_layout,
            size_hint=(0.7, 0.7),  # Relative to window size
            auto_dismiss=True  # Don't close when clicking outside
            )
            self.popup.open()
            

class augmentViewerApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.increase_brightness_threshold = 50
        self.decrease_brightness_threshold = 50

        self.increase_contrast_threshold = 30
        self.decrease_contrast_threshold = 30

        self.increase_saturation_threshold = 25
        self.decrease_saturation_threshold = 25

        self.salt_pepper_threshold = 50

        self.blur_threshold = 5

        self.horizontal_blur_threshold = 25
        self.vertical_blur_threshold = 25

        self.rotate_angle = 10

        self.sunlight_nums = 2
        self.sunlight_blur = 11
        self.sunlight_intensity = 80

        self.b = 50

        self.shadow_strength = 80
        self.shadow_blur = 11

        self.i = 0
        possible_images = os.listdir(parameters.path_values[0])
        self.images = []
        
        for image in possible_images:
            if image.endswith(".jpg"):
                self.images.append(image)
    def on_start(self):
        Window.size = (1200, 800)
        Window.minimum_width = 1200
        Window.minimum_height = 800
    def build(self):
        if len(parameters.active_checkboxs) <= 0:
            pass

        augmentViewerApp.create_sample(self)
        auriga_image_layout = AnchorLayout(anchor_x='right', anchor_y='bottom')
        auriga_image = Image(source = 'Auriga.png',size_hint = (None,None))
        auriga_image_layout.add_widget(auriga_image)
        
        image_layout = AnchorLayout(anchor_x='center', anchor_y='top')
        
        self.image = Image(source = "cache/output_img.jpg",size_hint = (0.8,0.6))
        self.image.reload()
        image_layout.add_widget(self.image)

        right_btn_layout = AnchorLayout(anchor_x='right', anchor_y='center')
        right_btn = Button(text='>',size_hint = (None,None),size=("40dp","40dp"),
                           on_press = self.right_clicked)
        right_btn_layout.add_widget(right_btn)

        left_btn_layout = AnchorLayout(anchor_x='left', anchor_y='center')
        left_btn = Button(text='<',size_hint = (None,None),size=("40dp","40dp"),
                          on_press = self.left_clicked)
        left_btn_layout.add_widget(left_btn)

        confirm_layout = AnchorLayout(anchor_x='center', anchor_y='bottom')
        confirm_btn = Button(size_hint = (None,None),size = ("75dp","40dp"),
                             background_normal='',background_color=(0,0.8,0.3,1),on_press = self.confirm_clicked)
        if len(parameters.active_checkboxs)> 1 :
            confirm_btn.text = 'confirm'
        else:
            confirm_btn.text = 'start'
        confirm_layout.add_widget(confirm_btn)

        threshold_layout = FloatLayout()
        
        if (parameters.active_checkboxs[0] == 'increase brightness'):
            self.threshold = Slider(min=0, max=200, value=self.increase_brightness_threshold,
                                    size_hint=(None, None), width=600, height=40,pos=(200,100))
        if (parameters.active_checkboxs[0] == 'decrease brightness'):
            self.threshold = Slider(min=0, max=200, value=self.decrease_brightness_threshold,
                                    size_hint=(None, None), width=600, height=40,pos=(200,100))    

        if (parameters.active_checkboxs[0] == 'increase contrast'):
            self.threshold = Slider(min=0, max=180, value=self.increase_contrast_threshold,
                                    size_hint=(None, None), width=600, height=40,pos=(200,100))
        if (parameters.active_checkboxs[0] == 'decrease contrast'):
            self.threshold = Slider(min=0, max=180, value=self.decrease_contrast_threshold,
                                size_hint=(None, None), width=600, height=40,pos=(200,100))
        
        if (parameters.active_checkboxs[0] == 'increase saturation'):
            self.threshold = Slider(min=0, max=180, value=self.increase_saturation_threshold,
                                    size_hint=(None, None), width=600, height=40,pos=(200,100))
        if (parameters.active_checkboxs[0] == 'decrease saturation'):
            self.threshold = Slider(min=0, max=200, value=self.decrease_saturation_threshold,
                                    size_hint=(None, None), width=600, height=40,pos=(200,100))
                
        if (parameters.active_checkboxs[0] == 'salt&pepper'):
            self.threshold = Slider(min=0, max=200, value=self.salt_pepper_threshold,
                                    size_hint=(None, None), width=600, height=40,pos=(200,100))
            
        if (parameters.active_checkboxs[0] == 'blur'):
            self.threshold = Slider(min=0, max=33, value=self.blur_threshold,
                                    size_hint=(None, None), width=600, height=40,pos=(200,100))
        if (parameters.active_checkboxs[0] == 'horizontal motion blur'):
            self.threshold = Slider(min=0, max=110, value=self.horizontal_blur_threshold,
                                    size_hint=(None, None), width=600, height=40,pos=(200,100))
        if (parameters.active_checkboxs[0] == 'vertical motion blur'):
            self.threshold = Slider(min=0, max=110, value=self.vertical_blur_threshold,
                                    size_hint=(None, None), width=600, height=40,pos=(200,100))
        if (parameters.active_checkboxs[0] == 'rotate'):
            self.threshold = Slider(min=-89, max=89, value=self.rotate_angle,
                                    size_hint=(None, None), width=600, height=40,pos=(200,100))
        
        if (parameters.active_checkboxs[0] == 'sunlight'):
            numlbl = Label(text = 'num',size_hint = (None,None),size = ("150dp", "100dp"), halign='left',valign='middle',pos=(110,120))
            self.threshold_sunlight_num = Slider(min=1, max=7, value=self.sunlight_nums,
                                            size_hint=(None, None), width=600, height=40,pos=(200,150))
            intensitylbl = Label(text = 'intensity',size_hint = (None,None),size = ("150dp", "100dp"), halign='left',valign='middle',pos=(110,70))
            self.threshold_sunlight_intensity = Slider(min=0, max=100, value=self.sunlight_intensity,
                                                size_hint=(None, None), width=600, height=40,pos=(200,100))
            blurlbl = Label(text = 'blur',size_hint = (None,None),size = ("150dp", "100dp"), halign='left',valign='middle',pos=(110,20))
            self.threshold_sunlight_blur = Slider(min=3, max=91, value=self.sunlight_blur,
                                                size_hint=(None, None), width=600, height=40,pos=(200,50))
        
        if (parameters.active_checkboxs[0] == 'shadow'):
            blurlbl = Label(text = 'blur',size_hint = (None,None),size = ("150dp", "100dp"), halign='left',valign='middle',pos=  (110,120))
            self.threshold_shadow_blur = Slider(min=3, max=91, value=self.shadow_blur,
                                            size_hint=(None, None), width=600, height=40,pos=(200,150))
            strengthlbl = Label(text = 'strength',size_hint = (None,None),size = ("150dp", "100dp"), halign='left',valign='middle',pos=(110,70))
            self.threshold_shadow_strength = Slider(min=0, max=100, value=self.shadow_strength,
                                            size_hint=(None, None), width=600, height=40,pos=(200,100))
            
            
        lbl = Label(text=parameters.active_checkboxs[0],pos=(20,100),size_hint = (None,None))
        if (parameters.active_checkboxs[0] in ['rotate','vertical motion blur','horizontal motion blur','blur','flipped','shadow']) == False:
            self.times = TextInput(text = '1',size_hint = (None,None),size=("50dp","30dp"),pos=(100,100),
                                        multiline=False,foreground_color=(1,1,1,1),background_normal='',background_color=(0.2,0.2,0.2,1))
        apply_btn = Button(text='apply',size_hint = (None,None),size = ("75dp","40dp"),
                             background_normal='',background_color=(0,0.8,0.3,1),pos=(800,100),on_press = self.apply_clicked)
        
        
        if parameters.active_checkboxs[0] != 'flipped' and parameters.active_checkboxs[0] != 'sunlight' and parameters.active_checkboxs[0] != 'shadow':
            threshold_layout.add_widget(self.threshold)
        
        if parameters.active_checkboxs[0] == 'sunlight':
            threshold_layout.add_widget(blurlbl)
            threshold_layout.add_widget(intensitylbl)
            threshold_layout.add_widget(numlbl)
            threshold_layout.add_widget(self.threshold_sunlight_blur)
            threshold_layout.add_widget(self.threshold_sunlight_intensity)
            threshold_layout.add_widget(self.threshold_sunlight_num)
        if parameters.active_checkboxs[0] == 'shadow':
            threshold_layout.add_widget(blurlbl)
            threshold_layout.add_widget(strengthlbl)
            threshold_layout.add_widget(self.threshold_shadow_blur)
            threshold_layout.add_widget(self.threshold_shadow_strength)

            
        threshold_layout.add_widget(apply_btn)
        if (parameters.active_checkboxs[0] in ['rotate','vertical motion blur','horizontal motion blur','blur','flipped','shadow']) == False:
            threshold_layout.add_widget(self.times)
        threshold_layout.add_widget(lbl)

                
        

        self.screen_layout = FloatLayout()
        self.screen_layout.add_widget(auriga_image_layout)
        self.screen_layout.add_widget(image_layout)
        self.screen_layout.add_widget(right_btn_layout)
        self.screen_layout.add_widget(left_btn_layout)
        self.screen_layout.add_widget(confirm_layout)
        self.screen_layout.add_widget(threshold_layout)

        return self.screen_layout
    
    def right_clicked(self,instance):
        if self.i + 1< len(self.images):
            self.i += 1
        else :
            self.i = 0
        augmentViewerApp.create_sample(self)
        self.image.reload()

    def left_clicked(self,instance):
        if self.i > 0:
            self.i -= 1
        else :
            self.i = len(self.images)-1
        augmentViewerApp.create_sample(self)
        self.image.reload()

    def apply_clicked(self,_):
        if (parameters.active_checkboxs[0] == 'increase brightness'):
            self.increase_brightness_threshold = int(self.threshold.value)
        if (parameters.active_checkboxs[0] == 'decrease brightness'):
            self.decrease_brightness_threshold = int(self.threshold.value)

        if (parameters.active_checkboxs[0] == 'increase contrast'):
            self.increase_contrast_threshold = int(self.threshold.value)
        if (parameters.active_checkboxs[0] == 'decrease contrast'):
            self.decrease_contrast_threshold = int(self.threshold.value)
        
        if (parameters.active_checkboxs[0] == 'increase saturation'):
            self.increase_saturation_threshold = int(self.threshold.value)
        if (parameters.active_checkboxs[0] == 'decrease saturation'):
            self.decrease_saturation_threshold = int(self.threshold.value)

        if (parameters.active_checkboxs[0] == 'salt&pepper'):
            self.salt_pepper_threshold = int(self.threshold.value)

        if (parameters.active_checkboxs[0] == 'blur'):
            val = int(self.threshold.value)
            if (val % 2 == 0):
                val -= 1
            self.blur_threshold = val

        if (parameters.active_checkboxs[0] == 'horizontal motion blur'):
            val = int(self.threshold.value)
            if (val % 2 == 0):
                val -= 1
            self.horizontal_blur_threshold = val
        if (parameters.active_checkboxs[0] == 'vertical motion blur'):
            val = int(self.threshold.value)
            if (val % 2 == 0):
                val -= 1
            self.vertical_blur_threshold = val

        if (parameters.active_checkboxs[0] == 'rotate'):
            self.rotate_angle = int(self.threshold.value)
        
        if (parameters.active_checkboxs[0] == 'sunlight'):
            val = int(self.threshold_sunlight_blur.value)
            if (val % 2 == 0):
                val -= 1
            self.sunlight_blur = val
            self.sunlight_intensity = int(self.threshold_sunlight_intensity.value)
            self.sunlight_nums = int(self.threshold_sunlight_num.value)
        
        if (parameters.active_checkboxs[0] == 'shadow'):
            val = int(self.threshold_shadow_blur.value)
            if (val % 2 == 0):
                val -= 1
            self.shadow_blur = val
            self.shadow_strength = int(self.threshold_shadow_strength.value)
        
        logging.info(f"AUGMENTOR:Your setting for '{parameters.active_checkboxs[0]}' changed!")
        

        augmentViewerApp.create_sample(self)
        self.image.reload()

    def confirm_clicked(self,instance):
        if (parameters.active_checkboxs[0] == 'increase brightness'):
            parameters.augment_process.append(('increase brightness',int(self.times.text),self.increase_brightness_threshold))
        if (parameters.active_checkboxs[0] == 'decrease brightness'):
            parameters.augment_process.append(('decrease brightness',int(self.times.text),self.decrease_brightness_threshold))

        if (parameters.active_checkboxs[0] == 'increase contrast'):
            parameters.augment_process.append(('increase contrast',int(self.times.text),self.increase_contrast_threshold))
        if (parameters.active_checkboxs[0] == 'decrease contrast'):
            parameters.augment_process.append(('decrease contrast',int(self.times.text),self.decrease_contrast_threshold))

        if (parameters.active_checkboxs[0] == 'increase saturation'):
            parameters.augment_process.append(('increase saturation',int(self.times.text),self.increase_saturation_threshold))
        if (parameters.active_checkboxs[0] == 'decrease saturation'):
            parameters.augment_process.append(('decrease saturation',int(self.times.text),self.decrease_saturation_threshold))

        if (parameters.active_checkboxs[0] == 'salt&pepper'):
            parameters.augment_process.append(('salt&pepper',int(self.times.text),self.salt_pepper_threshold))
        
        if (parameters.active_checkboxs[0] == 'blur'):
            parameters.augment_process.append(('blur',1,self.blur_threshold))

        if (parameters.active_checkboxs[0] == 'horizontal motion blur'):
            parameters.augment_process.append(('horizontal motion blur',1,self.horizontal_blur_threshold))
        if (parameters.active_checkboxs[0] == 'vertical motion blur'):
            parameters.augment_process.append(('vertical motion blur',1,self.vertical_blur_threshold))

        if (parameters.active_checkboxs[0] == 'flipped'):
            parameters.augment_process.append(('flipped',1,None))
        
        if (parameters.active_checkboxs[0] == 'rotate'):
            parameters.augment_process.append(('rotate',1,self.rotate_angle))
        
        if (parameters.active_checkboxs[0] == 'sunlight'):
            parameters.augment_process.append(('sunlight',int(self.times.text),
                                               (self.sunlight_blur,self.sunlight_intensity/100,self.sunlight_nums)))
        if (parameters.active_checkboxs[0] == 'shadow'):
            parameters.augment_process.append(('shadow',1,(self.shadow_blur,self.shadow_strength/100)))

        logging.info(f"AUGMENTOR:Your setting for '{parameters.active_checkboxs[0]}' saved!")

        if (len(parameters.active_checkboxs) > 1):
            parameters.active_checkboxs.pop(0)
            self.screen_layout.clear_widgets()
            augmentViewerApp().stop()
            augmentViewerApp().run()
        else :
            logging.info(f"AUGMENTOR: Augmentation in progress...")

            augmentProcessApp.calculateAugmentedImagesQuantity()
            self.stop()
            augmentProcessApp().run()

        
    def create_sample(self):
        image_path = os.path.join(parameters.path_values[0],self.images[self.i])
        shutil.copy2(image_path,"cache/input_img.jpg")
        
        img = cv2.imread("cache/input_img.jpg")
        if (parameters.active_checkboxs[0] == 'increase brightness'):
            sample_img = augmentor.brightnessIncreasedAugmentor(img,self.increase_brightness_threshold,'sample')
        if (parameters.active_checkboxs[0] == 'decrease brightness'):
            sample_img = augmentor.brightnessDecreasedAugmentor(img,self.decrease_brightness_threshold,'sample')

        if (parameters.active_checkboxs[0] == 'increase contrast'):
            sample_img = augmentor.contrastIncreasedAugmentor(img,self.increase_contrast_threshold,'sample')
        if (parameters.active_checkboxs[0] == 'decrease contrast'):
            sample_img = augmentor.contrastDecreasedAugmentor(img,self.decrease_contrast_threshold,'sample')

        if (parameters.active_checkboxs[0] == 'increase saturation'):
            sample_img = augmentor.saturationIncreasedAugmentor(img,self.increase_saturation_threshold,'sample')
        if (parameters.active_checkboxs[0] == 'decrease saturation'):
            sample_img = augmentor.saturationDecreasedAugmentor(img,self.decrease_saturation_threshold,'sample')

        if (parameters.active_checkboxs[0] == 'salt&pepper'):
            sample_img = augmentor.saltPepperAugmentor(img,self.salt_pepper_threshold,'sample')
        
        if (parameters.active_checkboxs[0] == 'blur'):
            sample_img = augmentor.blurAugmentor(img,self.blur_threshold,'sample')
        
        if (parameters.active_checkboxs[0] == 'horizontal motion blur'):
            sample_img = augmentor.shakeHorizontalBlurAugmentor(img,self.horizontal_blur_threshold,'sample')
        if (parameters.active_checkboxs[0] == 'vertical motion blur'):
            sample_img = augmentor.shakeVerticalBlurAugmentor(img,self.vertical_blur_threshold,'sample')

        if (parameters.active_checkboxs[0] == 'flipped'):
            sample_img = augmentor.flippedAugmentor(img,None,'sample')
        if (parameters.active_checkboxs[0] == 'rotate'):
            sample_img = augmentor.rotateAugmentor(img,None,self.rotate_angle,'sample')
        
        if (parameters.active_checkboxs[0] == 'sunlight'):
            sample_img = augmentor.sunlightAugmentor(img,self.sunlight_nums,self.sunlight_blur,self.sunlight_intensity/100)
        
        if (parameters.active_checkboxs[0] == 'shadow'):
            imageName = self.images[self.i]
            babooo = imageName[:len(imageName)-4]
            babooo += '.txt'
            label_path = os.path.join(parameters.path_values[1],babooo)
            with open(label_path,'r') as f:
                lines = f.readlines()
            sample_img = augmentor.shadowAugmentor(img,lines,self.shadow_blur,self.shadow_strength/100)
            
        
        logging.info(f"AUGMENTOR:Showing sample image for '{parameters.active_checkboxs[0]}'")
        cv2.imwrite("cache/output_img.jpg",sample_img)

class augmentProcessApp(App):
   
    def on_start(self):
        Window.size = (1200, 800)
        Window.minimum_width = 1200
        Window.minimum_height = 800
        
    def build(self):
        auriga_image_layout = AnchorLayout(anchor_x='right', anchor_y='bottom')
        auriga_image = Image(source = 'Auriga.png',size_hint = (None,None))
        auriga_image_layout.add_widget(auriga_image)
        layout = FloatLayout()
        self.pb = ProgressBar(max=parameters.quantity, value=parameters.counter, size_hint=(None, None), width=800, height=30,pos=(200, 400))
        self.lbl = Label(text = f"{parameters.counter}/{parameters.quantity}",size_hint = (None,None),size = ("150dp", "100dp"),
                          halign='left',valign='middle',pos=(550, 350),color=(1,1,1,1))
        layout.add_widget(self.pb)
        layout.add_widget(self.lbl)
        layout.add_widget(auriga_image_layout)
        self.augmentProcessHandler()

        # UI update loop (main thread safe)
        Clock.schedule_interval(self.update_progress, 0.1)
        return layout

    @mainthread
    def augmentProcessHandler(self):
        threads = []
       
        if len(parameters.augment_process) >= parameters.threads_num:
            for i in range(parameters.threads_num):
                aug = augmentor(parameters.path_values[0],parameters.path_values[1],parameters.path_values[2],
                                    parameters.path_values[3],parameters.augment_process[i][1],parameters.augment_process[i][0])
                t = threading.Thread(target=augmentor.action,args=(aug,parameters.augment_process[i][2]))
                threads.append(t)
                parameters.finish.append(parameters.augment_process[i][0])
            for _ in range(parameters.threads_num):
                parameters.augment_process.pop(0)
        else :
            for i in range(len(parameters.augment_process)):
                aug = augmentor(parameters.path_values[0],parameters.path_values[1],parameters.path_values[2],
                                    parameters.path_values[3],parameters.augment_process[i][1],parameters.augment_process[i][0])
                t = threading.Thread(target=augmentor.action,args=(aug,parameters.augment_process[i][2]))
                threads.append(t)
                parameters.finish.append(parameters.augment_process[i][0])
            for _ in range(len(parameters.augment_process)):
                parameters.augment_process.pop(0)
        for thread in threads:
            thread.start()
    
    @staticmethod
    def calculateAugmentedImagesQuantity():
        input_images_num = len(os.listdir(parameters.path_values[1]))
        times = 0
        for augment in parameters.augment_process:
            times += augment[1]
        parameters.quantity = times * input_images_num

    def finish(self):
        self.stop()
        finitoApp().run()

    def update_progress(self, dt):
        if len(parameters.augment_process) != 0 and len(parameters.finish) == 0:
            self.augmentProcessHandler()

        self.pb.value = parameters.counter
        self.lbl.text = f"{parameters.counter}/{parameters.quantity}"

        if parameters.counter >= parameters.quantity:
            Clock.unschedule(self.update_progress)
            self.finish()

        
        
    
class finitoApp(App):
    def on_start(self):
        Window.size = (1200, 800)
        Window.minimum_width = 1200
        Window.minimum_height = 800
        
    def build(self):
        logging.info("AUGMENTOR: Augmentation process completed successfully.")
        auriga_image_layout = AnchorLayout(anchor_x='center', anchor_y='center')
        auriga_image = Image(source = 'Auriga.png',size_hint = (None,None),size=(400,400))
        auriga_image_layout.add_widget(auriga_image)


        layout = FloatLayout()
        layout.add_widget(auriga_image_layout)
        return layout

if __name__ == '__main__':
    root = augmentorModeSelectorApp()
    root.run()

