import os
from PIL import Image

# 定义源文件夹和目标文件夹
source_folder = 'D:\PythonFile\datasets\\UPRC2018Enhanced\images\\val'
target_folder = 'D:\PythonFile\datasets\\UPRC2018Enhanced\images\\valA'

# 如果目标文件夹不存在，则创建
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

# 列出源文件夹中的所有PNG文件
for filename in os.listdir(source_folder):
    if filename.endswith('.png'):
        # 打开PNG文件
        image = Image.open(os.path.join(source_folder, filename))
        # 转换为JPG格式
        image.convert('RGB').save(os.path.join(target_folder, os.path.splitext(filename)[0] + '.jpg'), 'JPEG')