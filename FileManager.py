import os

class fileManager():
    def __init__(self, directory: str):
        self.directory = directory

def walkDirectory(directory: str):
    for root, dirs, files in os.walk(directory):
        # print("root", root)  # 当前目录路径
        # print("dirs", dirs)  # 当前路径下所有子目录
        # print("files", files)  # 当前路径下所有非目录子文件

        # 在输出文件夹生成相应的目录
        # for dir in dirs:
        #     outputDirectory = output_directory + '/' + dir
        #     createDirectory(outputDirectory)

        # 获取所有符合条件的子文件
        for file in files:
            filePath = root + '/' + file
            filePath = pathEncode(filePath)
            print(filePath)

def pathEncode(path: str) -> str:
    path = path.replace('(', '\(')
    path = path.replace(')', '\)')
    path = path.replace('[', '\[')
    path = path.replace(']', '\]')
    path = path.replace('?', '\?')
    return path


walkDirectory('/Users/harrycao/Desktop/output/周星驰合集')