from backend.modelos import db
from backend import create_app
from flask import Flask

app = create_app('default')
app_context = app.app_context()
app_context.push()
db.init_app(app)
db.create_all()


from flask import Flask, request

app = Flask(__name__)

@app.route('/username/<username>/password/<password>', methods=['GET', 'POST'])
def login(username, password):
    app.logger.info(f'Solicitud de la ruta {request.path}')
    return f"Tu username es {username}, pero no se mostrará tu contraseña por motivos de seguridad."

if __name__ == '__main__':
    app.run(debug=True)

@app.route ('/username/<username>/certificado/<certificado>', methods=['GET', 'POST'])
def certificado(username, certificado):
    app.logger.info(f'solicitud de la ruta {request.path}')
    return f"querido usuario {username}, tu certificado es {certificado}"   

@app.route ('/certificado/<certificado>/estado/<estado>')
def estado(certificado, estado):
    app.logger.info(f'solicitud de la ruta {request.path}')    
    return f"tu certificado {certificado}, estan en estado {estado}"

@app.route ('/certificado/<certificado>/fecha/<fecha>/hora/<hora>')
def fecha(certificado, fecha, hora):
    app.logger.info(f'solicitud de la ruta {request.path}')    
    return f"tu certificado {certificado}, de la fecha {fecha}, y hora es{hora}"
