import os
import time
import sys
from enum import Enum


class FileType(Enum):
    mkv = 1
    mp4 = 2
    rmvb = 3
    gif = 4

input_directory = '/Users/harrycao/Desktop/input/周星驰合集/家有喜事'
output_directory = '/Users/harrycao/Desktop/output'
inputType = FileType.mkv
outputType = FileType.mp4

# 目录下级所有文件名
# def fileNamesFromDirectory(directory: str) -> list[str]:
#     return os.listdir(directory)

# 获取所有符合条件的子文件
def inputPathsFromDirectory(directory: str) -> list[str]:
    inputFilePaths: list[str] = []
    for root, dirs, files in os.walk(directory):
        # print("root", root)  # 当前目录路径
        # print("dirs", dirs)  # 当前路径下所有子目录
        # print("files", files)  # 当前路径下所有非目录子文件

        # 在输出文件夹生成相应的目录
        for dir in dirs:
            outputDirectory = output_directory + '/' + dir
            createDirectory(outputDirectory)

        # 获取所有符合条件的子文件
        for file in files:
            fileName = str(file)
            if fileName.find(inputType.name) > 0:
                inputFilePath = str(root + '/' + fileName)
                inputFilePaths.append(inputFilePath)
    
    return inputFilePaths

# ffmpeg操作命令串
def middleCmdStringWithType(type: FileType) -> str:
    # return ' -map 0:v -vcodec copy -map 0:a:1 -acodec copy '
    if type == FileType.mkv:
        return ' -vcodec copy -acodec acc '
    else:
        return ' '

# mkv转mp4
def mkvToMp4_single(inputPath: str, outputPath: str):
    middleCmdString = middleCmdStringWithType(inputType)
    cmdString = 'ffmpeg -i ' + inputPath + middleCmdString + outputPath
    # os.system(cmdString)
    os.popen(cmdString, 'w', 1)

# 创建目录
def createDirectory(directory: str):
    if not os.path.exists(directory):
        os.mkdir(directory)

# 目录下级文件转.mp4
def mkvToMp4(inputDirectory: str, outputDirectory: str):
    inputPaths = inputPathsFromDirectory(inputDirectory)
    for inputPath in inputPaths:
        outputPath = inputPath.replace(inputDirectory, outputDirectory).replace(inputType.name, outputType.name)
        mkvToMp4_single(inputPath, outputPath)


# 获取输入目录
def getInputDirectory(request: str) -> str:
    inputDirectory = input(request)
    if os.path.exists(inputDirectory):
        return inputDirectory
    else:
        print('ERROR: directory is not exists')
        sys.exit()

# 获取输出目录
def getOutputDirectory(request: str) -> str:
    outputDirectory = input(request)
    createDirectory(outputDirectory)
    return outputDirectory

# 获取目标文件类型
def getFileType(request: str) -> FileType:
    typeList = '支持的类型：'
    for type in FileType:
        typeList += type.name+':'+str(type.value)+'/'
    print(typeList)
    typeInt = int(input(request))
    fileType = FileType(typeInt)
    return fileType





# input_directory = getInputDirectory('请输入目标目录：')
# output_directory = getOutputDirectory('请输入存放目录：')
# inputType = getFileType('请输入目标类型：')
# outputType = getFileType('请输入输出类型：')
mkvToMp4(input_directory, output_directory)




# 压缩

# def compress():
#     cmdString = 'ffmpeg -i /Users/harrycao/Desktop/output/使徒行者/使徒行者_01.mp4 -s vga /Users/harrycao/Desktop/output/使徒行者_01.mp4'
#     os.system(cmdString)


# compress()