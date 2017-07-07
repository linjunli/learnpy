from bottle import route, run, template, error, response, static_file

@route('/hello/<name>')
def index(name='Stranger'):
    return template('<b>Hello {{ name }}</b>', name=name)
@error(404)
def error404(error):
    return "Nothing here, sorry!"
@route('/js/<filename:re:.*\.js>')
def send_js(filename):
    return static_file(filename, root='./app/static/js', mimetype='application/javascript')
run(server='wsgiref', host='localhost', port=8080)