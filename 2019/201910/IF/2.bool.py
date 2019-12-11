#__author:"Peter"
#date:2019/11/15
import os
cmd = input("请输入cmd命令:")
isrun = (cmd == "notepad")
print(isrun)
if isrun:
    os.system("notepad")