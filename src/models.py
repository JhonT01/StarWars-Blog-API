from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    people = db.relationship("Favorite_People", lazy=True, backref="user")
    planets = db.relationship("Favorite_Planet", lazy=True, backref="user")
    vehicles = db.relationship("Favorite_Vehicle", lazy=True, backref="user")

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250))
    height = db.Column(db.Integer)
    mass = db.Column(db.Integer)
    hair_color = db.Column(db.String(250))
    skin_color = db.Column(db.String(250))
    eye_color = db.Column(db.String(250))
    gender = db.Column(db.String(250))
    homeworld = db.Column(db.String(250))
    films = db.Column(db.String(250))
    species = db.Column(db.String(250))
    vehicles = db.Column(db.String(250))
    starships = db.Column(db.String(250))
    created = db.Column(db.String(250))
    edited = db.Column(db.String(250))
    url = db.Column(db.String(250))
    
    def __repr__(self):
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "description" : self.description,
            "height" : self.height,
            "mass" : self.mass,
            "hair_color" : self.hair_color,
            "skin_color" : self.skin_color,
            "eye_color" : self.eye_color,
            "gender" : self.homeworld,
            "homeworld" : self.homeworld,
            "films" : self.films,
            "species" : self.species,
            "vehicles" : self.vehicles,
            "starships" : self.starships,
            "created" : self.created,
            "edited" : self.edited,
            "url" : self.url
        }

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250))
    diameter = db.Column(db.Integer)
    rotation_period = db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)
    gravity = db.Column(db.String(250))
    population = db.Column(db.Integer)
    climate = db.Column(db.String(250))
    terrain = db.Column(db.String(250))
    surface_water = db.Column(db.Integer)
    created = db.Column(db.String(250))
    edited = db.Column(db.String(250))
    url = db.Column(db.String(250))
  

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    model = db.Column(db.String(250))
    vehicle_class = db.Column(db.String(250))
    manufacturer = db.Column(db.String(250))
    cost_in_credits = db.Column(db.Integer)
    length = db.Column(db.Float)
    crew = db.Column(db.Integer)
    passengers = db.Column(db.Integer)
    max_atmosphering_speed = db.Column(db.Integer)
    cargo_capacity = db.Column(db.Integer)
    consumables = db.Column(db.String(250))
    films = db.Column(db.String(250))
    pilots = db.Column(db.String(250))
    created = db.Column(db.String(250))
    edited = db.Column(db.String(250))
    url = db.Column(db.String(250))

    def to_dict(self):
        return {}   

# --------------  Tablas Pivote  -------------------------------------

class Favorite_People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'))

    def to_dict(self):
        return {}   

class Favorite_Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))

    def to_dict(self):
        return {}   

class Favorite_Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'))

    def to_dict(self):
        return {}   