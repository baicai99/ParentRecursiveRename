import os

def rename_files_and_folders_recursively(directory_path):
    for root, dirs, files in os.walk(directory_path, topdown=False):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            
            # 获取文件的父级目录名称
            parent_dir = os.path.basename(root)

            # 构建新的文件名，将父级目录名称添加到文件名前面，以"_"分隔
            new_file_name = f"{parent_dir}_{file_name}"

            # 构建新的文件路径
            new_file_path = os.path.join(root, new_file_name)

            # 重命名文件
            os.rename(file_path, new_file_path)
            print(f"重命名文件：{file_path} -> {new_file_path}")

        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)

            # 获取父级目录的名称
            parent_dir = os.path.basename(root)

            # 去除单引号符号并构建新的目录名，递归地包含之前的父级目录名称
            dir_name_without_quotes = dir_name.replace("'", "")
            new_dir_name = f"{parent_dir}_{dir_name_without_quotes}"

            # 构建新的目录路径
            new_dir_path = os.path.join(root, new_dir_name)

            # 重命名目录
            os.rename(dir_path, new_dir_path)
            print(f"重命名目录：{dir_path} -> {new_dir_path}")

            # 递归调用函数，处理新的目录
            rename_files_and_folders_recursively(new_dir_path)

if __name__ == "__main__":
    # 使用input函数询问用户输入文件夹地址，然后过滤掉单引号
    directory_path = input("请输入文件夹地址：").replace("'", "")
    rename_files_and_folders_recursively(directory_path)
