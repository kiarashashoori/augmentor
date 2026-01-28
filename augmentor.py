import os
from pathlib import Path
import shutil
import cv2
import numpy as np
import random
import parameters

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
                    
###################################################################################################
###            MOTION BLUR AUGMENT               ###   

        if self.augment_type == 'vertical motion blur':
            ###copy and paste the labels###
            label_filename_list = os.listdir(self.input_label_path)
            for filename in label_filename_list:
                if filename.endswith(".txt"):
                    label_output_filename = "VBLR_"+ filename
                    label_output_path = os.path.join(self.output_label_path , label_output_filename)
                    shutil.copy2(os.path.join(self.input_label_path,filename),label_output_path)
            ###augment the image###
            img_filename_list = os.listdir(self.input_img_path)
            for filename in img_filename_list:
                if filename.endswith(".jpg"):
                    img = cv2.imread(os.path.join(self.input_img_path,filename))
                    img_output_filename = "VBLR_" + filename
                    img_output_path = os.path.join(self.output_img_path,img_output_filename)
                    augmented_image = augmentor.shakeVerticalBlurAugmentor(img,threshold,'augment')
                    cv2.imwrite(img_output_path,augmented_image)
        
        if self.augment_type == 'horizontal motion blur':
            ###copy and paste the labels###
            label_filename_list = os.listdir(self.input_label_path)
            for filename in label_filename_list:
                if filename.endswith(".txt"):
                    label_output_filename = "HBLR_"+ filename
                    label_output_path = os.path.join(self.output_label_path , label_output_filename)
                    shutil.copy2(os.path.join(self.input_label_path,filename),label_output_path)
            ###augment the image###
            img_filename_list = os.listdir(self.input_img_path)
            for filename in img_filename_list:
                if filename.endswith(".jpg"):
                    img = cv2.imread(os.path.join(self.input_img_path,filename))
                    img_output_filename = "HBLR_" + filename
                    img_output_path = os.path.join(self.output_img_path,img_output_filename)
                    augmented_image = augmentor.shakeHorizontalBlurAugmentor(img,threshold,'augment')
                    cv2.imwrite(img_output_path,augmented_image)

###################################################################################################
###            FLIPPED AUGMENT               ###   
        if self.augment_type == 'flipped':
            label_filename_list = os.listdir(self.input_label_path)
            img_filename_list = os.listdir(self.input_img_path)
            for filename in label_filename_list:
                if filename.endswith('.txt') and ((filename[:len(filename)-4]+'.jpg') in img_filename_list):
                    with open(os.path.join(self.input_label_path,filename),'r') as f:
                        lines = f.readlines()
                    img = cv2.imread(os.path.join(self.input_img_path,((filename[:len(filename)-4]+'.jpg'))))
                    img_output_filename = "FLP_" + (filename[:len(filename)-4]+'.jpg')
                    img_output_path = os.path.join(self.output_img_path,img_output_filename)
                    augmented_image,augmented_label_list = augmentor.flippedAugmentor(img,lines,'augment') 
                    cv2.imwrite(img_output_path,augmented_image)
                    f.close()
                    label_output_filename = "FLP_"+ filename
                    label_output_path = os.path.join(self.output_label_path , label_output_filename)
                    with open(label_output_path,'w') as f:
                        f.writelines(augmented_label_list)
                    f.close()

