#__author:"Peter"
#date:2019/11/25
import win32com.client #系统客户端包
speaker = win32com.client.Dispatch("SAPI.SPVOICE")  # 系统接口

num=5
while num >0:
    speaker.speak("我是凤姐，我爱死了申凌睿")
    num -=1
