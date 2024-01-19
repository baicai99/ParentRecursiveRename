import os

def is_name_conform(name, parent_path):
    """
    检查名称是否已符合目录层级格式
    """
    if parent_path:
        return name.startswith(parent_path + "_")
    return True

def rename_files_and_folders(directory_path, parent_path=""):
    # 获取当前目录的基本名称
    current_dir_name = os.path.basename(directory_path)

    # 如果当前目录不是根目录，则更新父路径
    if parent_path:
        parent_path = f"{parent_path}_{current_dir_name}"
    else:
        parent_path = current_dir_name

    # 遍历目录中的每个项目
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        
        # 处理子目录
        if os.path.isdir(item_path):
            if not is_name_conform(os.path.basename(item_path), parent_path):
                rename_files_and_folders(item_path, parent_path)

        # 处理文件
        elif os.path.isfile(item_path):
            if not is_name_conform(item, parent_path):
                new_file_name = f"{parent_path}_{item}"
                new_file_path = os.path.join(directory_path, new_file_name)
                os.rename(item_path, new_file_path)
                print(f"重命名文件：{item_path} -> {new_file_path}")

    # 重命名当前目录（除非它是根目录）
    if directory_path != os.path.join(os.getcwd(), current_dir_name) and not is_name_conform(current_dir_name, parent_path):
        new_directory_path = os.path.join(os.path.dirname(directory_path), parent_path)
        os.rename(directory_path, new_directory_path)
        print(f"重命名目录：{directory_path} -> {new_directory_path}")

if __name__ == "__main__":
    directory_path = input("请输入文件夹地址：").replace("'", "")  # 删除输入地址中的单引号
    rename_files_and_folders(directory_path)
