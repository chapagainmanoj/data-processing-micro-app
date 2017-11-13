import os
import json
import subprocess
import stat
import bottle
import tempfile
from bottle import route, run, template, auth_basic, request, response


INFO_PATH = 'data.json'
DIR_SCRIPTS = 'scripts'
OUTPUT_TEMPLATES = 'output_templates'


def check_auth(user, pw):
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
    drop_down = get_info(INFO_PATH)
    # print(drop_down)
    return template('templates/index', menu=drop_down)


@route('/', method='POST')
def process():
    script_id = request.forms.selector
    print("req",request.forms.selector)
    upload = request.files.get('quid_KOL_webofscience_input.csv')
    print("upload",upload.__dict__)

    input_filename = "scripts/KOL/test_input.csv"
    output_filename = "test_output.xlsx"

    # # random files
    # tmp = tempfile.NamedTemporaryFile(suffix='.csv')
    # input_filename = tmp.name
    # tmp.close()
    #
    # tmp = tempfile.NamedTemporaryFile(suffix='.xlsx')
    # output_filename = tmp.name
    # tmp.close()

    # try:
    #     upload.save(input_filename)
    # except:
    #     return "Error saving uploaded file"

    # if script_id:
    #     with open(INFO_PATH) as data_file:
    #         data = json.load(data_file)
    #         for script in data:
    #             if int(script['id']) == int(script_id):
    #                 # filename, file_extension = os.path.splitext(script["script"])
    #
    #                 script_path = "{}/{}".format(DIR_SCRIPTS, script['script'])
    #                 script_path = 'scripts/KOL/kol.py'
    #                 template_file = 'scripts/KOL/template.xlsx'
    #
    #                 # script_path = 'scripts/second.py'
    #
    #                 st = os.stat(script_path)
    #                 os.chmod(script_path, st.st_mode | stat.S_IEXEC)
    #
    #                 # subprocess.run([script_path, input_filename, output_filename,
    #                 #                 "{}/{}".format(OUTPUT_TEMPLATES,script['output_template'])],
    #                 #                stdout=subprocess.PIPE)
    #
    #                 print("process started")
    #                 subprocess.run([script_path, input_filename, output_filename,
    #                                 template_file],
    #                                stdout=subprocess.PIPE)
    #                 print("process Ended")
    #
    #                 with open(output_filename, 'rb') as fp:
    #                     contents = fp.read()
    #
    #                 try:
    #                     os.remove(output_filename)
    #                 except OSError:
    #                     pass
    #
    #                 response.headers['Content-Type'] \
    #                     = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    #                 response.headers['Content-Disposition'] = 'attachment; filename="{}"'.\
    #                     format(script['output_filename'])
    #
    #                 return contents
    # else:
    #     return "Error processing request"

    print("ok")


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    run(host='0.0.0.0', port=port, debug=True)


application = bottle.default_app()
