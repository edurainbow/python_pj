#__author:"Peter"
#date:2019/12/11
from P3_Excel_Parser_openpyxl_Return_dict import excel_parser_return_dict
from P2_SSH_Client_CMDS import QYT_SSHClient_MultiCMD
def excel_user_to_ios(ip,username,password,excelfile):
    #读取excel信息，返回字典!
    user_dict = excel_parser_return_dict(excelfile)
    #产生配置命令
    cmds = ['configure terminal']
    for x,y in user_dict.items():
        cmd = 'username' + x + 'privilege' + str(y[1] + 'password' + str(y[0]))
        cmds.append(cmd)
    #ssh登录设备，配置用户信息
    QYT_SSHClient_MultiCMD(ip,username,password,cmds)
if __name__ == '__main__':
    excel_user_to_ios('202,100,1,1','admin','cisco','P3_Read_Accounts.xlsx')