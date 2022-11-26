from flask import Blueprint
import click
import getpass
from werkzeug.security import generate_password_hash

from extensions.database import database

userCommands = Blueprint('user', __name__)

@userCommands.cli.command('getUser')
@click.argument('name')
def get_user(name):
    userCollection = database()['usuarios']
    user = [u for u in userCollection.find({'name': name})]
    print(user)

@userCommands.cli.command('addUser')
@click.argument('name')
def create_user(name):
    userCollection = database()['usuarios']
    password = getpass.getpass()
    user = {
        'name': name,
        'password': generate_password_hash(password) 
    }

    userExists = userCollection.find_one({'name':name})

    if not userExists:
        userCollection.insert_one(user)      

@userCommands.cli.command('deleteUser')
@click.argument('name')
def delete_user(name):
    userCollection = database()['usuarios']

    userExists = userCollection.find_one({'name': name})
    if userExists:
        userCollection.delete_one({'name':name})

@userCommands.cli.command('updateuser')
@click.argument('name')
def update_user(name):
    userCollection = database.users 
    userExists = userCollection.find_one({'name': name})
    #userCollection. metodo de atualizar do mongoDb({'name':name})