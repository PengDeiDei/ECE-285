# UCSD ECE-285
## Topic: Introduction to Visual Learning


## Porject: DCGAN on CelebA dataset
### User Brief Guide:
#### 1. CelebA dataset: 
Download link: https://drive.google.com/drive/folders/0B7EVK8r0v71pWEZsZE9oNnFzTm8?resourcekey=0-5BR16BdXnb8hVj6CNHKzLg

The package I downloaded is "img_align_celeba.zip", which contains .jpg version of images. It should be noticed that when user unzip this file, it creates a foler directly with all images, i.e. no subfolder.

#### 2. Project_DCGAN.ipynb
This is jupyter notebook of our DCGAN project containing the whole training process. 

Notice: the path of CelebA dataset folder defined in "datasets.ImageFolder()" function is weird. The path of the dataset should never be the path of folder which directly contains images. For example, if user store images in foler "dataset" whose path is "your_path/previous_folder/dataset", user should define the path as "your_path/previous_folder" to treat "dataset" folder as subfolder.

#### 3. DCGAN.py:
It is the architectures of discriminator and generator for DCGAN networks. 

#### 4. groupImg.py:
This is a script for copy a group of images with a specific feature from foler of CelebA dataset and transfer to a new folder defined by yourself.

User should edit this script before compiling it.

In this script, it contains four editable parameters that user needs to define: 
1) output_path, which is the path of output folder; 
2) image_path, the path of CelebA image folder;
3) CelebA_Attr_file, the path of "list_attr_celeba.txt" file;
4) Attr_type, the desired feature (attribute) that user wants to group images by. 

There are 40 attributes in CelebA dataset, which can be viewed in the "list_attr_celeba.txt" file. They are:
1) 5_o_Clock_Shadow (Newly grown cheek beard): 刚长出的双颊胡须
2) Arched_Eyebrows：柳叶眉
3) Attractive：吸引人的
4) Bags_Under_Eyes：眼袋
5) Bald：秃头
6) Bangs：刘海
7) Big_Lips：大嘴唇
8) Big_Nose：大鼻子
9) Black_Hair：黑发
10) Blond_Hair：金发
11) Blurry：模糊的
12) Brown_Hair：棕发
13) Bushy_Eyebrows：浓眉
14) Chubby：圆胖的
15) Double_Chin：双下巴
16) Eyeglasses：眼镜
17) Goatee：山羊胡子
18) Gray_Hair：灰发或白发
19) Heavy_Makeup：浓妆
20) High_Cheekbones：高颧骨
21) Male：男性
22) Mouth_Slightly_Open：微微张开嘴巴
23) Mustache：胡子，髭
24) Narrow_Eyes：细长的眼睛
25) No_Beard：无胡子
26) Oval_Face：椭圆形的脸
27) Pale_Skin：苍白的皮肤
28) Pointy_Nose：尖鼻子
29) Receding_Hairline：发际线后移
30) Rosy_Cheeks：红润的双颊
31) Sideburns：连鬓胡子
32) Smiling：微笑
33) Straight_Hair：直发
34) Wavy_Hair：卷发
35) Wearing_Earrings：戴着耳环
36) Wearing_Hat：戴着帽子
37) Wearing_Lipstick：涂了唇膏
38) Wearing_Necklace：戴着项链
39) Wearing_Necktie：戴着领带
40) Young：年轻人
