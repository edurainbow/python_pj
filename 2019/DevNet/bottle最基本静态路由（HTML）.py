#__author:"Peter"
#date:2019/11/19
from bottle import route,run,static_file
@route('/')
def index():
    return static_file('index.html',root='G:/python_pj/templates/')
run(host="0.0.0.0",port=6868,debug=True)