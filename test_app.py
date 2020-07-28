import os
import unittest
import json

from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import *


admin_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IllLRm02M1lqekRIcmlyZGtZNmhtVSJ9.eyJpc3MiOiJodHRwczovL3NldGh3dGVzdC5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDQzODMxNzU2NTQ2OTczNDc4ODgiLCJhdWQiOlsiQ2hhcmFjdGVycyIsImh0dHBzOi8vc2V0aHd0ZXN0LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1OTU3MzQwNjUsImV4cCI6MTU5NTgyMDQ2NSwiYXpwIjoiWHNySXZJSzg1eHZtNnV2S0Y5MTNYTXF3bk1xdjU1d3UiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmNoYXJhY3RlcnMiLCJkZWxldGU6Y2xhc3NlcyIsImRlbGV0ZTpyYWNlcyIsImdldDpjaGFyYWN0ZXJzIiwiZ2V0OmNsYXNzZXMiLCJnZXQ6cmFjZXMiLCJwb3N0OmNoYXJhY3RlcnMiLCJwb3N0OmNsYXNzZXMiLCJwb3N0OnJhY2VzIl19.agPO71Y9urQC9Mz55wMcoFCq0gfyQdhIrIO8Is4v3aqpiMENFEuHiWGOAqR32lSlPme1dznRb_pz-I3f9oIfnULIEPmCVe704BUUF6PIaEQ8To4_9eg8Kt8fqBDIS6qkAFynw6g_TPbSKjZZ8dBcCeJXubrKi5An8Iv1ZMewCKfTZR-A0FgF_LSSs5avajeIyny25tBCAVMtQ0CLolyTP4FGOPMbSQ0lljXbNF6KTImFzoU_A8Mw5RGwY773qVnI_C-GM7s9BcMYIOYzUjQEfcJbTPLgCTf6j_wmn_ZP8mBGVsOdzgZEvtMTL9ohfge7hpTevLZE4zyxZfCW2GmJUw'
user_token = 'sdfsdaf'


class CharGenTests(unittest.TestCase):
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "CharGen_test"
        self.database_path = "postgresql://{}/{}".format(
            'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_race = {
            "name": "Dwarf",
            "max_age": 450,
            "strength_bonus": 2,
            "speed_bonus": 0,
            "will_bonus": 1
        }
        self.patch_race = {
            "name": "Dwarf",
            "max_age": 450,
            "strength_bonus": 2,
            "speed_bonus": 0,
            "will_bonus": 1
        }

        self.new_class = {
            "name": "Wizard",
            "primary_role": "ranged_attacker",
            "secondary_role": "controller",
            "strength_bonus": 0,
            "speed_bonus": 0,
            "will_bonus": 3
        }

        self.new_character = {
            "first_name": "Foo",
            "last_name": "Bar",
            "race_id": 1,
            "char_class_id": 1
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        pass

    # Tests for POST (Race, Class, Character) RABC is seen with User/Admin
    def test_01_admin_post_to_races_200(self):
        res = self.client().post('/races',
                                 headers={"Authorization": "Bearer {}".format(admin_token)}, json=self.new_race)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['race_list'])
        self.assertTrue(data['created_id'])
        self.assertTrue(data['number_of_races'])

    def test_01_admin_post_to_races_422(self):
        res = self.client().post('/races',
                                 headers={"Authorization": "Bearer {}".format(admin_token)}, json=self.new_class)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    def test_01_user_post_to_races_401(self):
        res = self.client().post('/races',
                                 headers={"Authorization": "Bearer {}".format(user_token)}, json=self.new_race)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_01_admin_post_to_classes_200(self):
        res = self.client().post('/classes',
                                 headers={"Authorization": "Bearer {}".format(admin_token)}, json=self.new_class)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['class_list'])
        self.assertTrue(data['created_id'])
        self.assertTrue(data['number_of_classes'])

    def test_01_admin_post_to_classes_422(self):
        res = self.client().post('/classes',
                                 headers={"Authorization": "Bearer {}".format(admin_token)}, json=self.new_character)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    def test_01_user_post_to_classes_401(self):
        res = self.client().post('/classes',
                                 headers={"Authorization": "Bearer {}".format(user_token)}, json=self.new_class)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    # Note: Character tests cannot run until race and class have been created
    def test_02_admin_post_to_characters_200(self):
        res = self.client().post('/characters',
                                 headers={"Authorization": "Bearer {}".format(admin_token)}, json=self.new_character)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['character_list'])
        self.assertTrue(data['created_id'])
        self.assertTrue(data['number_of_characters'])

    def test_02_user_post_to_characters_200(self):
        res = self.client().post('/characters',
                                 headers={"Authorization": "Bearer {}".format(user_token)}, json=self.new_character)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['character_list'])
        self.assertTrue(data['created_id'])
        self.assertTrue(data['number_of_characters'])

    def test_02_admin_post_to_characters_422(self):
        res = self.client().post('/characters',
                                 headers={"Authorization": "Bearer {}".format(admin_token)}, json=self.new_race)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

