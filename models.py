import os
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

database_path = os.environ.get('DATABASE_URL')
# Case where there is no set path, set it
if not database_path:
    database_name = "CharGen"
    database_path = "postgres://{}/{}".format(
        'localhost:5432', database_name)

db = SQLAlchemy()
'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'''
Race
BLAH BLAH
'''


class Race(db.Model):
    __tablename__ = 'races'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    max_age = Column(Integer, nullable=False)
    strength_bonus = Column(Integer, nullable=False)
    speed_bonus = Column(Integer, nullable=False)
    will_bonus = Column(Integer, nullable=False)

    def __init__(self, name, max_age, strength_bonus, speed_bonus, will_bonus):
        self.name = name
        self.max_age = max_age
        self.strength_bonus = strength_bonus
        self.speed_bonus = speed_bonus
        self.will_bonus = will_bonus

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'max_age': self.max_age,
            'strength_bonus': self.strength_bonus,
            'speed_bonus': self.speed_bonus,
            'will_bonus': self.will_bonus
        }


class Char_class(db.Model):
    __tablename__ = 'classes'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    primary_role = Column(String)
    secondary_role = Column(String)
    strength_bonus = Column(Integer, nullable=False)
    speed_bonus = Column(Integer, nullable=False)
    will_bonus = Column(Integer, nullable=False)

    def __init__(self, name, primary_role, secondary_role, strength_bonus,
                 speed_bonus, will_bonus):
        self.name = name
        self.primary_role = primary_role
        self.secondary_role = secondary_role
        self.strength_bonus = strength_bonus
        self.speed_bonus = speed_bonus
        self.will_bonus = will_bonus

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'primary_role': self.primary_role,
            'secondary_role': self.secondary_role,
            'strength_bonus': self.strength_bonus,
            'speed_bonus': self.speed_bonus,
            'will_bonus': self.will_bonus
        }


class Character(db.Model):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    char_class_id = Column(Integer, ForeignKey(
        'classes.id'), nullable=False)
    race_id = Column(Integer, ForeignKey('races.id'), nullable=False)
    strength = Column(Integer, nullable=False)
    speed = Column(Integer, nullable=False)
    will = Column(Integer, nullable=False)

    def __init__(self, first_name, last_name, char_class_id, race_id, strength, speed, will):
        self.first_name = first_name
        self.last_name = last_name
        self.char_class_id = char_class_id
        self.race_id = race_id
        self.strength = strength
        self.speed = speed
        self.will = will

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'char_class_id': self.char_class_id,
            'race_id': self.race_id,
            'strength': self.strength,
            'speed': self.speed,
            'will': self.will
        }


'''
Races

{
    "name": "Elf",
    "max_age": 750,
    "strength_bonus": 0,
    "speed_bonus": 1,
    "will_bonus": 2
}
{
    "name": "Dwarf",
    "max_age": 450,
    "strength_bonus": 2,
    "speed_bonus": 0,
    "will_bonus": 1
}
{
    "name": "Human",
    "max_age": 90,
    "strength_bonus": 1,
    "speed_bonus": 1,
    "will_bonus": 1
}
{
    "name": "Gnome",
    "max_age": 315,
    "strength_bonus": -2,
    "speed_bonus": 1,
    "will_bonus": 3
}

CLASSES


{
    "name": "Wizard",
    "primary_role": "ranged_attacker",
    "secondary_role": "controller",
    "strength_bonus": 0,
    "speed_bonus": 0,
    "will_bonus": 3
}
{
    "name": "Druid",
    "primary_role": "supporter",
    "secondary_role": "ranged_attacker",
    "strength_bonus": 0,
    "speed_bonus": 1,
    "will_bonus": 2
}
{
    "name": "Paladin",
    "primary_role": "supporter",
    "secondary_role": "melee_attacker",
    "strength_bonus": 2,
    "speed_bonus": 0,
    "will_bonus": 1
}
{
    "name": "Bard",
    "primary_role": "supporter",
    "secondary_role": "controller",
    "strength_bonus": 0,
    "speed_bonus": 2,
    "will_bonus": 1
}
{
    "name": "Elementalist",
    "primary_role": "ranged_attacker",
    "secondary_role": "controller",
    "strength_bonus": 0,
    "speed_bonus": 1,
    "will_bonus": 2
}
{
    "name": "Barbarian",
    "primary_role": "melee_attacker",
    "secondary_role": "controller",
    "strength_bonus": 3,
    "speed_bonus": 0,
    "will_bonus": 0
}


'''
