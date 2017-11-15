import os
import json
import subprocess
import stat
import bottle
import tempfile
from bottle import route, run, template, auth_basic, request, HTTPResponse

from mail import send_mail


INFO_PATH = 'data.json'
DIR_SCRIPTS = 'scripts'
OUTPUT_TEMPLATES = 'output_templates'


def check_auth(user, pw):
    username = 'quid'
    password = 'Labs@Quid'

    if pw == password and user == username:
        return True
    return False


def save_to_temp(upload):
    name, ext = os.path.splitext(upload.filename)
    tmp = tempfile.NamedTemporaryFile(suffix=ext)
    input_filename = tmp.name
    tmp.close()
    try:
        upload.save(input_filename)
        return input_filename
    except:
        return "Error saving uploaded file"

@route('/', method='GET')
@auth_basic(check_auth)
def index():
    with open(INFO_PATH) as data_file:
        data = json.load(data_file)
    return template('templates/index', menu=data)


@route('/', method='POST')
def process():
    script_id = request.forms.script_id

    if script_id:
        input_files = None
        script_path =None
        output = None
        template = None
        download = False
        with open(INFO_PATH) as data_file:
            data = json.load(data_file)
            for script in data:
                if script.get('id') == int(script_id):
                    try:
                        input_files = [request.files.get(inputs.get('name')) for inputs in script.get('input')]
                        script_path = '{0}{1}'.format(script.get('dir'),script.get('script'))
                        output = ['{0}{1}'.format(output.get('name'),output.get('extension')) for output in script.get('output')]
                        if 'template' in script:
                            template = ['{0}{1}'.format(script.get('dir'),templ.get('name')) for templ in script.get('template')]
                        if script.get('download') == 'yes': download = True
                    except:
                        return "Error parsing scripts info"

        inputs  = list(map(save_to_temp,input_files))
        command = [script_path]
        for ip in inputs:
            command.append(ip)
        for op in output: command.append(op)
        if template:
            for tp in template: command.append(tp)

        st = os.stat(script_path)
        os.chmod(script_path, st.st_mode | stat.S_IEXEC)

        print(command)
        if download:
            subprocess.run(command,stdout=subprocess.PIPE)
            res = HTTPResponse()
            res.headers['Content-Type'] \
            = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            res.headers['Content-Disposition'] = 'attachment; filename="{}"'.\
            format(output_filename)

            with open(output_filename, 'rb') as fp:
                res.body = fp.read()
            for input_filename in inputs:
                try:
                    os.remove(input_filename)
                except OSError:
                    pass

            try:
                os.remove(output_filename)
            except OSError:
                pass
                return res
        # for output_filename in output:
        else:
            subprocess.Popen(command)
            send_mail(output[0],"Test")
            return HTTPResponse(status = 201)

    else:
        return "Error processing request"


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    run(host='0.0.0.0', port=port, debug=True)


application = bottle.default_app()
