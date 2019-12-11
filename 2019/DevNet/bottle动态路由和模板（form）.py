#__author:"Peter"
#date:2019/12/4
from bottle import route,run,static_file,request,TEMPLATE_PATH,jinja2_template
TEMPLATE_PATH.append('G:/python_pj/templates')
@route('/formtest',method=['GET','POST'])
def formtest():
    if request.method == 'POST':
        name = request.forms.get('name')
        age = request.forms.get('age')
        return jinja2_template('form_result.html',{'name':name,'age':age})
    else:
        return static_file('form.html',root='G:/python_pj/templates/')
run(host="0.0.0.0",port=6868,debug=True)