from flask import Flask, flash, request, render_template, redirect,url_for

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Shelter, Puppy

engine = create_engine("sqlite:///puppyshelter.db")
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

app = Flask(__name__)


@app.route("/")
@app.route("/shelters/")
def allShelters():
	shelters = session.query(Shelter).all()
	return render_template("shelters.html", shelters = shelters)

@app.route("/shelters/new/", methods = ['GET','POST'])
def createShelter():
	if request.method == 'POST':
		newShelter = Shelter(name = request.form['name'],
								address = request.form['address'],
								phone = request.form['phone'],
								email = request.form['email'],
								owner = request.form['owner'])
		session.add(newShelter)
		session.commit()
		return redirect(url_for('allShelters'))
	return render_template('addshelter.html')

@app.route("/shelters/<int:shelter_id>/edit/")
def editShelter(shelter_id):
	return "<h1>Edit puppy shelter</h1>"

@app.route("/shelters/<int:shelter_id>/delete/")
def deleteShelter(shelter_id):
	return "<h1>Delete puppy shelter</h1>"	

@app.route("/shelters/<int:shelter_id>/puppies/")
def allPuppies(shelter_id):
	puppies = session.query(Puppy).filter_by(shelter_id = shelter_id).all()
	shelter = session.query(Shelter).filter_by(id = shelter_id).one()
	return render_template('puppies.html', shelter = shelter, puppies = puppies)

@app.route("/shelters/<int:shelter_id>/puppies/<int:puppy_id>/profile/")
def puppyProfile(shelter_id, puppy_id):
	puppy = session.query(Puppy).filter_by(id = puppy_id).one()
	shelter = session.query(Shelter).filter_by(id = puppy_id).one()
	return render_template('puppyprofile.html', puppy = puppy, shelter = shelter)

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