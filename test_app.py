import os
import json
import subprocess
import stat
import bottle
import tempfile
from multiprocessing import Pool
from bottle import route, run, template, auth_basic, request, HTTPResponse

from mail.mail import send_mail


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

def process_mail_wrapper(command, filename, title):
    subprocess.run(command)
    print("sending mail")
    send_mail(filename,title)

@route('/', method='GET')
@auth_basic(check_auth)
def index():
    with open(INFO_PATH) as data_file:
        data = json.load(data_file)
    return template('templates/index', menu=data)


@route('/', method='POST')
def process():
    script_id = request.forms.script_id
    print(request.__dict__)
    print('file',request.files)
    print('query',request.query)
    print('params',request.params)
    print('GET',request.GET)
    print('POST',request.POST)

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
            format(output[0])

            with open(output[0], 'rb') as fp:
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
            _pool.apply_async(process_mail_wrapper,[command,output[0],"Totally test with multiprocessing"])
            # p = Process(target = process_mail_wrapper, args=(command,output[0],"Totally test with multiprocessing"))
            # subprocess.Popen(command)
            # send_mail(output[0],"Test")
            # p.start()
            # p.join()
            print("mail will be sent")

    else:
        return "Error processing request"


if __name__ == '__main__':
    _pool = Pool(processes=4)
    try:
        port = int(os.environ.get('PORT', 8080))
        run(host='0.0.0.0', port=port, debug=True)
    except KeyboardInterrupt:
        _pool.close()
        _pool.join()


application = bottle.default_app()
