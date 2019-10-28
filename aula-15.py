from bottle import Bottle, run

app = Bottle()

msg = '''
<center><h1>Minha página web</h1></center>
<center><a href="/curso_python">Cliqe aqui para acessar o curso</a></center>
'''


@app.route('/')
def index():
	return msg

@app.route('/curso_python')
def curso():
	return '<center><h1>Bem-vindo!</h1></center>'

run(app, host='localhost', port=8080)