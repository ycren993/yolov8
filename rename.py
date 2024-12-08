import os

# 设置文件夹路径
folder_path = 'D:\PythonFile\datasets\\UPRC2018Enhanced\labels\\val'

# 获取文件夹内文件列表
files = os.listdir(folder_path)

# 对每个文件进行重命名
for file in files:
    # 获取文件的扩展名
    file_name, file_extension = os.path.splitext(file)
    # 构建新的文件名
    new_file_name = f"{file_name}_fake_B{file_extension}"
    # 重命名文件
    os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_file_name))