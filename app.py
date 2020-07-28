import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Race, Char_class, Character
from auth.auth import AuthError, requires_auth, get_token_auth_header

STAT_BASE = 8


def format_list(selection):
    item_list = [item.format() for item in selection]
    return item_list


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/')
    def welcome():
        msg = 'Welcome to CharGen!'
        return msg

    # List all races
    @app.route('/races')
    def get_races():
        race_list = []
        races = Race.query.all()

        for race in races:
            race_list.append(race.format())
        return jsonify({
            'status_code': 200,
            'success': True,
            'number_of_races': len(race_list),
            'race_list': race_list
        })

    @app.route('/classes')
    def get_classes():
        class_list = []
        classes = Char_class.query.all()

        for char_class in classes:
            class_list.append(char_class.format())

        return jsonify({
            'status_code': 200,
            'success': True,
            'number_of_classes': len(class_list),
            'class_list': class_list
        })

    @app.route('/characters')
    def get_characters():
        character_list = []
        characters = Character.query.all()

        for character in characters:
            character_list.append(character.format())

        return jsonify({
            'status_code': 200,
            'success': True,
            'number_of_characters': len(character_list),
            'character_list': character_list
        })

    @app.route('/races', methods=['POST'])
    @requires_auth('post:races')
    def create_race(payload):
        body = request.get_json()
        name = body.get('name', None)
        max_age = body.get('max_age', None)
        strength_bonus = body.get('strength_bonus', None)
        speed_bonus = body.get('speed_bonus', None)
        will_bonus = body.get('will_bonus', None)
        try:
            new_race = Race(
                name=name,
                max_age=max_age,
                strength_bonus=strength_bonus,
                speed_bonus=speed_bonus,
                will_bonus=will_bonus
            )
            new_race.insert()
            race_list = format_list(Race.query.all())

            return jsonify({
                'success': True,
                'created_id': new_race.id,
                'race_list': race_list,
                'number_of_races': len(race_list)
            })
        except BaseException:
            abort(422)

    @app.route('/classes', methods=['POST'])
    @requires_auth('post:classes')
    def create_class(payload):
        body = request.get_json()
        name = body.get('name', None)
        primary_role = body.get('primary_role', None)
        secondary_role = body.get('secondary_role', None)
        strength_bonus = body.get('strength_bonus', None)
        speed_bonus = body.get('speed_bonus', None)
        will_bonus = body.get('will_bonus', None)
        try:
            new_class = Char_class(
                name=name,
                primary_role=primary_role,
                secondary_role=secondary_role,
                strength_bonus=strength_bonus,
                speed_bonus=speed_bonus,
                will_bonus=will_bonus
            )
            new_class.insert()
            class_list = format_list(Char_class.query.all())

            return jsonify({
                'success': True,
                'created_id': new_class.id,
                'class_list': class_list,
                'number_of_classes': len(class_list)
            })
        except BaseException:
            abort(422)

    @app.route('/characters', methods=['POST'])
    @requires_auth('post:characters')
    def create_character(payload):
        body = request.get_json()
        first_name = body.get('first_name', None)
        last_name = body.get('last_name', None)
        char_class_id = body.get('char_class_id', None)
        race_id = body.get('race_id', None)
        try:
            race = Race.query.get(race_id)
            char_class = Char_class.query.get(char_class_id)
            new_character = Character(
                first_name=first_name,
                last_name=last_name,
                char_class_id=char_class_id,
                race_id=race_id,
                strength=race.strength_bonus+char_class.strength_bonus+STAT_BASE,
                speed=race.speed_bonus+char_class.speed_bonus+STAT_BASE,
                will=race.will_bonus+char_class.will_bonus+STAT_BASE
            )
            new_character.insert()
            character_list = format_list(Character.query.all())

            return jsonify({
                'success': True,
                'created_id': new_character.id,
                'character_list': character_list,
                'number_of_characters': len(character_list)
            })
        except BaseException:
            abort(422)

    @app.route('/races/<int:race_id>', methods=['DELETE'])
    @requires_auth('delete:races')
    def delete_race(payload, race_id):
        race = Race.query.filter(Race.id == race_id).one_or_none()
        if race is None:
            abort(404)
        else:
            try:
                race.delete()
                race_list = format_list(Race.query.all())
                return jsonify({
                    'success': True,
                    'deleted_id': race.id,
                    'race_list': race_list,
                    'number_of_races': len(race_list)
                })
            except BaseException:
                abort(422)

    @app.route('/classes/<int:class_id>', methods=['DELETE'])
    @requires_auth('delete:classes')
    def delete_class(payload, class_id):
        char_class = Char_class.query.filter(
            Char_class.id == class_id).one_or_none()
        if char_class is None:
            abort(404)
        else:
            try:
                char_class.delete()
                class_list = format_list(Char_class.query.all())
                return jsonify({
                    'success': True,
                    'deleted_id': char_class.id,
                    'class_list': class_list,
                    'number_of_classes': len(class_list)
                })
            except BaseException:
                abort(422)

    @app.route('/characters/<int:character_id>', methods=['DELETE'])
    @requires_auth('delete:characters')
    def delete_character(payload, character_id):
        character = Character.query.filter(
            Character.id == character_id).one_or_none()
        if character is None:
            abort(404)
        else:
            try:
                character.delete()
                character_list = format_list(Character.query.all())
                return jsonify({
                    'success': True,
                    'deleted_id': character.id,
                    'character_list': character_list,
                    'number_of_characters': len(character_list)
                })
            except BaseException:
                abort(422)

    @app.route('/races/<int:race_id>', methods=['PATCH'])
    @requires_auth('post:races')
    def update_race(payload, race_id):
        body = request.get_json()
        race = Race.query.filter(Race.id == race_id).one_or_none()
        if race is None:
            abort(404)
        elif body is None:
            abort(404)
        else:
            try:
                # print(body)
                if "name" in body:
                    race.name = body.get("name")
                if "max_age" in body:
                    race.max_age = body.get("max_age")
                if "strength_bonus" in body:
                    race.strength_bonus = body.get("strength_bonus")
                if "speed_bonus" in body:
                    race.speed_bonus = body.get("speed_bonus")
                if "will_bonus" in body:
                    race.will_bonus = body.get("will_bonus")

                race.update()
                updated_race = Race.query.get(race_id)

                return jsonify({
                    'success': True,
                    'updated_race': updated_race.format()
                })
            except BaseException:
                abort(422)

    @app.route('/classes/<int:class_id>', methods=['PATCH'])
    @requires_auth('post:classes')
    def update_class(payload, class_id):
        body = request.get_json()
        char_class = Char_class.query.filter(
            Char_class.id == class_id).one_or_none()
        if char_class is None:
            abort(404)
        elif body is None:
            abort(404)
        else:
            try:
                if "name" in body:
                    char_class.name = body.get("name")
                if "primary_role" in body:
                    char_class.primary_role = body.get("primary_role")
                if "secondary_role" in body:
                    char_class.secondary_role = body.get("secondary_role")
                if "strength_bonus" in body:
                    char_class.strength_bonus = body.get("strength_bonus")
                if "speed_bonus" in body:
                    char_class.speed_bonus = body.get("speed_bonus")
                if "will_bonus" in body:
                    char_class.will_bonus = body.get("will_bonus")

                char_class.update()
                updated_class = Char_class.query.get(class_id)

                return jsonify({
                    'success': True,
                    'updated_class': updated_class.format()
                })
            except BaseException:
                abort(422)

    @app.route('/characters/<int:character_id>', methods=['PATCH'])
    @requires_auth('post:characters')
    def update_character(payload, character_id):
        body = request.get_json()
        character = Character.query.filter(
            Character.id == character_id).one_or_none()
        if character is None:
            abort(404)
        elif body is None:
            abort(404)
        else:
            try:
                if "first_name" in body:
                    character.first_name = body.get("first_name")
                if "last_name" in body:
                    character.last_name = body.get("last_name")
                if "char_class_id" in body:
                    character.char_class_id = body.get("char_class_id")
                if "race_id" in body:
                    character.race_id = body.get("race_id")
                if "strength" in body:
                    character.strength = body.get("strength")
                if "speed" in body:
                    character.speed = body.get("speed")
                if "will" in body:
                    character.will = body.get("will")

                character.update()
                updated_character = Character.query.get(character_id)

                return jsonify({
                    'success': True,
                    'updated_character': updated_character.format()
                })
            except BaseException:
                abort(422)

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "unauthorized"
        }), 401

    @app.errorhandler(AuthError)
    def forbidden(error):
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error['code'],
        }), error.status_code

    return app


APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
