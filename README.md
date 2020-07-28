# Full Stack Nanodegree Capstone Project

## Background

This project shows many of the skills and tools I've learned through the Full Stack Nanodegree (FSND) course offered by Udacity.
This project began with no template - I referenced many of my other projects and built this one from scratch.
I intend to build more onto this project in the future.

Shoutout to the README boiler plate creators - You make documentation much easier after a night of little sleep. 


## Getting Started

As of this posting this service is publically availible on Heroku at the following address:

    https://sw-char-gen.herokuapp.com/


## Local Quick Start

###Prepare your environment and app

Start Postgresql

* install postgres if needed
* create a database
* save the database, username, and password someplace handy

####Clone the repository
```bash
https://github.com/SethW89/sw-char-gen
```

####Update the models.py
Update the database name and configure the database path with username and password if you have one.


## Running the server

To run the server, execute:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `app.py` directs flask to use the `app.py` file as the application. 

### Roles and Permissions

There are three roles with different permissions setup for this api:

Anyone!

- Can view races, classes, and characters.

User

- All permissions above
- can create and edit characters.

User Authentication Token
```bash
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IllLRm02M1lqekRIcmlyZGtZNmhtVSJ9.eyJpc3MiOiJodHRwczovL3NldGh3dGVzdC5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWViMWQyYzI1NGIxNGMwYzEyN2E2NGEwIiwiYXVkIjoiQ2hhcmFjdGVycyIsImlhdCI6MTU5NTk1MzEzNiwiZXhwIjoxNTk2MDM5NTM2LCJhenAiOiJYc3JJdklLODV4dm02dXZLRjkxM1hNcXduTXF2NTV3dSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmNoYXJhY3RlcnMiLCJnZXQ6Y2xhc3NlcyIsImdldDpyYWNlcyIsInBvc3Q6Y2hhcmFjdGVycyJdfQ.hUOPRACZIYj4WuM_IPbuQQQahlSJ9nLDThBKJH9zM1gM1mOrJldrfhFRg1he3fS1qcZMB3vdIehdG18ZFF5zWEJYaVu4uEyB-ajcm-ZdiVVw-oLpyD8mflG_WbfRwKB2VtK00dNqgDNQP8RE23AFtzHfubua6MZimoxipawizDnkUvv2BSAyrOXHsUuzXmnqViwspnW_SO8g9ELVg2kID2S0a2TS3C2zDUJDhIM3rmCZMt00F-SrjUCIH0j4wld9Dn6S_7lrLBkZ1umGtMOTFz2wNWWW9E4hTj44hy1dpeBesxNgBZWsl6HECGFTtHH7KTwKH0Q18CZfjY-XB1erVg
```

Admin

- All permissions above
- Can create races, classes, and characters
- Can edit races, classes, and characters
- Can delete races, classes, and characters

Admin Authentication Token
```bash
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IllLRm02M1lqekRIcmlyZGtZNmhtVSJ9.eyJpc3MiOiJodHRwczovL3NldGh3dGVzdC5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDQzODMxNzU2NTQ2OTczNDc4ODgiLCJhdWQiOlsiQ2hhcmFjdGVycyIsImh0dHBzOi8vc2V0aHd0ZXN0LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1OTU5NTE1MzQsImV4cCI6MTU5NjAzNzkzNCwiYXpwIjoiWHNySXZJSzg1eHZtNnV2S0Y5MTNYTXF3bk1xdjU1d3UiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmNoYXJhY3RlcnMiLCJkZWxldGU6Y2xhc3NlcyIsImRlbGV0ZTpyYWNlcyIsImdldDpjaGFyYWN0ZXJzIiwiZ2V0OmNsYXNzZXMiLCJnZXQ6cmFjZXMiLCJwb3N0OmNoYXJhY3RlcnMiLCJwb3N0OmNsYXNzZXMiLCJwb3N0OnJhY2VzIl19.Sa_Wi2W4Wt6XZ1TM3RXLnYas8lpy78QDo3O5JxnvWMZeAPz2pCfTLP5IDGJlJHxdEloPaIQH3hH7gBWAEitSKlKL5vbg4Zi1hK7Fp1vMeCnJDokxM_Dj1n904VIQy4yQWfVS_43N4_YM8wHbl_bZkxVnoPOAQ7Ii2qHFTG3x8qAsX0tS5uwlb8VdlRljw5nGPphOwBDaJbUnmNCXXK9xRpu7h8TUJSLUUnNTZv49VqK4WScHEdWFQp6BQY94PignqEQPUIYlGSLzqKX4nfR_y3c-AOMv0QY7UQpC6vhyQiHsTKu6H5JGlDufTRH7WCWvav_43Qhtwc0Z9hKBw5B_Lg
```

