#__author:"Peter"
#date:2019/11/19
from bottle import route,run,jinja2_view,TEMPLATE_PATH,jinja2_template
TEMPLATE_PATH.append('G:/python_pj/templates')
@route('/template',method=['GET'])
def template():
    return jinja2_template('template.html',{'template':'welcom to qytang!'})
@route('/dynamic/<dynamic_name>',method=['GET'])
def dynamic(dynamic_name):
    return jinja2_template('dynamic.html',{'dynamic':dynamic_name})
run(host="0.0.0.0",port=6868,debug=True)