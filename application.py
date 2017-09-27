import os
import json
import subprocess
import stat
import bottle
import tempfile
from bottle import route, run, template, auth_basic, request, response


INFO_PATH = 'data.json'
DIR_SCRIPTS = 'scripts'


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
    return template('templates/index', menu=drop_down)


@route('/', method='POST')
def process():
    script_id = request.forms.selector
    upload = request.files.get('data')

    tmp = tempfile.NamedTemporaryFile(suffix='.csv')
    input_filename = tmp.name
    tmp.close()

    tmp = tempfile.NamedTemporaryFile(suffix='.xlsx')
    output_filename = tmp.name
    tmp.close()

    try:
        upload.save(input_filename)
    except:
        return "Error saving uploaded file"

    if script_id:
        with open(INFO_PATH) as data_file:
            data = json.load(data_file)
            for script in data:
                if int(script['id']) == int(script_id):
                    # filename, file_extension = os.path.splitext(script["script"])

                    script_path = "{}/{}".format(DIR_SCRIPTS, script['script'])

                    st = os.stat(script_path)
                    os.chmod(script_path, st.st_mode | stat.S_IEXEC)
                    subprocess.run([script_path, input_filename, output_filename, script['output_template']],
                                   stdout=subprocess.PIPE)

                    with open(output_filename, 'rb') as fp:
                        contents = fp.read()

                    try:
                        os.remove(input_filename)
                    except OSError:
                        pass

                    try:
                        os.remove(output_filename)
                    except OSError:
                        pass

                    response.headers['Content-Type'] \
                        = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                    response.headers['Content-Disposition'] = 'attachment; filename="{}"'.\
                        format(script['output_filename'])

                    return contents
    else:
        return "Error processing request"


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    run(host='0.0.0.0', port=port, debug=True)


application = bottle.default_app()
