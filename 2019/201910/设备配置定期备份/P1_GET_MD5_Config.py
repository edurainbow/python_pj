#__author:"Peter"
#date:2019/12/10
import shelve
from Simple_SSH_Client import QYT_SSHClient_SingleCMD
import pickle
import re

def get_md5_config(host_list,username,password,operation=0):
    dict_config = {}
    for host in host_list:
        if operation == 0:#如果操作码为0，表示MD5和Config都要获取！
            try:
                #获取完整的running-configuration
                run_config = QYT_SSHClient_SingleCMD(host,'admin','cisco','show run')
                #下面部分在做running-configuration的裁剪操作，只留hostname开始的配置
                list_run_config = run_config.decode().split('\r\n')
                location = 0
                host_location = 0
                for i in list_run_config:
                    if re.match('.*hostname.*',i):
                        host_location = location#定位hostname所在位置
                    else:
                        location +=1
                list_run_config = list_run_config[host_location:]#截取hostname开始往后的部分
                run_config = '\r\n'.join(list_run_config)#再次还原为字串形式的配置
                #获取配置的MD5值
                md5 = QYT_SSHClient_SingleCMD(host,'admin','cisco','verify /md5 system:running')
                dict_config[host] = [run_config.encode(),md5.strip()[-32:]]
                #仅仅截取最后32位的MD5值
                #返回字典
            except Exception as e:
                print('%stErrorn %s'%(host,e))
        elif operation == 1:#如果操作码为1，表示获取Config!
            try:
                run_config = QYT_SSHClient_SingleCMD(host,'admin','cisco','show run')
                list_run_config = _config.decode().split('\r\n')
                location = 0
                host_location = 0
                for i in list_run_config:
                    if re.match('.*hostname.*',i):
                        host_location = location
                    else:
                        location +=1
                list_run_config = list_run_config[host_location:]
                run_config = '\r\n'.join(list_run_config)
                dict_config[host] = run_config.encode()
            except Exception as e:
                print('%stErrorn %s'%(host,e))
        elif operation ==2:#如果操作码为2表示只获取MD5值！
            try:
                md5 = QYT_SSHClient_SingleCMD(host,'admin','cisco','verify /md5 system:running')
                dict_config[host] = md5.strip()[-32:]
            except Exception as e:
                print('%stErrorn %s'%(host,e))
        else:
            print('操作码传入错误！')
    return dict_config
if __name__ == '__main__':
    print(get_md5_config(['202.100.1.1','202,100.12.2'],'admin','cisco',operation=2))