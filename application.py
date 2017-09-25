import os
import json
import subprocess
import sys
import io
from bottle import route, run, template, auth_basic,request, response

INFO_PATH = 'data.json'


def check_auth(user,pw):
    username = 'quid'
    password = 'Labs@Quid'

    if pw == password and user == username:
        return True
    return False

def get_dropdown(filename):
    dropdown = []
    with open(filename) as data_file:
        data = json.load(data_file)
        for script in data:
            dropdown.append({'id':script['id'],'title':script['title']})
    return dropdown

@route('/', method='GET')
@auth_basic(check_auth)
def index():
    dropdown = get_dropdown(INFO_PATH)
    return template('templates/index', menu=dropdown)

@route('/', method='POST')
def process():
    # response = None
    response.headers['Content-Type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    response.headers['Content-Disposition'] = 'attachment; filename="out1.xlsx"'
    script_id = request.forms.get('scripts')
    if script_id:
        with open(INFO_PATH) as data_file:
            data = json.load(data_file)
            for script in data:
                if int(script['id']) == int(script_id):
                    filename, file_extension = os.path.splitext(script["cmd"])
                    if file_extension=='.sh':
                        result = subprocess.run(['./'+'scripts/'+ script['cmd'],script['params']],stdout=subprocess.PIPE)
                        # response = result.stdout.decode('utf-8')
                    elif file_extension=='.py':
                        result = subprocess.run(['python', 'scripts/'+ script['cmd'],script['params']],stdout=subprocess.PIPE)
                        # response = result.stdout.decode('utf-8')
                        return open('output/out1.xlsx', 'rb').read()



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    run(host='0.0.0.0', port=port, debug=True)
