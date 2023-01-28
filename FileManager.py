import os
from enum import Enum

class ConditionType(Enum):
    endInput = 0
    contain = 1
    notContain = 2
    allFile = 3

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


# copyDirectory('/Users/harrycao/Desktop/YSCloud', '/Users/harrycao/Desktop/output')


targetFiles: list[str] = []


def searchFiles(fileList: list[str]):
    condition = getCondition('请输入选择条件(0-完成输入 1-包含 2-不包含 3-所有文件): ')
    if condition == ConditionType.endInput:
        return
    elif condition == ConditionType.contain:
        pass
    elif condition == ConditionType.notContain:
        pass
    elif condition == ConditionType.allFile:
        pass
    print('搜索到符合条件的文件数:' + str(targetFiles.count))
    searchFiles(fileList)
    


def getCondition(request: str) -> ConditionType:
    input = input(request)
    inputNum = int(input)
    condition = ConditionType(inputNum)
    return condition