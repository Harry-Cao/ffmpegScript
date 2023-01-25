import os

def walkDirectory(directory: str) -> tuple:
    allDirectories: list[str] = []
    allFilePaths: list[str] = []
    for root, dirs, files in os.walk(directory):
        # print("root", root)  # 当前目录路径
        # print("dirs", dirs)  # 当前路径下所有子目录
        # print("files", files)  # 当前路径下所有非目录子文件

        # 在输出文件夹生成相应的目录
        for dir in dirs:
            directory = root + '/' + dir
            directory = pathEncode(directory)
            allDirectories.append(directory)
        # 获取所有符合条件的子文件
        for file in files:
            filePath = root + '/' + file
            filePath = pathEncode(filePath)
            allFilePaths.append(filePath)

    return (allDirectories, allFilePaths)

# string -> url friendly
def pathEncode(path: str) -> str:
    path = path.replace('(', '\(')
    path = path.replace(')', '\)')
    path = path.replace('[', '\[')
    path = path.replace(']', '\]')
    path = path.replace('?', '\?')
    return path

# 复制目录结构
def copyDirectory(inputDirectory: str, outputDirectory: str):
    resultTuple = walkDirectory(inputDirectory)
    directories: list[str] = resultTuple[0]
    for directory in directories:
        directory = directory.replace(inputDirectory, outputDirectory)
        createDirectory(directory)

def createDirectory(directory: str):
    if not os.path.exists(directory):
        os.mkdir(directory)


copyDirectory('/Users/harrycao/Desktop/YSCloud', '/Users/harrycao/Desktop/output')