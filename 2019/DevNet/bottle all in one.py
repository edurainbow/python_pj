#__author:"Peter"
#date:2019/12/4
from bottle import route,run,static_file,request,TEMPLATE_PATH,jinja2_template,jinja2_view,post,get,response
from datetime import datetime,date
TEMPLATE_PATH.append('G:/python_pj/templates')
@route('/')
def index():
    return "qytang bottle home"

@route('/home')
def index():
    return static_file('index.html',root='G:/python_pj/templates/')

@route('/template',method=['GET'])
def template():
    return jinja2_template('template.html',{'template':'welcom to qytang!'})
@route('/dynamic/<dynamic_name>',method=['GET'])

def dynamic(dynamic_name):
    return jinja2_template('dynamic.html',{'dynamic':dynamic_name})

@route('/formtest',method=['GET','POST'])
def formtest():
    if request.method == 'POST':
        name = request.forms.get('name')
        age = request.forms.get('age')
        return jinja2_template('form_result.html',{'name':name,'age':age})
    else:
        return static_file('form.html',root='G:/python_pj/templates/')

@route('/complex',method=['GET'])
def complex():
    return jinja2_template('complex.html',{'complex_dict':{'dict_key':'dict_value'},
                                           'complex_list':['list1','list2']})

@get('/rpc/<function>')
def rpc(function):
    # response.content_type = 'application/json'
    if function == 'datetime':
        return {'datetime':datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    elif function == 'date':
        return {'datetime':date.today().strftime('%Y-%m-%d')}
    else:
        return {'error':'function not find!'}

@post('/rpc_function')
def rpc_function():
    # response.content_type = 'application/json'
    client_post_data = request.json
    if client_post_data:
        client_function = client_post_data.get('function')
        if client_function == 'datetime':
            return {'datetime': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        elif client_function == 'date':
            return {'datetime': date.today().strftime('%Y-%m-%d')}
        else:
            return {'error': 'function not find!'}
    else:
        return {'error':'no json data'}


run(host="0.0.0.0",port=6868,debug=True)
