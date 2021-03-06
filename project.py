from flask import Flask, flash, request, render_template, redirect,url_for

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Shelter, Puppy

engine = create_engine("sqlite:///puppyshelter.db")
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

app = Flask(__name__)


#the main page routing
@app.route("/")
@app.route("/shelters/")
def allShelters():
	shelters = session.query(Shelter).all()
	return render_template("shelters.html", shelters = shelters)

#routing for new shelter creation
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

#routing for updation of a shelter
@app.route("/shelters/<int:shelter_id>/update/", methods=['GET','POST'])
def updateShelter(shelter_id):
	shelter = session.query(Shelter).filter_by(id = shelter_id).one()
	if request.method == 'POST':
		shelter.name = request.form['name']
		shelter.address = request.form['address']
		shelter.phone = request.form['phone']
		shelter.email = request.form['email']
		shelter.owner = request.form['owner']
		session.add(shelter)
		session.commit()
		return redirect(url_for('allShelters'))
	return render_template('updateshelter.html',shelter = shelter)

#routing for deletion of shelter
@app.route("/shelters/<int:shelter_id>/delete/")
def deleteShelter(shelter_id):
	return "<h1>Delete puppy shelter</h1>"	

#routing for all puppies page
@app.route("/shelters/<int:shelter_id>/puppies/")
def allPuppies(shelter_id):
	puppies = session.query(Puppy).filter_by(shelter_id = shelter_id).all()
	shelter = session.query(Shelter).filter_by(id = shelter_id).one()
	return render_template('puppies.html', shelter = shelter, puppies = puppies)

#routing for a specific puppy profile
@app.route("/shelters/<int:shelter_id>/puppies/<int:puppy_id>/profile/")
def puppyProfile(shelter_id, puppy_id):
	puppy = session.query(Puppy).filter_by(id = puppy_id).one()
	shelter = session.query(Shelter).filter_by(id = shelter_id).one()
	return render_template('puppyprofile.html', puppy = puppy, shelter = shelter)

#routing for adding new puppy
@app.route("/shelters/<int:shelter_id>/puppies/new/", methods=['GET','POST'])
def addNewPuppy(shelter_id):
	shelter = session.query(Shelter).filter_by(id = shelter_id).one()
	if request.method == 'POST':
		newPuppy = Puppy(name=request.form['name'],
							weight=float(request.form['weight']),
							age = int(request.form['age']),
							breed = request.form['breed'],
							gender = request.form['gender'],
							shelter = shelter)
		session.add(newPuppy)
		session.commit()
		return redirect(url_for('allPuppies',shelter_id = shelter.id))
	return render_template('addpuppy.html', shelter = shelter)

#routing for deletion of a puppy
@app.route("/shelters/<int:shelter_id>/puppies/<int:puppy_id>/delete/")
def deletePuppy(shelter_id, puppy_id):
	pup = session.query(Puppy).filter_by(id = puppy_id).one()
	session.delete(pup)
	session.commit()
	return redirect(url_for("allPuppies",shelter_id = shelter_id))

#routing for adoption of a puppy
@app.route("/shelters/<int:shelter_id>/puppies/<int:puppy_id>/adopt/")
def adoptPuppy(shelter_id, puppy_id):
	return "<ht>Adobt this adorable puppy</h1>"

#routing for updating a puppy's information
@app.route("/shelters/<int:shelter_id>/puppies/<int:puppy_id>/update/")
def editPuppy(shelter_id,puppy_id):
	return "<h1>Update information about puppy</h1>"



if __name__ == "__main__":
	app.debug = True
	app.run(host="0.0.0.0", port = 5000)