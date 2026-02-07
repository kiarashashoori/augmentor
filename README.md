# AurigaAugmentor

AurigaAugmentor is a Python-based GUI application developed by the AURIGA Robotics Team at Shahid Beheshti University. It is designed to efficiently augment, clean, and analyze image datasets for computer vision tasks, including line detection and traffic/sign detection.

## Features
### 1.Augment
Enhance your dataset with a wide range of image augmentations:
- Brightness: increase / decrease
- Contrast: increase / decrease
- Saturation: increase / decrease
- Noise: salt & pepper
- Blur: standard, vertical motion, horizontal motion
- Environmental effects: shadow, sunlight
- Geometric: rotate, flipped
- Color adjustments: hue
  
Multi-threaded processing ensures efficient augmentation for large datasets, with real-time progress updates.
### 2.Data Cleaner
Prepare your dataset for training by automatically:
- Removing images without proper labels
- Deleting irrelevant or corrupted images
- Producing a clean, ready-to-use dataset

### 3.Data Analysis (Coming Soon)
Planned features include:
- Dataset statistics (class distribution, image counts)
- Visualization of dataset diversity
- Recommendations for augmentations to balance your dataset

## Installation

1. Clone the repository:
```bash
git clone https://github.com/kiarashashoori/AurigaAugmentor.git
cd AurigaAugmentor
```

2. Install dependencies (Python 3.8+ recommended):

```bash
pip install kivy numpy pillow opencv-python
```

### Dependencies include:
- Kivy
- OpenCV (opencv-python)
- NumPy
- Pillow

## Note
Before running AurigaAugmentor, please make sure to:

1. Download the `Auriga.png` image and place it in the project folder.
2. Create a folder named `cache` in the project root (used for temporary processing).
3. We recommend that at first run data cleaner app over your dataset.

## Usage
1.Launch the application:
```markdown
python main.py
```
2.Select one of the three main modes:
- Augment – apply various image augmentations
- Data Cleaner – remove images without proper labels
- Data Analysis – explore dataset (coming soon)

3.Configure your dataset paths and augmentation parameters.

4.Start the process and watch the progress bar for real-time updates.

## Contributing

We welcome contributions from the community!

- Bug reports, feature requests, and pull requests are appreciated
- For major changes, open an issue first to discuss your idea

## License

This project is licensed under the MIT License – see the LICENSE file for details.

## Contact
### AURIGA Robotics Team – Shahid Beheshti University
### Project: AurigaAugmentor
For questions, collaboration, or suggestions, contact: [Ashoorikiarash8585@gmail.com]
