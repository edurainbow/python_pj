#__author:"Peter"
#date:2019/12/10
from difflib import *

def diff_txt(file1,file2):
    txt1 = open(file1,'r').readlines()
    txt2 = open(file2,'r').readlines()
    result = Differ().compare(txt1,txt2)
    return_result = '\n'.join(list(result))
    return return_result
def diff_txt(txt1,txt2):
    txt1_list = txt1.decode().split('\r\n')
    txt2_list = txt2.decode().split('\r\n')
    result = Differ().compare(txt1_list,txt2_list)
    return_result = '\r\n'.join(list(result))
    return return_result

if __name__ == '__main__':
    txt1 = b"\r\nBuilding configuration...\r\n\r\nCurrent configuration : 2406 bytes\r\n!\r\nversion"
    txt2 = b"\r\nBuilding configur...\r\n\r\nCurrent configuran : 2407 bytes\r\n!\r\nversion 15.2"
    print(diff_txt(txt1,txt2))