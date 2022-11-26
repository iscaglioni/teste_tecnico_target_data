from flask import Flask
from routes.usuario import usuario
from routes.dados_receita import dados_receita
from extensions.database import database
from commands.userCommands import userCommands
# from commands.dadosCommands import dados_empresas
# from commands.dadosCommands import dadosCommands

def create_app(config_object='settings'):
    app = Flask(__name__)   
    app.config.from_object(config_object)
    app.register_blueprint(usuario)
    app.register_blueprint(dados_receita)
    app.register_blueprint(userCommands)
    # app.register_blueprint(dadosCommands) 
    # app.register_blueprint(dados_empresas)   

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()

