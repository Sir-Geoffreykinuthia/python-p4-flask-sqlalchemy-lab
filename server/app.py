#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal = Animal.query.filter(Animal.id == id).first()

    return f'''
     <ul>
        <ul>ID: {animal.id}</ul>
        <ul>Name: {animal.name}</ul>
        <ul>Species: {animal.species}</ul>
        <ul>Zookeeper: {animal.zookeeper_id}</ul>
        <ul>Enclosure: {animal.enclosure_id}</ul>
     </ul> 
    '''


@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.filter(Zookeeper.id == id).first()
    animals = ''
    for animal in zookeeper.animals:
        animals += f'<ul>Animal: {animal.name}</ul>'
    return f'''
        <ul>
        <ul>ID: {zookeeper.id}</ul>
        <ul>Name: {zookeeper.name}</ul>
        <ul>Birthday: {zookeeper.birthday}</ul>
        <ul>
        {animals}
        </ul>
    '''


@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.filter(Enclosure.id == id).first()
    animals = ''
    for animal in enclosure.animals:
        animals += f'<ul>Animal: {animal.name}</ul>'
    return f'''
        <ul>
        <ul>ID: {enclosure.id}</ul>
        <ul>Environment: {enclosure.environment}</ul>
        <ul>Open to visitors: {enclosure.open_to_visitors}</ul>
        </iul>
        <ul>
        {animals}
        </ul>
    '''

if __name__ == '__main__':
    app.run(port=5555, debug=True)