## Resource endpoint library

Endpoints

- GET '/races'
- GET '/classes'
- GET '/characters'
- POST '/races'
- POST '/classes'
- POST '/characters'
- DELETE '/races/<int:race_id>'
- DELETE '/classes/<int:class_id>'
- DELETE '/characters/<int:character_id>'
- PATCH '/races/<int:race_id>'
- PATCH '/classes/<int:class_id>'
- PATCH '/characters/<int:character_id>'

GET '/races' 

- Fetches a list of races.
- Returns:
    - Success value
    - Status code
    - The number of races in the database
    - A list of all races

```bash
{
    "number_of_races": 2,
    "race_list": [
        {
            "id": 1,
            "max_age": 750,
            "name": "Elf",
            "speed_bonus": 1,
            "strength_bonus": 0,
            "will_bonus": 2
        },
        {
            "id": 2,
            "max_age": 750,
            "name": "Dwarf",
            "speed_bonus": 0,
            "strength_bonus": 2,
            "will_bonus": 1
        }
    ],
    "status_code": 200,
    "success": true
}
```

GET '/classes' 

- Fetches a list of classes.
- Returns:
    - Success value
    - Status code
    - The number of classes in the database
    - A list of all classes

```bash
{
    "class_list": [
        {
            "id": 1,
            "name": "Wizard",
            "primary_role": "ranged_attacker",
            "secondary_role": "controller",
            "speed_bonus": 0,
            "strength_bonus": 0,
            "will_bonus": 3
        },
        {
            "id": 2,
            "name": "Druid",
            "primary_role": "supporter",
            "secondary_role": "ranged_attacker",
            "speed_bonus": 1,
            "strength_bonus": 0,
            "will_bonus": 2
        }
    ],
    "number_of_classes": 2,
    "status_code": 200,
    "success": true
}
```

GET '/characters' 

- Fetches a list of characters.
- Returns:
    - Success value
    - Status code
    - The number of characters in the database
    - A list of all characters

```bash
{
    "character_list": [
        {
            "char_class_id": 1,
            "first_name": "Dude",
            "id": 1,
            "last_name": "Bar",
            "race_id": 1,
            "speed": 9,
            "strength": 8,
            "will": 11
        }
    ],
    "number_of_characters": 1,
    "status_code": 200,
    "success": true
}
```

POST '/races'

- Creates a new race. See example for required infomration.
- Returns:
    - Success value
    - Created id
    - Race list
    - Number of races in the database
Example race:
```bash
{
    "name": "Human",
    "max_age": 90,
    "strength_bonus": 1,
    "speed_bonus": 1,
    "will_bonus": 1
}
```
Results:
```bash
{
    "created_id": 4,
    "number_of_races": 2,
    "race_list": [
        {
            "id": 1,
            "max_age": 750,
            "name": "Elf",
            "speed_bonus": 1,
            "strength_bonus": 0,
            "will_bonus": 2
        },
        {
            "id": 4,
            "max_age": 90,
            "name": "Human",
            "speed_bonus": 1,
            "strength_bonus": 1,
            "will_bonus": 1
        }
    ],
    "success": true
}
```

POST '/classes'

- Creates a new class. See example for required infomration.
- Returns:
    - Success value
    - Created id
    - Class list
    - Number of classes in the database
Example class:
```bash
{
    "name": "Paladin",
    "primary_role": "supporter",
    "secondary_role": "melee_attacker",
    "strength_bonus": 2,
    "speed_bonus": 0,
    "will_bonus": 1
}
```
Results:
```bash
{
    "class_list": [
        {
            "id": 1,
            "name": "Wizard",
            "primary_role": "ranged_attacker",
            "secondary_role": "controller",
            "speed_bonus": 0,
            "strength_bonus": 0,
            "will_bonus": 2
        },
        {
            "id": 3,
            "name": "Paladin",
            "primary_role": "supporter",
            "secondary_role": "melee_attacker",
            "speed_bonus": 0,
            "strength_bonus": 2,
            "will_bonus": 1
        }
    ],
    "created_id": 3,
    "number_of_classes": 2,
    "success": true
}
```
POST '/characters'

