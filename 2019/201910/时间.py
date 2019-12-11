#__author:"Peter"
#date:2019/11/11
import time
mytimes=time.time()
print(mytimes)
print("自从1970现在过去了",int(mytimes),'秒')
seconds=int(mytimes)%60
hours=int(mytimes)//3600
#mins=int(mytimes)%3600//60
mins=(int(mytimes)-int(mytimes)//3600*3600)//60
days=hours//24
hours=hours%24
months=days//30
days=days%30
years=months//24
months=months%24

print("自从1970现在过去了",
      years,'年',
      months,'月',
      days,'天',
      hours,'时',
      mins,'分',
      seconds,'秒',
      )

