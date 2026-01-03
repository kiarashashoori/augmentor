class augmentor():
    def __init__(self,input_img_path,input_label_path,output_img_path,output_label_path):
        self.input_img_path = input_img_path
        self.input_label_path = input_label_path
        self.output_img_path = output_img_path
        self.output_label_path = output_label_path


class brightnessAugmentor(augmentor):
    def __init__(self, input_img_path, input_label_path, output_img_path, output_label_path,brightness_threshold):
        super().__init__(input_img_path, input_label_path, output_img_path, output_label_path)
        self.brightness_threshold = brightness_threshold
    def action(self):
        pass


class contrastAugmentor(augmentor):
    def __init__(self, input_img_path, input_label_path, output_img_path, output_label_path,contrast_threshold):
        super().__init__(input_img_path, input_label_path, output_img_path, output_label_path)
        self.contrast_threshold = contrast_threshold
    def action(self):
        pass

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