# Tests for GET

    def test_03_get_races_200(self):
        res = self.client().get(
            '/races', headers={"Authorization": "Bearer {}".format(admin_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['race_list'])
        self.assertTrue(data['number_of_races'])

    def test_03_get_classes_200(self):
        res = self.client().get(
            '/classes', headers={"Authorization": "Bearer {}".format(admin_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['class_list'])
        self.assertTrue(data['number_of_classes'])

    def test_03_get_characters_200(self):
        res = self.client().get(
            '/characters', headers={"Authorization": "Bearer {}".format(admin_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['character_list'])
        self.assertTrue(data['number_of_characters'])

# Tests for PATCH

    def test_04_patch_to_races_200(self):
        res = self.client().patch(f'/races/1',
                                  headers={"Authorization": "Bearer {}".format(admin_token)}, json={"name": "Foo"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['updated_race'])

    def test_04_patch_to_races_404(self):
        res = self.client().patch(f'/races/0',
                                  headers={"Authorization": "Bearer {}".format(admin_token)}, json={"name": "Foo"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_04_patch_to_classes_200(self):
        res = self.client().patch(f'/classes/1',
                                  headers={"Authorization": "Bearer {}".format(admin_token)}, json={"name": "Foo"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['updated_class'])

    def test_04_patch_to_classes_404(self):
        res = self.client().patch(f'/classes/0',
                                  headers={"Authorization": "Bearer {}".format(admin_token)}, json={"name": "Foo"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_04_patch_to_characters_200(self):
        res = self.client().patch(f'/characters/1',
                                  headers={"Authorization": "Bearer {}".format(admin_token)}, json={"first_name": "Foo"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['updated_character'])

    def test_04_admin_patch_to_characters_404(self):
        res = self.client().patch(f'/characters/0',
                                  headers={"Authorization": "Bearer {}".format(admin_token)}, json={"name": "Foo"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

# Tests for DELETE

    def test_05_DELETE_to_races_200(self):
        res = self.client().post('/races',
                                 headers={"Authorization": "Bearer {}".format(admin_token)}, json=self.new_race)
        data = json.loads(res.data)
        res = self.client().delete(
            f'/races/3', headers={"Authorization": "Bearer {}".format(admin_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['number_of_races'])

    def test_05_DELETE_to_races_404(self):
        res = self.client().delete(
            f'/races/0', headers={"Authorization": "Bearer {}".format(admin_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_05_DELETE_to_classes_200(self):
        res = self.client().post('/classes',
                                 headers={"Authorization": "Bearer {}".format(admin_token)}, json=self.new_class)
        data = json.loads(res.data)
        res = self.client().delete(
            f'/classes/3', headers={"Authorization": "Bearer {}".format(admin_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['number_of_classes'])

    def test_05_DELETE_to_classes_404(self):
        res = self.client().delete(
            f'/classes/0', headers={"Authorization": "Bearer {}".format(admin_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_05_DELETE_to_characters_200(self):
        res = self.client().post('/characters',
                                 headers={"Authorization": "Bearer {}".format(admin_token)}, json=self.new_character)
        data = json.loads(res.data)
        res = self.client().delete(
            f'/characters/1', headers={"Authorization": "Bearer {}".format(admin_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['number_of_characters'])

    def test_05_DELETE_to_characters_404(self):
        res = self.client().delete(
            f'/characters/0', headers={"Authorization": "Bearer {}".format(admin_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
