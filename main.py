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

import shutil
from augmentor import augmentor
import cv2

import parameters

import os
    
tb_values = parameters.path_values
class PathBrowserApp(App):
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
                augmentSelectorApp().run()
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
            elif id == 'input label':
                parameters.path_values[1] = filechooser.selection[0]
                tb_values = parameters.path_values
                self.input_label_tb.text = parameters.path_values[1]
            elif id == 'output image':
                parameters.path_values[2] = filechooser.selection[0]
                tb_values = parameters.path_values
                self.output_img_tb.text = parameters.path_values[2]
            elif id == 'output label':
                parameters.path_values[3] = filechooser.selection[0]
                tb_values = parameters.path_values
                self.output_label_tb.text = parameters.path_values[3]
            self.close_popup()
        else:
            print("No path selected")
    
    def close_popup(self, *args):
        """Close the popup"""
        if hasattr(self, 'popup'):
            self.popup.dismiss()

class augmentSelectorApp(App):
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
        # print(parameters.active_checkboxs)
        if (len(parameters.active_checkboxs) >0):
            self.stop()
            print(parameters.active_checkboxs)
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
        print('hi')
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
        confirm_btn = Button(text='confirm',size_hint = (None,None),size = ("75dp","40dp"),
                             background_normal='',background_color=(0,0.8,0.3,1),on_press = self.confirm_clicked)
        confirm_layout.add_widget(confirm_btn)

        threshold_layout = FloatLayout()
        self.threshold = TextInput(text = '50',size_hint = (None,None),size=("600dp","30dp"),pos=(200,100),
                                    multiline=False,foreground_color=(1,1,1,1),background_normal='',background_color=(0.2,0.2,0.2,1))
        self.times = TextInput(text = '1',size_hint = (None,None),size=("50dp","30dp"),pos=(100,100),
                                    multiline=False,foreground_color=(1,1,1,1),background_normal='',background_color=(0.2,0.2,0.2,1))
        apply_btn = Button(text='apply',size_hint = (None,None),size = ("75dp","40dp"),
                             background_normal='',background_color=(0,0.8,0.3,1),pos=(800,100),on_press = self.apply_clicked)
        
        threshold_layout.add_widget(self.threshold)
        threshold_layout.add_widget(apply_btn)
        threshold_layout.add_widget(self.times)

        

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
            self.increase_brightness_threshold = int(self.threshold.text)
        if (parameters.active_checkboxs[0] == 'decrease brightness'):
            self.decrease_brightness_threshold = int(self.threshold.text)
        if (parameters.active_checkboxs[0] == 'increase contrast'):
            self.increase_contrast_threshold = int(self.threshold.text)
        if (parameters.active_checkboxs[0] == 'decrease contrast'):
            self.decrease_contrast_threshold = int(self.threshold.text)

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
        if (len(parameters.active_checkboxs) > 1):
            parameters.active_checkboxs.pop(0)
            print(parameters.augment_process)
            self.screen_layout.clear_widgets()
            augmentViewerApp().stop()
            augmentViewerApp().run()
        else :
            pass
        
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
            
        cv2.imwrite("cache/output_img.jpg",sample_img)
            
        
if __name__ == '__main__':
    root = augmentSelectorApp()
    root.run()