- Creates a new character. See example for required infomration.
- Returns:
    - Success value
    - Created id
    - Race list
    - Number of races in the database
Example character:
```bash
{
    "first_name": "Wally",
    "last_name": "West",
    "race_id": 1,
    "char_class_id": 1
}
```
Results:
```bash
{
    "character_list": [
        {
            "char_class_id": 1,
            "first_name": "Dude",
            "id": 1,
            "last_name": "Bar",
            "race_id": 1,
            "speed": 9,
            "strength": 8,
            "will": 11
        },
        {
            "char_class_id": 1,
            "first_name": "Wally",
            "id": 2,
            "last_name": "West",
            "race_id": 1,
            "speed": 9,
            "strength": 8,
            "will": 11
        }
    ],
    "created_id": 2,
    "number_of_characters": 2,
    "success": true
}
```

DELETE '/races/<int:race_id>'

- Deletes a race with a given id
- Returns:
    - Success value
    - Status code
    - Id of the deleted race
    - Number of races in the database

```bash
{
    "deleted_id": 4,
    "number_of_races": 1,
    "race_list": [
        {
            "id": 1,
            "max_age": 750,
            "name": "Elf",
            "speed_bonus": 1,
            "strength_bonus": 0,
            "will_bonus": 1
        },
    ],
    "success": true
}
```

DELETE '/classes/<int:class_id>'

- Deletes a class with a given id
- Returns:
    - Success value
    - Status code
    - Id of the deleted class
    - Number of classes in the database

```bash
{
    "class_list": [
        {
            "id": 1,
            "name": "Wizard",
            "primary_role": "ranged_attacker",
            "secondary_role": "controller",
            "speed_bonus": 0,
            "strength_bonus": 0,
            "will_bonus": 2
        }
    ],
    "deleted_id": 3,
    "number_of_classes": 1,
    "success": true
}
```

DELETE '/characters/<int:character_id>'

- Deletes a character with a given id
- Returns:
    - Success value
    - Status code
    - Id of the deleted character
    - Number of characters in the database

```bash
{
    "character_list": [
        {
            "char_class_id": 1,
            "first_name": "Dude",
            "id": 1,
            "last_name": "Bar",
            "race_id": 1,
            "speed": 9,
            "strength": 8,
            "will": 11
        }
    ],
    "deleted_id": 2,
    "number_of_characters": 1,
    "success": true
}
```

PATCH '/races/<int:race_id>'

- Updates a race with a given id.
- Returns:
    - Success value
    - Status code
    - Updated data for that class

Example update:
```bash
{
    "max_age": 120,
    "strength_bonus": 4
}
```
```bash
{
    "success": true,
    "updated_race": {
        "id": 1,
        "max_age": 120,
        "name": "Elf",
        "speed_bonus": 1,
        "strength_bonus": 4,
        "will_bonus": 1
    }
}
```
PATCH '/classes/<int:class_id>'

- Updates a class with a given id.
- Returns:
    - Success value
    - Status code
    - Updated data for that class

Example update:
```bash
{
    "name": "Buff Dude",
    "strength_bonus": 4,
    "will_bonus": 0
}
```
```bash
{
    "success": true,
    "updated_class": {
        "id": 2,
        "name": "Buff Dude",
        "primary_role": "ranged_attacker",
        "secondary_role": "controller",
        "speed_bonus": 0,
        "strength_bonus": 4,
        "will_bonus": 0
    }
}
```

PATCH '/characters/<int:character_id>'

- Updates a character with a given id.
- Returns:
    - Success value
    - Status code
    - Updated data for that character

Example update:
```bash
{
    "first_name": "Goose",
    "last_name": "Duckerson"
}
```
```bash
{
    "success": true,
    "updated_character": {
        "char_class_id": 1,
        "first_name": "Goose",
        "id": 1,
        "last_name": "Duckerson",
        "race_id": 1,
        "speed": 9,
        "strength": 8,
        "will": 11
    }
}
```


### Errors Handled

Errors that will be handled are:

- 422 - Unprocessable
- 404 - Resource not found
- 401 - Unauthorized

Errors will include a success value, message, and error value.

Example error response
```bash
{
    "error": 401,
    "message": "token_expired",
    "success": false
}
```