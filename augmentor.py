import os
from pathlib import Path
import shutil
import cv2
import numpy as np
import random
import threading

class augmentor():
    def __init__(self,input_img_path,input_label_path,output_img_path,output_label_path,times,augment_type):
        self.input_img_path = input_img_path
        self.input_label_path = input_label_path
        self.output_img_path = output_img_path
        self.output_label_path = output_label_path
        self.times = times
        self.augment_type = augment_type
    
    def action(self,threshold=50):
###################################################################################################
###            BRIGHTNESS AUGMENT               ###
        if self.augment_type == 'increase brightness':
            ###copy and paste the labels###
            label_filename_list = os.listdir(self.input_label_path)
            for filename in label_filename_list:
                if filename.endswith(".txt"):
                    for i in range(self.times):
                        label_output_filename = "BRI_"+ f"{i}_" + filename
                        label_output_path = os.path.join(self.output_label_path , label_output_filename)
                        shutil.copy2(os.path.join(self.input_label_path,filename),label_output_path)
            ###augment the image###
            img_filename_list = os.listdir(self.input_img_path)
            for filename in img_filename_list:
                if filename.endswith(".jpg"):
                    img = cv2.imread(os.path.join(self.input_img_path,filename))
                    for i in range(self.times):
                        img_output_filename = "BRI_" + f"{i}_" + filename
                        img_output_path = os.path.join(self.output_img_path,img_output_filename)
                        augmented_image = augmentor.brightnessIncreasedAugmentor(img,threshold,'augment')
                        cv2.imwrite(img_output_path,augmented_image)
        
        if self.augment_type == 'decrease brightness':
            ###copy and paste the labels###
            label_filename_list = os.listdir(self.input_label_path)
            for filename in label_filename_list:
                if filename.endswith(".txt"):
                    for i in range(self.times):
                        label_output_filename = "BRD_"+ f"{i}_" + filename
                        label_output_path = os.path.join(self.output_label_path , label_output_filename)
                        shutil.copy2(os.path.join(self.input_label_path,filename),label_output_path)
            ###augment the image###
            img_filename_list = os.listdir(self.input_img_path)
            for filename in img_filename_list:
                if filename.endswith(".jpg"):
                    img = cv2.imread(os.path.join(self.input_img_path,filename))
                    for i in range(self.times):
                        img_output_filename = "BRD_" + f"{i}_" + filename
                        img_output_path = os.path.join(self.output_img_path,img_output_filename)
                        augmented_image = augmentor.brightnessDecreasedAugmentor(img,threshold,'augment')
                        cv2.imwrite(img_output_path,augmented_image)

###################################################################################################
###            CONTRAST AUGMENT               ###

        if self.augment_type == 'decrease contrast':
            ###copy and paste the labels###
            label_filename_list = os.listdir(self.input_label_path)
            for filename in label_filename_list:
                if filename.endswith(".txt"):
                    for i in range(self.times):
                        label_output_filename = "CND_"+ f"{i}_" + filename
                        label_output_path = os.path.join(self.output_label_path , label_output_filename)
                        shutil.copy2(os.path.join(self.input_label_path,filename),label_output_path)
            ###augment the image###
            img_filename_list = os.listdir(self.input_img_path)
            for filename in img_filename_list:
                if filename.endswith(".jpg"):
                    img = cv2.imread(os.path.join(self.input_img_path,filename))
                    for i in range(self.times):
                        img_output_filename = "CND_" + f"{i}_" + filename
                        img_output_path = os.path.join(self.output_img_path,img_output_filename)
                        augmented_image = augmentor.contrastDecreasedAugmentor(img,threshold,'augment')
                        cv2.imwrite(img_output_path,augmented_image)
        if self.augment_type == 'increase contrast':
            ###copy and paste the labels###
            label_filename_list = os.listdir(self.input_label_path)
            for filename in label_filename_list:
                if filename.endswith(".txt"):
                    for i in range(self.times):
                        label_output_filename = "CNI_"+ f"{i}_" + filename
                        label_output_path = os.path.join(self.output_label_path , label_output_filename)
                        shutil.copy2(os.path.join(self.input_label_path,filename),label_output_path)
            ###augment the image###
            img_filename_list = os.listdir(self.input_img_path)
            for filename in img_filename_list:
                if filename.endswith(".jpg"):
                    img = cv2.imread(os.path.join(self.input_img_path,filename))
                    for i in range(self.times):
                        img_output_filename = "CNI_" + f"{i}_" + filename
                        img_output_path = os.path.join(self.output_img_path,img_output_filename)
                        augmented_image = augmentor.contrastIncreasedAugmentor(img,threshold,'augment')
                        cv2.imwrite(img_output_path,augmented_image)