###################################################################################################
###            ROTATE AUGMENT               ###   
        if self.augment_type == 'rotate':
            label_filename_list = os.listdir(self.input_label_path)
            img_filename_list = os.listdir(self.input_img_path)
            for filename in label_filename_list:
                if filename.endswith('.txt') and ((filename[:len(filename)-4]+'.jpg') in img_filename_list):
                    with open(os.path.join(self.input_label_path,filename),'r') as f:
                        lines = f.readlines()
                    img = cv2.imread(os.path.join(self.input_img_path,((filename[:len(filename)-4]+'.jpg'))))
                    img_output_filename = "ROT_" + (filename[:len(filename)-4]+'.jpg')
                    img_output_path = os.path.join(self.output_img_path,img_output_filename)
                    augmented_image,augmented_label_list = augmentor.rotateAugmentor(img,lines,threshold,'augment') 
                    cv2.imwrite(img_output_path,augmented_image)
                    f.close()
                    label_output_filename = "ROT_"+ filename
                    label_output_path = os.path.join(self.output_label_path , label_output_filename)
                    with open(label_output_path,'w') as f:
                        f.writelines(augmented_label_list)
                    f.close()



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
    @staticmethod
    def shakeVerticalBlurAugmentor(img,threshold,_):
        kernel_v = np.zeros((threshold, threshold))
        kernel_v[:, int((threshold - 1)/2)] = np.ones(threshold)
        kernel_v /= threshold
        augmented_image = cv2.filter2D(img, -1, kernel_v)
        return augmented_image
    @staticmethod
    def shakeHorizontalBlurAugmentor(img,threshold,_):
        kernel_h = np.zeros((threshold, threshold))
        kernel_h[int((threshold - 1)/2), :] = np.ones(threshold)
        kernel_h /= threshold
        augmented_image = cv2.filter2D(img, -1, kernel_h)
        return augmented_image
    @staticmethod
    def flippedAugmentor(img,label_content,mode):
        if mode == 'augment':
            augmented_image = cv2.flip(img,1)
            size = img.shape
            augmented_label_list = []
            if parameters.augmentor_mode == 'sign':
                for line in label_content:
                    augmented_label = ''
                    augmented_label += line.split()[0]
                    augmented_label += ' '
                    augmented_label += str(1 - float(line.split()[1]))
                    augmented_label += ' '
                    for content in line.split()[2:]:
                        augmented_label += content
                        augmented_label += ' '
                    augmented_label = augmented_label[:len(augmented_label)-1]
                    augmented_label += '\n'
                    augmented_label_list.append(augmented_label)
            
            if parameters.augmentor_mode == 'line':
                for line in label_content:
                    augmented_label = ''
                    line_content = line.split()
                    for i in range(len(line_content)):
                        if i % 2 == 0:
                            augmented_label += line_content[i]
                        else:
                            augmented_label += str(size[1] - float(line_content[i]))
                        augmented_label += ' '
                    augmented_label = augmented_label[:len(augmented_label)-1]
                    augmented_label += '\n'
                    augmented_label_list.append(augmented_label)
            return augmented_image,augmented_label_list
        if mode == 'sample':
            augmented_image = cv2.flip(img,1)
            return augmented_image
    @staticmethod
    def rotateAugmentor(img,label_content,angle,mode):
        if mode == 'sample':
            rotation_mat = cv2.getRotationMatrix2D((img.shape[1]//2,img.shape[0]//2),angle,1)
            augmented_image = cv2.warpAffine(img,rotation_mat,(img.shape[1],img.shape[0]))
            return augmented_image
        if mode == 'augment':
            rotation_mat = cv2.getRotationMatrix2D((img.shape[1]//2,img.shape[0]//2),angle,1)
            augmented_image = cv2.warpAffine(img,rotation_mat,(img.shape[1],img.shape[0]))
            size = img.shape
            augmented_label_list = []
            if parameters.augmentor_mode == 'sign':
                for line in label_content:
                    augmented_label = ''
                    line_content = line.split()
                    center_x,center_y = float(line_content[1]),float(line_content[2])
                    width,height = float(line_content[3]),float(line_content[4])
                    '''initial coordinates
                    x0y0-------------------x1y1
                      |                      |
                      |                      |
                      |                      |
                      |                      |
                      |                      |
                    x2y2-------------------x3y3 
                    '''
                    initial_x_coordinates = np.array([center_x-width/2,center_x+width/2,center_x-width/2,center_x+width/2])
                    initial_y_coordinates = np.array([center_y-height/2,center_y-height/2,center_y+height/2,center_y+height/2])

                    initial_x_coordinates = initial_x_coordinates - 0.5
                    initial_y_coordinates = initial_y_coordinates - 0.5

                    secondary_x_coordinates = (np.cos(np.radians(angle))*initial_x_coordinates)+(np.sin(np.radians(angle))*initial_y_coordinates)
                    secondary_y_coordinates = (np.cos(np.radians(angle))*initial_y_coordinates)-(np.sin(np.radians(angle))*initial_x_coordinates)

                    secondary_x_coordinates = secondary_x_coordinates + 0.5
                    secondary_y_coordinates = secondary_y_coordinates + 0.5

                    minimum_x = min(secondary_x_coordinates)
                    minimum_y = min(secondary_y_coordinates)
                    maximum_x = max(secondary_x_coordinates)
                    maximum_y = max(secondary_y_coordinates)


                    new_width,new_height = maximum_x - minimum_x,maximum_y-minimum_y
                    new_width += parameters.rotation_scale*new_width
                    new_height += parameters.rotation_scale*new_height
                    
                    miss_percentage = None
                    if maximum_x > 1 or maximum_y > 1 or minimum_x < 0 or minimum_y < 0 :
                        area = new_width * new_height
                        
                        if maximum_x > 1:
                            miss_area = (maximum_x-1) * new_height
                            maximum_x = 1
                            if miss_percentage == None:
                                miss_percentage = miss_area/area
                            else:
                                miss_percentage += miss_area/area
                        if maximum_y > 1:
                            miss_area = (maximum_y-1) * new_width
                            maximum_y = 1
                            if miss_percentage == None:
                                miss_percentage = miss_area/area
                            else:
                                miss_percentage += miss_area/area
                        if minimum_x < 0 :
                            miss_area = (0-minimum_x) * new_height
                            minimum_x = 0
                            if miss_percentage == None:
                                miss_percentage = miss_area/area
                            else:
                                miss_percentage += miss_area/area
                        if minimum_y < 0 :
                            miss_area = (0-minimum_y) * new_width
                            minimum_y = 0
                            if miss_percentage == None:
                                miss_percentage = miss_area/area
                            else:
                                miss_percentage += miss_area/area
                        new_width,new_height = maximum_x - minimum_x,maximum_y-minimum_y

                    new_center_x,new_center_y = minimum_x+new_width/2,minimum_y+new_height/2

                    if (miss_percentage == None or miss_percentage < 0.25):
                        augmented_label += line_content[0]
                        augmented_label += ' '
                        augmented_label += str(new_center_x)
                        augmented_label += ' '
                        augmented_label += str(new_center_y)
                        augmented_label += ' '
                        augmented_label += str(new_width)
                        augmented_label += ' '
                        augmented_label += str(new_height)
                        augmented_label += '\n'
                        augmented_label_list.append(augmented_label)


            return augmented_image,augmented_label_list



        
class shadowAugmentor(augmentor):
    def __init__(self, input_img_path, input_label_path, output_img_path, output_label_path, times):
        super().__init__(input_img_path, input_label_path, output_img_path, output_label_path, times)

class sunlightAugmentor(augmentor):
    def __init__(self, input_img_path, input_label_path, output_img_path, output_label_path, times):
        super().__init__(input_img_path, input_label_path, output_img_path, output_label_path, times)

class rotateAugmentor(augmentor):
    def __init__(self, input_img_path, input_label_path, output_img_path, output_label_path, times):
        super().__init__(input_img_path, input_label_path, output_img_path, output_label_path, times)

class hueAugmentor (augmentor):
    def __init__(self, input_img_path, input_label_path, output_img_path, output_label_path, times):
        super().__init__(input_img_path, input_label_path, output_img_path, output_label_path, times)