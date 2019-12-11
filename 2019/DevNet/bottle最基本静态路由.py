#__author:"Peter"
#date:2019/11/19
from bottle import route,run
@route('/')
def index():
    return "qytang bottle home"
run(host="0.0.0.0",port=6868,debug=True)