###################################################################################################
###            SATURATION AUGMENT               ###

        if self.augment_type == 'decrease saturation':
            ###copy and paste the labels###
            label_filename_list = os.listdir(self.input_label_path)
            for filename in label_filename_list:
                if filename.endswith(".txt"):
                    for i in range(self.times):
                        label_output_filename = "SAD_"+ f"{i}_" + filename
                        label_output_path = os.path.join(self.output_label_path , label_output_filename)
                        shutil.copy2(os.path.join(self.input_label_path,filename),label_output_path)
            ###augment the image###
            img_filename_list = os.listdir(self.input_img_path)
            for filename in img_filename_list:
                if filename.endswith(".jpg"):
                    img = cv2.imread(os.path.join(self.input_img_path,filename))
                    for i in range(self.times):
                        img_output_filename = "SAD_" + f"{i}_" + filename
                        img_output_path = os.path.join(self.output_img_path,img_output_filename)
                        augmented_image = augmentor.saturationDecreasedAugmentor(img,threshold,'augment')
                        cv2.imwrite(img_output_path,augmented_image)
        if self.augment_type == 'increase saturation':
            ###copy and paste the labels###
            label_filename_list = os.listdir(self.input_label_path)
            for filename in label_filename_list:
                if filename.endswith(".txt"):
                    for i in range(self.times):
                        label_output_filename = "SAI_"+ f"{i}_" + filename
                        label_output_path = os.path.join(self.output_label_path , label_output_filename)
                        shutil.copy2(os.path.join(self.input_label_path,filename),label_output_path)
            ###augment the image###
            img_filename_list = os.listdir(self.input_img_path)
            for filename in img_filename_list:
                if filename.endswith(".jpg"):
                    img = cv2.imread(os.path.join(self.input_img_path,filename))
                    for i in range(self.times):
                        img_output_filename = "SAI_" + f"{i}_" + filename
                        img_output_path = os.path.join(self.output_img_path,img_output_filename)
                        augmented_image = augmentor.saturationIncreasedAugmentor(img,threshold,'augment')
                        cv2.imwrite(img_output_path,augmented_image)  

###################################################################################################
###            SALT & PEPPER AUGMENT               ###        
                   
        if self.augment_type == 'salt&pepper':
            ###copy and paste the labels###
            label_filename_list = os.listdir(self.input_label_path)
            for filename in label_filename_list:
                if filename.endswith(".txt"):
                    for i in range(self.times):
                        label_output_filename = "SP_"+ f"{i}_" + filename
                        label_output_path = os.path.join(self.output_label_path , label_output_filename)
                        shutil.copy2(os.path.join(self.input_label_path,filename),label_output_path)
            ###augment the image###
            img_filename_list = os.listdir(self.input_img_path)
            for filename in img_filename_list:
                if filename.endswith(".jpg"):
                    img = cv2.imread(os.path.join(self.input_img_path,filename))
                    for i in range(self.times):
                        img_output_filename = "SP_" + f"{i}_" + filename
                        img_output_path = os.path.join(self.output_img_path,img_output_filename)
                        augmented_image = augmentor.saltPepperAugmentor(img,threshold,'augment')
                        cv2.imwrite(img_output_path,augmented_image)   

