import os

def get_folder_size(folder_path):
    """获取目录大小"""
    size = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            size += os.path.getsize(file_path)
    return size

def get_largest_files(folder_path, num_files):
    """获取最大的几个文件"""
    file_sizes = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            file_sizes.append((file_path, file_size))
    file_sizes.sort(key=lambda x: x[1], reverse=True)
    for i in range(min(num_files, len(file_sizes))):
        print(f"{file_sizes[i][0]} - {format_size(file_sizes[i][1])}")

def print_folder_sizes(folder_path):
    """显示各层目录的文件大小"""
    for root, dirs, files in os.walk(folder_path):
        size = get_folder_size(root)
        print(f"{root} - {format_size(size)}")

def format_size(size):
    """将文件大小格式化为易读的字符串"""
    for unit in ["bytes", "KB", "MB", "GB"]:
        if size < 1024.0:
            return f"{size:.2f} {unit}"
        size /= 1024.0
    return f"{size:.2f} TB"

if __name__ == "__main__":
    folder_path = r"C:\Users\oceanstellar\Desktop\工作\看matlab代码\backup"
    num_files = 5
    print_folder_sizes(folder_path)
    print(f"\nTop {num_files} largest files:")
    get_largest_files(folder_path, num_files)