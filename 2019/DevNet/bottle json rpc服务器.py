#__author:"Peter"
#date:2019/12/4
from bottle import route,run,post,get,response,request
from datetime import datetime,date
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

run(host="0.0.0.0", port=6666, debug=True)