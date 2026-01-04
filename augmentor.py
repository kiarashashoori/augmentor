import os
from pathlib import Path
import shutil
import cv2
import numpy as np

class augmentor():
    def __init__(self,input_img_path,input_label_path,output_img_path,output_label_path,times):
        self.input_img_path = input_img_path
        self.input_label_path = input_label_path
        self.output_img_path = output_img_path
        self.output_label_path = output_label_path
        self.times = times


class brightnessIncreasedAugmentor(augmentor):
    def __init__(self, input_img_path, input_label_path, output_img_path, output_label_path,times,brightness_threshold):
        super().__init__(input_img_path, input_label_path, output_img_path, output_label_path,times)
        self.brightness_threshold = brightness_threshold

    def action(self):
        label_filename_list = os.listdir(self.input_label_path)
        img_filename_list = os.listdir(self.input_img_path)
        
        for filename in label_filename_list:
            if filename.endswith(".txt"):
                for i in range(self.times):
                    label_output_filename = "BRI_"+ f"{i}_" + filename
                    label_output_path = os.path.join(self.output_label_path , label_output_filename)
                    shutil.copy2(os.path.join(self.input_label_path,filename),label_output_path)

        for filename in img_filename_list:
            if filename.endswith(".jpg"):
                img = cv2.imread(os.path.join(self.input_img_path,filename))
                for i in range(self.times):
                    brightness_factor = np.random.randint(10,self.brightness_threshold)
                    augmented_image = cv2.convertScaleAbs(img, alpha=1, beta=brightness_factor)
                    img_output_filename = "BRI_" + f"{i}_" + filename
                    img_output_path = os.path.join(self.output_img_path,img_output_filename)
                    cv2.imwrite(img_output_path,augmented_image)

        
        
class brightnessDecreasedAugmentor(augmentor):
    def __init__(self, input_img_path, input_label_path, output_img_path, output_label_path,times,brightness_threshold):
        super().__init__(input_img_path, input_label_path, output_img_path, output_label_path,times)
        self.brightness_threshold = brightness_threshold

    def action(self):
        label_filename_list = os.listdir(self.input_label_path)
        img_filename_list = os.listdir(self.input_img_path)
        for filename in label_filename_list:
            if filename.endswith(".txt"):
                for i in range(self.times):
                    label_output_filename = "BRD_"+ f"{i}_" + filename
                    label_output_path = os.path.join(self.output_label_path , label_output_filename)
                    shutil.copy2(os.path.join(self.input_label_path,filename),label_output_path)
            
        for filename in img_filename_list:
            if filename.endswith(".jpg"):
                img = cv2.imread(os.path.join(self.input_img_path,filename))
                for i in range(self.times):
                    brightness_factor = np.random.randint(-1 * self.brightness_threshold , -10)
                    augmented_image = cv2.convertScaleAbs(img, alpha=1, beta=brightness_factor)
                    img_output_filename = "BRD_" + f"{i}_" + filename
                    img_output_path = os.path.join(self.output_img_path,img_output_filename)
                    cv2.imwrite(img_output_path,augmented_image)


class contrastIncreasedAugmentor(augmentor):
    def __init__(self, input_img_path, input_label_path, output_img_path, output_label_path,times,contrast_threshold):
        super().__init__(input_img_path, input_label_path, output_img_path, output_label_path,times)
        self.contrast_threshold = contrast_threshold

    def action(self):
        label_filename_list = os.listdir(self.input_label_path)
        img_filename_list = os.listdir(self.input_img_path)
        
        for filename in label_filename_list:
            if filename.endswith(".txt"):
                for i in range(self.times):
                    label_output_filename = "CNI_"+ f"{i}_" + filename
                    label_output_path = os.path.join(self.output_label_path , label_output_filename)
                    shutil.copy2(os.path.join(self.input_label_path,filename),label_output_path)

        for filename in img_filename_list:
            if filename.endswith(".jpg"):
                img = cv2.imread(os.path.join(self.input_img_path,filename))
                for i in range(self.times):
                    contrast_factor = np.random.randint(5,self.contrast_threshold)
                    augmented_image = cv2.convertScaleAbs(img, alpha=1+(contrast_factor/100), beta=0)
                    img_output_filename = "CNI_" + f"{i}_" + filename
                    img_output_path = os.path.join(self.output_img_path,img_output_filename)
                    cv2.imwrite(img_output_path,augmented_image)

class contrastDecreasedAugmentor(augmentor):
    def __init__(self, input_img_path, input_label_path, output_img_path, output_label_path,times,contrast_threshold):
        super().__init__(input_img_path, input_label_path, output_img_path, output_label_path,times)
        self.contrast_threshold = contrast_threshold

    def action(self):
        label_filename_list = os.listdir(self.input_label_path)
        img_filename_list = os.listdir(self.input_img_path)
        for filename in label_filename_list:
            if filename.endswith(".txt"):
                for i in range(self.times):
                    label_output_filename = "CND_"+ f"{i}_" + filename
                    label_output_path = os.path.join(self.output_label_path , label_output_filename)
                    shutil.copy2(os.path.join(self.input_label_path,filename),label_output_path)
        
        for filename in img_filename_list:
            if filename.endswith(".jpg"):
                img = cv2.imread(os.path.join(self.input_img_path,filename))
                for i in range(self.times):
                    contrast_factor = np.random.randint(5,self.contrast_threshold)
                    augmented_image = cv2.convertScaleAbs(img, alpha=1-(contrast_factor/100), beta=0)
                    img_output_filename = "CND_" + f"{i}_" + filename
                    img_output_path = os.path.join(self.output_img_path,img_output_filename)
                    cv2.imwrite(img_output_path,augmented_image)
        

class flippedAugmentor(augmentor):
    def __init__(self, input_img_path, input_label_path, output_img_path, output_label_path):
        super().__init__(input_img_path, input_label_path, output_img_path, output_label_path)
    def action(self):
        pass

class saturationAugmentor(augmentor):
    def __init__(self, input_img_path, input_label_path, output_img_path, output_label_path,saturation_threshold):
        super().__init__(input_img_path, input_label_path, output_img_path, output_label_path)
        self.saturation_threshold = saturation_threshold
    def action(self):
        pass

class saltAugmentor(augmentor):
    def __init__(self, input_img_path, input_label_path, output_img_path, output_label_path,noise):
        super().__init__(input_img_path, input_label_path, output_img_path, output_label_path)
        self.noise = noise
    def action(self):
        pass

class pepperAugmentor(augmentor):
    def __init__(self, input_img_path, input_label_path, output_img_path, output_label_path,noise):
        super().__init__(input_img_path, input_label_path, output_img_path, output_label_path)
        self.noise = noise
    def action(self):
        pass