## Setup Process

Based on the OS you are using you may have to setup things differently. But requirements
are python 3, github, postgres. I strongly recommend using MacOS or Ubunutu. If you are using Windows
please find alternate options to run flask, postgres, app in that OS.

### Environment Setup

1. Setup python virtual environment: Important because you keep this project separate from other python projects

2. When you activate your virtual environment it uses python installed, note that python version should be 3.6.2 or above

3. Clone this repo:
```bash
https://github.com/e911/FLask-Basic-CRUD-Api.git
```

4. Activate your virtual environment that you setup.

5. Create Flask config environment in .bash_profile or .zshrc depending on your shell
   export FLASK_CONFIG='development'

### Create Database in postgres

Install postgres database. Depending on your operating system
http://www.postgresqltutorial.com/install-postgresql/

```bash
sudo su - postgres
```
```postgres
psql -d template1

template1=# create database ramrios_candidate;

template1=# create user ramrios_candidate password 'ramrios_candidate';
CREATE ROLE
ramrios_dev=# grant all privileges on database ramrios_candidate to ramrios_candidate;
GRANT
ramrios_dev=# alter database ramrios_candidate owner to ramrios_candidate;
ALTER DATABASE

type \q to exit from psql console
```

### Setup Flask Backend

1. activate virtual environment. If you are using mkvirtualenv eg; command below
   ```bash
   mkvirtualenv activate <<your_virtual_environment>>
   ```

2. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```

3. Create backend objects (note this will run all the migrations)
    ```bash
    python manage.py db upgrade head
    ```

4. Run Backend server
    ```bash
    python manage.py runserver
    ```

    http://localhost:5000  is default backend API

### Test your setup

Please test after you successfully deploy the code above.

Creating user: Endpoint URI: http://localhost:5000/users/create_user

Curl Example: You can use any Rest client doing below

```bash 
curl -d '{"email":"you@numweb.com", "password":"topsecret"}' -H "Content-Type: application/json" -X POST http://localhost:5000/users/create_user
```

Backend table will have one record with email you@numweb.com

From your browser call http://localhost:5000/users this will list the users you have created.


Creating appointment: Endpoint URI: http://localhost:5000/appointments/create_appointment

Curl Example: You can use any Rest client doing below

```bash
curl -d '{"client_name":"Pujan Thapa", "preferred_clinician":"Poojan Thapa","appointment_reason":"Business deal"}' -H "Content-Type: application/json" -X POST http://localhost:5000/appointments/create_appointment
```

Backend table will have one record.

From your browser call http://localhost:5000/appointments this will list the appointments you have created.
