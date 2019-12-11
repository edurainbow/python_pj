#__author:"Peter"
#date:2019/12/10
from P1_GET_MD5_Config import get_md5_config
import pickle
from P1_Diff_TXT import diff_txt
from PyQYT.Network.SMTP.SMTP_SEND_MAIL_Attachment import qyt_smtp_attachment
import random
import time

host_list = ['202.100.1.1','202.100.12.2']
def first_bak(host_list,username,password):#备份完整的MD5值与Config!
    dict_config = get_md5_config(host_list,'admin','cisco')
    with open('./config_bak/Pickle_config',"wb") as Pickle_config:
        pickle.dump(dict_config,Pickle_config)
    print('配置备份成功！')
def find_diff(host_list,username,password):
    new_md5_dict = get_md5_config(host_list,'admin','cisco',operation=2)#获取MD5值
    with open('./config_bak/Pickle_Config',"rb") as Pickle_config:
        old_md5_dict = pickle.load(Pickle_config)
    for x in new_md5_dict:
        if new_md5_dict[x] != old_md5_dict[x][1]:#比较MD5是否不同！
            diff_md5_dict = get_md5_config(host_list,'admin','cisco')#如果不同就再次获取这个主
            diff_result = diff_txt(old_md5_dict[x][0],diff_md5_dict[x][0])#比较配置的详细区别
            return x,diff_result#返回IP地址与配置区别
def check_diff():
    try:
        ip,config_changed = find_diff(host_list,'admin','cisco')
        print('发现配置更改！')#如果有返回值，就表示配置变化，打印信息
        id_no = str(int(random.random()*10000))#产生唯一的ID，标识本次邮件！
        Subject = ip + 'configuration changed' + 'reply "y1" for update db' + id_no
        Main_Body = config_changed
        #发送邮件，注意主题最后附上了本次邮件的唯一标示ID
        qyt_smtp_attachment('smtp.163.com',
                            'collinsctk',
                            '1a.cisco',
                            'collinsctk@163.com',
                            'collinsctk@qytang.com;collinsctk@163.com',
                            Subject,
                            Main_Body)
        time.sleep(30)#等到30秒，听候管理员处理结果！
        operation_code = qyt_rec_mail('pop.163.com','collinsctk','1a.cisco',id_no)
        if operation_code == True:#如果范围值为True，就更新数据库
            print('收到管理员确认！更新数据库！')
            first_bak(host_list,'admin','cisco')
    except TypeError:#如果发生错误，就表示配置并没有变化！
        print('配置没有任何修改！')
if __name__ == '__main__':
    first_bak(host_list,'admin','cisco')
    # find_diff(host_list,'admin','cisco')
    #check_diff()