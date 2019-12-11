#__author:"Peter"
#date:2019/12/4
from bottle import route,run,TEMPLATE_PATH,jinja2_template
TEMPLATE_PATH.append('G:/python_pj/templates')
@route('/complex',method=['GET'])
def complex():
    return jinja2_template('complex.html',{'complex_dict':{'dict_key':'dict_value'},
                                           'complex_list':['list1','list2']})
run(host="0.0.0.0",port=6868,debug=True)