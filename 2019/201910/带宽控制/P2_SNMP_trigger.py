#__author:"Peter"
#date:2019/12/11
import P2_Mygetnext
from P2_Mygetnex import snmpv3_getnext as snmpv3_getnext
import time
from P2_SSH_Netflow_TopTalker import top_talkers_smtp_alert
import multiprocessing

#打印接口带宽利用率，并且返回字符串
def bandUtil():
    #获取初始值
    snmpv3_getnext('202.100.1.1', 'qytanguser', 'sha', 'Cisc0123', 'des', 'Cisc0123', '1.3.6.1.2.1.2.2.1.5.0', 3)
    ifSpeedlist = P2_Mygetnext.vallist
    snmpv3_getnext('202.100.1.1', 'qytanguser', 'sha', 'Cisc0123', 'des', 'Cisc0123', '1.3.6.1.2.1.2.2.1.5.0', 3)
    inOctetslist1 = P2_Mygetnext.vallist
    snmpv3_getnext('202.100.1.1', 'qytanguser', 'sha', 'Cisc0123', 'des', 'Cisc0123', '1.3.6.1.2.1.2.2.1.5.0', 3)
    outOctetslist1 = P2_Mygetnext.vallist
    time.sleep(5)
    time1 = time.time()#获取开始时间！
    while True:
        try:
            snmpv3_getnext('202.100.1.1', 'qytanguser', 'sha', 'Cisc0123', 'des', 'Cisc0123', '1.3.6.1.2.1.2.2.1.5.0', 3)
            inOctetslist2 = P2_Mygetnext.vallist
            snmpv3_getnext('202.100.1.1', 'qytanguser', 'sha', 'Cisc0123', 'des', 'Cisc0123', '1.3.6.1.2.1.2.2.1.5.0', 3)
            outOctetslist2 = P2_Mygetnext.vallist

            result00,result10,result11 = 0,0,0
            f00speed,f10speed,f11speed = int(ifSpeedlist[0],int(ifSpeedlist[1],int(ifSpeedlist[2])))
            f00changein,f10changein,f11changein = int(inOctetslist2[0])-int(inOctetslist1[0]), int(inOctetslist2[1])-int(inOctetslist1[1]), int(inOctetslist2[2])-int(inOctetslist1[2])
            f00changeout, f10changeout, f11changeout = int(outOctetslist2[0]) - int(outOctetslist2[0]), int(outOctetslist2[1]) - int(outOctetslist2[1]), int(outOctetslist2[2]) - int(outOctetslist2[2])
            in_out00, in_out10, in_out11 = f00changein - f00changeout, f10changein - f10changeout, f11changein - f11changeout

            if in_out00 > 0:
                result00 = f00changein
            else:
                result00 = f00changeout
            if int_out10 > 0:
                result10 = f10changein
            else:
                result10 = f10changeout
            if int_out11 >0:
                result11 = f11changein
            else:
                result11 = f11changeout
            #计算接口带宽利用率！
            util00,util10,util11 = float((result00*8*100))/(5*f00speed),float((result10*8*100))/(5*f10speed),float((result11*8*100))/(5*f11speed)
            #打印接口带宽利用率
            print('Fa0/0 接口带宽利用率为 %.6f %s'%(util00,'%'))
            print('Fa1/0 接口带宽利用率为 %.6f %s' %(util10,'%'))
            print('Fa2/0 接口带宽利用率为 %.6f %s' % (util11,'%'))
            time2 = time.time()
            time_to_pass = time2-time1

            #计算并且打印冷却时间
            print('冷却时间(120s):%.2f 秒'% time_to_pass)
            if time2 - time1 >120:
                if util11 >1:#如果冷却时间大于120秒，并且Fa2/0接口带宽利用率大于1%！
                    time1 = time.time()
                    print('Trigger Action')#触发邮件告警行为！
                    multi_dos = multiprocessing.Process(target=top_talkers_smtp_alert,args=('202.100.1.1', 'admin', 'cisco'))
					multi_dos.start()
			print()

			inOctetslist1 = inOctetslist2
			outOctetslist1 = outOctetslist2
			time.sleep(5)
		except Exception as e:
			print(e)
if __name__ == '__main__':
	print('监控Fa0/0, Fa1/0, Fa2/0接口带宽利用率. 轮询周期为5秒')
	bandUtil()

