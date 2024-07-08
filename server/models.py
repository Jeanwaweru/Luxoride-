from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Enum('admin', 'user', name='user_roles'), nullable=False)
    profile_image = db.Column(db.String(255), nullable=True)
    phone_number = db.Column(db.String(20), nullable=True)
    reviews = db.relationship('Review', backref='user', lazy=True)
    bookings = db.relationship('Booking', backref='user', lazy=True)

class CarOwner(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(20), nullable=True)
    profile_image = db.Column(db.String(255), nullable=True)
    cars = db.relationship('Car', backref='car_owner', lazy=True)

class Car(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    make = db.Column(db.String(255), nullable=False)
    model = db.Column(db.String(255), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    price_per_day = db.Column(db.Numeric, nullable=False)
    availability_status = db.Column(db.Boolean, nullable=False, default=True)
    car_image_url = db.Column(db.String(255), nullable=True)
    owner_id = db.Column(db.BigInteger, db.ForeignKey('car_owner.id'), nullable=False)
    reviews = db.relationship('Review', backref='car', lazy=True)
    bookings = db.relationship('Booking', backref='car', lazy=True)

class Review(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger, db.ForeignKey('user.id'), nullable=False)
    car_id = db.Column(db.BigInteger, db.ForeignKey('car.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=True)

class Booking(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger, db.ForeignKey('user.id'), nullable=False)
    car_id = db.Column(db.BigInteger, db.ForeignKey('car.id'), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    car_owner_id = db.Column(db.BigInteger, nullable=False)