###################################################################################################
###            BlUR AUGMENT               ###    
        if self.augment_type == 'blur':
            ###copy and paste the labels###
            label_filename_list = os.listdir(self.input_label_path)
            for filename in label_filename_list:
                if filename.endswith(".txt"):
                    label_output_filename = "BLR_"+ filename
                    label_output_path = os.path.join(self.output_label_path , label_output_filename)
                    shutil.copy2(os.path.join(self.input_label_path,filename),label_output_path)
            ###augment the image###
            img_filename_list = os.listdir(self.input_img_path)
            for filename in img_filename_list:
                if filename.endswith(".jpg"):
                    img = cv2.imread(os.path.join(self.input_img_path,filename))
                    img_output_filename = "BLR_" + filename
                    img_output_path = os.path.join(self.output_img_path,img_output_filename)
                    augmented_image = augmentor.blurAugmentor(img,threshold,'augment')
                    cv2.imwrite(img_output_path,augmented_image)    

                
    @staticmethod
    def brightnessIncreasedAugmentor(img,brightness_threshold,mode):
        if mode == 'augment':
            brightness_factor = np.random.randint(10,brightness_threshold)
            augmented_image = cv2.convertScaleAbs(img, alpha=1, beta=brightness_factor)
        elif mode == 'sample':
            augmented_image = cv2.convertScaleAbs(img, alpha=1, beta=brightness_threshold)
        return augmented_image
    @staticmethod
    def brightnessDecreasedAugmentor(img,brightness_threshold,mode):
        if mode == 'augment':
            brightness_factor = np.random.randint(-1 * brightness_threshold,-10)
            augmented_image = cv2.convertScaleAbs(img, alpha=1, beta=brightness_factor)
        elif mode == 'sample':
            augmented_image = cv2.convertScaleAbs(img, alpha=1, beta=-1 * brightness_threshold)
        return augmented_image
    @staticmethod
    def contrastIncreasedAugmentor(img,contrast_threshold,mode):
        if mode == 'augment':
            contrast_factor = np.random.randint(5,contrast_threshold)
            augmented_image = cv2.convertScaleAbs(img, alpha=1+(contrast_factor/100), beta=0)
        elif mode == 'sample':
            augmented_image = cv2.convertScaleAbs(img, alpha=1+(contrast_threshold/100), beta=0)
        return augmented_image
    @staticmethod
    def contrastDecreasedAugmentor(img,contrast_threshold,mode):
        if mode == 'augment':
            contrast_factor = np.random.randint(5,contrast_threshold)
            augmented_image = cv2.convertScaleAbs(img, alpha=1-(contrast_factor/100), beta=0)
        elif mode == 'sample':
            augmented_image = cv2.convertScaleAbs(img, alpha=1-(contrast_threshold/100), beta=0)
        return augmented_image
    @staticmethod
    def saturationIncreasedAugmentor(img,saturation_threshold,mode):
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        s_channel = hsv[:,:,1]
        s = s_channel
        hsv_copy = hsv
        if mode == 'augment':
            saturation_factor = np.random.randint(5,saturation_threshold)
            s += saturation_factor
            hsv_copy [:,:,1] = s
        if mode == 'sample':
            s += saturation_threshold
            hsv_copy [:,:,1] = s
        augmented_image = cv2.cvtColor(hsv_copy,cv2.COLOR_HSV2BGR)
        return augmented_image
    @staticmethod
    def saturationDecreasedAugmentor(img,saturation_threshold,mode):
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        s_channel = hsv[:,:,1]
        s = s_channel
        hsv_copy = hsv
        if mode == 'augment':
            saturation_factor = np.random.randint(5,saturation_threshold)
            s -= saturation_factor
            hsv_copy [:,:,1] = s
        if mode == 'sample':
            s -= saturation_threshold
            hsv_copy [:,:,1] = s
        augmented_image = cv2.cvtColor(hsv_copy,cv2.COLOR_HSV2BGR)
        return augmented_image
    @staticmethod
    def saltPepperAugmentor(img,noise_level,mode):
        if mode == 'augment':
            noise = random.randint(10,noise_level)  
        elif mode == 'sample':
            noise = noise_level
        augmented_image = img
        noise /= 1000
        salt_prob = noise / 2
        pepper_prob = noise / 2
        salt_mask = np.random.random(img.shape[:2]) < salt_prob
        augmented_image[salt_mask] = 255
        pepper_mask = np.random.random(img.shape[:2]) < pepper_prob
        augmented_image[pepper_mask] = 0

        return augmented_image
    @staticmethod 
    def blurAugmentor(img,threshold,_):
        augmented_image = cv2.blur(img,(threshold,threshold))
        return augmented_image

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

class shakeVerticalBlurAugmentor(augmentor):
    def __init__(self, input_img_path, input_label_path, output_img_path, output_label_path, times):
        super().__init__(input_img_path, input_label_path, output_img_path, output_label_path, times)
    
    def action(self):
        kernel_size = 25
        img = cv2.imread('cache/input_img.jpg')
        # Create the vertical kernel.
        kernel_v = np.zeros((kernel_size, kernel_size))

        # Fill the middle row with ones.
        kernel_v[:, int((kernel_size - 1)/2)] = np.ones(kernel_size)

        # Normalize.
        kernel_v /= kernel_size

        # Apply the vertical kernel.
        vertical_mb = cv2.filter2D(img, -1, kernel_v)

        # Save the outputs.
        # cv2.imwrite('car_vertical.jpg', vertical_mb)
        # cv2.imwrite('car_horizontal.jpg', horizonal_mb)

class shakeHorizentalBlurAugmentor(augmentor):
    def __init__(self, input_img_path, input_label_path, output_img_path, output_label_path, times):
        super().__init__(input_img_path, input_label_path, output_img_path, output_label_path, times)
    
    def action(self):
        kernel_size = 25
        img = cv2.imread('cache/input_img.jpg')
        # Create the vertical kernel.
        kernel_h = np.zeros((kernel_size, kernel_size))
        kernel_h[int((kernel_size - 1)/2), :] = np.ones(kernel_size)

        # Normalize.
        kernel_h /= kernel_size

        # Apply the horizontal kernel.
        horizonal_mb = cv2.filter2D(img, -1, kernel_h)
        
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


class augmentorTest(augmentor):
    def __init__(self, input_img_path, input_label_path, output_img_path, output_label_path, times):
        super().__init__(input_img_path, input_label_path, output_img_path, output_label_path, times)

# augmentorTest('','','','',None)