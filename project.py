from flask import Flask, flash, request, render_template, redirect

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


app = Flask(__name__)


@app.route("/")
@app.route("/shelters/")
def allShelters():
	return "<h1>All the shelters</h1>"

@app.route("/shelters/new/")
def createShelter():
	return "<h1>Create a new shelter</h1>"

@app.route("/shelters/<int:shelter_id>/edit/")
def editShelter(shelter_id):
	return "<h1>Edit puppy shelter</h1>"

@app.route("/shelters/<int:shelter_id>/delete/")
def deleteShelter(shelter_id):
	return "<h1>Delete puppy shelter</h1>"	

@app.route("/shelters/<int:shelter_id>/puppies/")
def allPuppies(shelter_id):
	return "<h1>All the puppies</h1>"

@app.route("/shelters/<int:shelter_id>/puppies/new/")
def addNewPuppy(shelter_id):
	return "<h1>Create new puppy</h1>"

@app.route("/shelters/<int:shelter_id>/puppies/<int:puppy_id>/adopt/")
def adoptPuppy(shelter_id, puppy_id):
	return "<ht>Adobt this adorable puppy</h1>"

@app.route("/shelters/<int:shelter_id>/puppies/<int:puppy_id>/edit/")
def editPuppy(shelter_id,puppy_id):
	return "<h1>Update information about puppy</h1>"



if __name__ == "__main__":
	app.debug = True
	app.run(host="0.0.0.0", port = 5000)