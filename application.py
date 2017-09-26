import os
import json
import subprocess
import sys
import io
import stat
import bottle
from bottle import route, run, template, auth_basic,request, response

INFO_PATH = 'data.json'


def check_auth(user,pw):
    username = 'quid'
    password = 'Labs@Quid'

    if pw == password and user == username:
        return True
    return False

def get_info(filename):
    with open(filename) as data_file:
        data = json.load(data_file)
    return data

@route('/', method='GET')
@auth_basic(check_auth)
def index():
    dropdown = get_info(INFO_PATH)
    return template('templates/index', menu=dropdown)

@route('/', method='POST')
def process():
    response.headers['Content-Type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    response.headers['Content-Disposition'] = 'attachment; filename="out1.xlsx"'
    script_id = request.forms.selector
    input_csv = request.forms.data
    upload = request.files.get('data')

    upload_path = '/tmp/'
    try:
        upload.save(upload_path)
    # except IOError:
    #     os.rename(upload_path+input_csv,upload_path+input_csv+'.old')
    except:
        pass
    if script_id:
        with open(INFO_PATH) as data_file:
            data = json.load(data_file)
            for script in data:
                if int(script['id']) == int(script_id):
                    filename, file_extension = os.path.splitext(script["script"])

                    st = os.stat('scripts/'+script['script'])
                    os.chmod('scripts/'+script['script'], st.st_mode | stat.S_IEXEC)
                    result = subprocess.run(['./scripts/'+script['script'],script['input']],stdout=subprocess.PIPE)
                    output_file = result.stdout.decode('utf-8').rstrip()
                    print(output_file)
                    return open('output/out1.xlsx', 'rb').read()



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    run(host='0.0.0.0', port=port, debug=True)


application = bottle.default_app()
