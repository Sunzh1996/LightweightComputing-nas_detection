import os

#解决windows下路径分割符问题
def convertPath(path: str) -> str:
    return path.replace(os.sep, "/")