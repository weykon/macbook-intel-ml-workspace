import os
from PIL import Image

def check_images(directory):
    for filename in os.listdir(directory):
        print(filename)
        if filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg'):
            try:
                img = Image.open(os.path.join(directory, filename)) # 打开图像文件
                img.verify() # 验证图像的完整性
            except (IOError, SyntaxError) as e:
                print('Bad file:', filename) # 输出损坏的文件名

# 使用函数检查 "PetImages" 目录
check_images("PetImages/Cat")
check_images("PetImages/Dog")
