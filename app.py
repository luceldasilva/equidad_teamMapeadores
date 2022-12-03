from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
app = Flask(__name__)


@app.route('/')
def index():
   print('Abriendo pagina de inicio')
   return render_template('index.html')

@app.route('/servidoras/instituciones')
def servidorasInstituciones():
   print('Pagina de Servidoras por instituciones')
   return render_template('index.html')

@app.route('/servidoras/area')
def servidorasArea():
    print('Pagina de Servidoras por area')
    return render_template('index.html')

@app.route('/servidoras/puesto')
def servidorasPuesto():
    print('Pagina de Servidoras por puesto')
    return render_template('index.html')


@app.route('/servidoras/responsabilidad')
def servidorasResponsabilidad():
   print('Pagina de Servidoras por responsabiliad')
   return render_template('index.html')

@app.route('/servidoras/procedimiento')
def servidorasProcedimiento():
   print('Pagina de Servidoras por procedimiento')
   return render_template('index.html')


#Sancionadas
@app.route('/servidoras/sancionadas')
def servidorasSancionadas():
    print('Pagina de Servidoras sancionadas')
    return render_template('index.html')

@app.route('/servidoras/sancionadas/puesto')
def servidorasSancionadasPuesto():
    print('Pagina de Servidoras sancionadas puesto')
    return render_template('index.html')

@app.route('/servidoras/sancionadas/tipofalta')
def servidorasSancionadasTipoFalta():
    print('Pagina de Servidoras tipofalta')
    return render_template('index.html')

@app.route('/servidoras/sancionadas/causamotivo')
def servidorasSancionadasCausaMotivo():
    print('Pagina de Servidoras causamotivo')
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico', mimetype='image/vnd.microsoft.icon')

# metodo en caso de errores
@app.errorhandler(404)
def page_not_found(e):
    return render_template('page-404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('page-500.html'), 500


@app.errorhandler(401)
def no_authorized(e):
    return render_template('page-500.html'), 401



if __name__ == '__main__':
   app.run(debug=True)