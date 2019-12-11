#__author:"Peter"
#date:2019/12/11
import sys
sys.path.append('/usr/local/lib/python3.4/dist-packages/PyQYT/ExtentionPackages')
sys.path.append('/usr/lib/python3.4/site-packages/PyQYT/ExtentionPackages')
sys.path.append('../../ExtentionPackages')
import paramiko
import re
import random
import time
from PyQYT.Network.SMTP.SMTP_SEND_MAIL_Attachment import qyt_smtp_attachment
from POP3_For_Practice_Lab import qyt_rec_mail
from P2_SSH_Client_CMD5 import QYT_SSHClient_MultiCMD

white_list = ['202,100,1,101','202,100,1,1']#永远不希望被阻止的IP地址！白名单！
def QYT_SSHClient_SingleCMD(ip,username,password,cmd):#执行单一命令并且返回结果
    try:
        ssh = paramiko.SSHClient()#创建SSH Client
        ssh.load_system_host_keys()#加载系统SSH密钥
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())#添加新的SSH密钥
        ssh.connect(ip,port=22,username=username,password=password,timeout=5,compress=True)
        stdin,stdout,stderr = ssh.exec_command(cmd)#执行命令
        x = stdout.read().decode()#读取回显
        return x
        ssh.close()
    except Exception as e:
        print('%stErrorn %s'%(ip,e))

def get_top_talkers(ip,username,password):
    SSH_Result = QYT_SSHClient_SingleCMD(ip,username,password,'show ip flow top-talkers')
    '''
    读取show ip flow top-talkers
    '''
    SSH_Result_List_Raw = SSH_Result.split('\r\n')
    SSH_Result_List = []
    for line in SSH_Result_List_Raw:
        if line == '':
            continue
        if re.match('.*top talkers.*',line):
            continue
        if re.match('.*SrcIPaddress.*',line):
            continue
        else:#提取show ip flow top-talkers的内容，并且通过正则表达式匹配整理成为清单
            tmp = re.search('(\w.*)\s+(\w.*)\s+(\w.*)\s+(\w.*)\s+(\w.*)\s+(\w.*)\s+(\w.*)\s+(\w.*)', line).groups()
            tmp_list = [z.strip() for z in tmp]
            SSH_Result_List.append(tmp_list)
    return SSH_Result_List#返回清单

def top_talkers_smtp_alert(ip,username,password):
    local_ip = ip
    local_username = username
    local_password = password

    top_talkers_not_in_white_list = []
    for i in get_top_talkers(ip,username,password)[:3]:#获取在top-talker中前三的IP！
        found = 0
        for x in white_list:
            if i[1] == x:
                found = 1
            else:
                continue
        if found == 0:
            #找到位于top-talker前三，并且不在白名单中的IP地址！
            top_talkers_not_in_white_list.append(i[1])

        if top_talkers_not_in_white_list != []:
            new_list = []#清除重复IP地址
            for i in top_talkers_not_in_white_list:#清除重复IP地址
                if not i in new_list:
                    new_list.append(i)
            top_talkers_not_in_white_list = new_list
    if top_talkers_not_in_white_list != []:
        #产生唯一标示ID!
        id_no = str(int(random.random()*10000))
        Subject = 'Top Talker not in the white list'+ id_no
        Main_Body = 'Top Talker host not in the white list\n'
        for ip in top_talkers_not_in_white_list:
            Main_Body = Main_Body + ip + '\n'
        Main_Body = Main_Body + 'Pls reply in 1 min,y1 (for kill),n2 (do noting)[default]'
        #发送邮件通知管理员，注意主题最后有唯一标识ID!
        qyt_smtp_attachment('smtp.163.com',
                            'collinsctk',
                            '1a.cisco',
                            'collinsctk@163.com',
                            'collinsctk@qytang.coom;collinsctk@163.com',
                            Subject,
                            Main_Body)
        time.sleep(30)#等待30秒，听候管理员处理的回复邮件！
        operation_code = qyt_rec_mail('pop.163.com','collinsctk','1a.cisco',id_no)

        if operation_code = True:#如果管理员回复'y1'，表示要阻止这些IP地址
            #产生配置命令
            print('管理员回复邮件希望阻止流量!')
            print('开始配置ACL阻止流量！')
            cmds = ['configure terminal','ip access-list extended python_acl_'+id_no]
            for ip in top_talkers_not_in_white_list:
                cmd = 'deny ip host' + ip + 'any'
                cmds.append(cmd)
            cmd = 'permit ip any any'
            cmds.append(cmd)
            cmd = 'interface FastEthernet2/0'
            cmds.append(cmd)
            cmd = 'ip access-group python_acl_' + id_no + 'in'
            cmds.append(cmd)
            #登录到设备，并且配置命令
            QYT_SSHClient_MultiCMD(local_ip,local_username,local_password,cmds)

            time.sleep(20)#等待20秒后，自动清除配置
            print('阻止时间已过！自动清除ACL配置！')
            del_cmds = ['configure terminal']
            cmd = 'no ip access-list extended python_acl_'+id_no
            del_cmds.append(cmd)
            cmd = 'interface FastEthernet2/0'
            del_cmds.append(cmd)
            #登录到设备，并且清除配置命令
            QYT_SSHClient_MultiCMD(local_ip,local_username,local_password,del_cmds)
        else:
            print('未收到管理员处理邮件，或者回复为"n2",保持现状！')
if __name__ == '__main__':
    top_talkers_smtp_alert('202.100.1.1','admin','cisco')

