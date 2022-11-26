from flask import Blueprint, render_template, request, session, redirect, url_for
from extensions.database import database

dados_receita = Blueprint('dados_receita', __name__)

@dados_receita.route('/list')

def list_dados():
    if 'username' in session:
        dados = database.dados.find()
        return render_template('dados/list.html', dados = dados)
    else:
        return redirect(url_for('usuario.index'))


