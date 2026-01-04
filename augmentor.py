import os
from pathlib import Path
import shutil
import cv2
import numpy as np
import random

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
    
class saturationIncreasedAugmentor(augmentor):
    def __init__(self, input_img_path, input_label_path, output_img_path, output_label_path,times,saturation_threshold):
        super().__init__(input_img_path, input_label_path, output_img_path, output_label_path,times)
        self.saturation_threshold = saturation_threshold

    def action(self):
        label_filename_list = os.listdir(self.input_label_path)
        img_filename_list = os.listdir(self.input_img_path)
        for filename in label_filename_list:
            if filename.endswith(".txt"):
                for i in range(self.times):
                    label_output_filename = "SAI_"+ f"{i}_" + filename
                    label_output_path = os.path.join(self.output_label_path , label_output_filename)
                    shutil.copy2(os.path.join(self.input_label_path,filename),label_output_path)
        
        for filename in img_filename_list:
            if filename.endswith(".jpg"):
                img = cv2.imread(os.path.join(self.input_img_path,filename))
                hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
                s_channel = hsv[:,:,1]
                for i in range(self.times):
                    s = s_channel
                    hsv_copy = hsv
                    saturation_factor = np.random.randint(5,self.saturation_threshold)
                    s += saturation_factor
                    hsv_copy [:,:,1] = s
                    augmented_image = cv2.cvtColor(hsv_copy,cv2.COLOR_HSV2BGR)
                    img_output_filename = "SAI_" + f"{i}_" + filename
                    img_output_path = os.path.join(self.output_img_path,img_output_filename)
                    cv2.imwrite(img_output_path,augmented_image)

class saturationDecreasedAugmentor(augmentor):
    def __init__(self, input_img_path, input_label_path, output_img_path, output_label_path,times,saturation_threshold):
        super().__init__(input_img_path, input_label_path, output_img_path, output_label_path,times)
        self.saturation_threshold = saturation_threshold

    def action(self):
        label_filename_list = os.listdir(self.input_label_path)
        img_filename_list = os.listdir(self.input_img_path)
        for filename in label_filename_list:
            if filename.endswith(".txt"):
                for i in range(self.times):
                    label_output_filename = "SAD_"+ f"{i}_" + filename
                    label_output_path = os.path.join(self.output_label_path , label_output_filename)
                    shutil.copy2(os.path.join(self.input_label_path,filename),label_output_path)
        
        for filename in img_filename_list:
            if filename.endswith(".jpg"):
                img = cv2.imread(os.path.join(self.input_img_path,filename))
                hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
                s_channel = hsv[:,:,1]
                for i in range(self.times):
                    s = s_channel
                    hsv_copy = hsv
                    saturation_factor = np.random.randint(5,self.saturation_threshold)
                    s -= saturation_factor
                    hsv_copy [:,:,1] = s
                    augmented_image = cv2.cvtColor(hsv_copy,cv2.COLOR_HSV2BGR)
                    img_output_filename = "SAD_" + f"{i}_" + filename
                    img_output_path = os.path.join(self.output_img_path,img_output_filename)
                    cv2.imwrite(img_output_path,augmented_image)


class salt_and_pepperAugmentor(augmentor):
    def __init__(self, input_img_path, input_label_path, output_img_path, output_label_path, times,noise_max):
        super().__init__(input_img_path, input_label_path, output_img_path, output_label_path, times)
        self.noise_max = noise_max
    def action(self):
        label_filename_list = os.listdir(self.input_label_path)
        img_filename_list = os.listdir(self.input_img_path)
        for filename in label_filename_list:
            if filename.endswith(".txt"):
                for i in range(self.times):
                    label_output_filename = "SP_"+ f"{i}_" + filename
                    label_output_path = os.path.join(self.output_label_path , label_output_filename)
                    shutil.copy2(os.path.join(self.input_label_path,filename),label_output_path)
        
        for filename in img_filename_list:
            if filename.endswith(".jpg"):
                img = cv2.imread(os.path.join(self.input_img_path,filename))
                
                for i in range(self.times):
                    noise = random.randint(20,self.noise_max)
                    noisy_image = img.copy()
                    noise /= 1000
                    salt_prob = noise / 2
                    pepper_prob = noise / 2
                    salt_mask = np.random.random(img.shape[:2]) < salt_prob
                    noisy_image[salt_mask] = 255
                    pepper_mask = np.random.random(img.shape[:2]) < pepper_prob
                    noisy_image[pepper_mask] = 0
                    img_output_filename = "SP_" + f"{i}_" + filename
                    img_output_path = os.path.join(self.output_img_path,img_output_filename)
                    cv2.imwrite(img_output_path,noisy_image)

class blurAugmentor(augmentor):
    def __init__(self, input_img_path, input_label_path, output_img_path, output_label_path, times,ksize):
        super().__init__(input_img_path, input_label_path, output_img_path, output_label_path, times)
        self.ksize = ksize

    def action(self):
        label_filename_list = os.listdir(self.input_label_path)
        img_filename_list = os.listdir(self.input_img_path)
        for filename in label_filename_list:
            if filename.endswith(".txt"):
                for i in range(self.times):
                    label_output_filename = "BLR_"+ f"{i}_" + filename
                    label_output_path = os.path.join(self.output_label_path , label_output_filename)
                    shutil.copy2(os.path.join(self.input_label_path,filename),label_output_path)
        for filename in img_filename_list:
            if filename.endswith(".jpg"):
                img = cv2.imread(os.path.join(self.input_img_path,filename))
                for i in range(self.times):
                    img_copy = img.copy()
                    img_copy = cv2.blur(img_copy,(self.ksize,self.ksize))
                    img_output_filename = "BLR_" + f"{i}_" + filename
                    img_output_path = os.path.join(self.output_img_path,img_output_filename)
                    cv2.imwrite(img_output_path,img_copy)


class shakeBlurAugmentor(augmentor):
    def __init__(self, input_img_path, input_label_path, output_img_path, output_label_path, times):
        super().__init__(input_img_path, input_label_path, output_img_path, output_label_path, times)

class shadowAugmentor(augmentor):
    def __init__(self, input_img_path, input_label_path, output_img_path, output_label_path, times):
        super().__init__(input_img_path, input_label_path, output_img_path, output_label_path, times)

class sunlightAugmentor(augmentor):
    def __init__(self, input_img_path, input_label_path, output_img_path, output_label_path, times):
        super().__init__(input_img_path, input_label_path, output_img_path, output_label_path, times)

class flippedAugmentor(augmentor):
    def __init__(self, input_img_path, input_label_path, output_img_path, output_label_path):
        super().__init__(input_img_path, input_label_path, output_img_path, output_label_path)
    def action(self):
        pass

class rotateAugmentor(augmentor):
    def __init__(self, input_img_path, input_label_path, output_img_path, output_label_path, times):
        super().__init__(input_img_path, input_label_path, output_img_path, output_label_path, times)

class hueAugmentor (augmentor):
    def __init__(self, input_img_path, input_label_path, output_img_path, output_label_path, times):
        super().__init__(input_img_path, input_label_path, output_img_path, output_label_path, times)
