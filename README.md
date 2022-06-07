# UCSD ECE-285
## Topic: Introduction to Visual Learning


# Porject: DCGAN on CelebA dataset
### User Brief Guide:
#### 1. CelebA dataset: 
Download link: https://drive.google.com/drive/folders/0B7EVK8r0v71pWEZsZE9oNnFzTm8?resourcekey=0-5BR16BdXnb8hVj6CNHKzLg

The package I downloaded is "img_align_celeba.zip", which contains .jpg version of images.
It should be noticed that when user unzip this file, it creates a foler directly with all images, i.e. no subfolder.

#### 2. DCGAN.py:
It is the architectures of discriminator and generator for DCGAN networks. 

#### 3. groupImg.py:
This is a script for copy a group of images with a specific feature from foler of CelebA dataset and transfer to a new folder defined by yourself.
User should edit this script before compiling it. 
In this script, it contains four editable parameters: "output_path", "image_path", "CelebA_Attr_file", "Attr_type".
