# SQLAlchemy Recap

Before going back to yesterday's `twitter-api` repository, let's create a brand new Flask app (without the factory pattern `create_app`) and:

1. Add [psycopg2](http://initd.org/psycopg/) to use PostgreSQL
1. Use [SQLAlchemy](https://www.sqlalchemy.org/) as the ORM on top of PostgreSQL
1. Add [Alembic](http://alembic.zzzcomputing.com/) to manage schema migration with the [`Flask-Migrate`](http://flask-migrate.readthedocs.io/) package.
1. Deploy to Heroku

## PostgreSQL

Head over to [postgresql.org/download/windows/](https://www.postgresql.org/download/windows/) and download the installer for PostgreSQL 10+. Run it. It will install:

- the PostgreSQL Server
- pgAdmin 4, a very useful GUI client to run queries and administrate the server
- Command line tools, useful to install the `psycopg2` package

The setup wizard will ask you for a superadmin password. Put something you can remember easily.

You should leave the port as the default suggested value (`5432`), and choose `English, United States` as the default locale.

## Getting started

Let's start a new repository from scratch:

```bash
cd ~/code/<your_username>
mkdir flask-with-sqlalchemy
cd flask-with-sqlalchemy
git init
pipenv --python 3.7
pipenv install flask psycopg2-binary gunicorn flask-sqlalchemy flask-migrate flask-script
```

```bash
touch wsgi.py
subl . # Open Sublime Text in the current folder.
```

### Flask Boilerplate

In your `wsgi.py` file, copy paste the following boilerplate:

```python
# wsgi.py
from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hello World!"
```

Check that your application is starting with:

```bash
FLASK_ENV=development pipenv run flask run
```

And go to [`localhost:5000/hello`](http://localhost:5000)

We will need to manipulate environment variables to configure access to the database.

```bash
touch .env
echo ".env" >> .gitignore # You don't want to commit your env variables!
```

Let's try this right away. Open the `.env` file in Sublime Text and add a dummy environment variable:

```bash
# .env
DUMMY="dummy"
```

Open the `wsgi.py` file and insert at the beginning of the file the following code:

```bash
import os
import logging
logging.warn(os.environ["DUMMY"])

# [...]
```

Relaunch the `FLASK_ENV=development pipenv run flask run` server. You should see this:

```bash
Loading .env environment variables...
# [...]
WARNING:root:dummy
```

See? It automatically populates the `os.environ` with the content of the `.env` file!

## `Config` class

To prepare for a Heroku deployment, we will tell the Flask application how to connect to the database **through a `DATABASE_URL` environment variable**. We can encapsulate this behavior in a specific file:

```bash
touch config.py
```

```python
# config.py
import os

class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
```

Once we have this file, we can **bind** the Flask application to SQLAlchemy:

```python
# wsgi.py
from flask import Flask
from config import Config
app = Flask(__name__)
app.config.from_object(Config)


from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

# [...]
```

## `DATABASE_URL`

The `DATABASE_URL` environment variable is the cornerstone of the SQLAlchemy configuration. That's where you put all the information needed by the python code to actually connect to the database server.

In development, we will use this:

```bash
# .env
DATABASE_URL="postgresql://postgres:<password_if_necessary>@localhost/flask_db"
```

It means that we are using the PostgreSQL server we installed earlier and the `flask_db` database. Database that we actually need to created!

```bash
export PATH="$PATH:/c/Program Files/PostgreSQL/10/bin"
winpty psql -U postgres -c "CREATE DATABASE flask_db"
```

## Adding our **first** model

Create a new `models.py` file:

```bash
touch models.py
```

```python
# models.py
from wsgi import db

class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    def __repr__(self):
        return '<id {}>'.format(self.id)
```

Once the first model has been created, we can include it into the main file:

```python
# wsgi.py
# [...] After `db = SQLAlchemy(app)`
from models import Product
```

We are now going to set up Alambic to generate our first migration and upgrade the database to actually **create** the `products` table.

```bash
touch manage.py
```

```python
# manage.py
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from wsgi import app, db

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
```

This gives us a `python manage.py` command we can use to first initialize the Alembic files:

```bash
pipenv run python manage.py db init
```

Then we can run a migration to snapshot the state of the `models.py` file:

```bash
pipenv run python manage.py db migrate -m "create products"
```

Open the file in `./migrations/versions` and read the `upgrade()` auto-generated method. Did you see how it creates the two column `id` and `name`?

To apply this migration to the actual database, run this:

```bash
pipenv run python manage.py db upgrade
```

To manually check that the schema now contains a `product` table, re-connect to the PostgreSQL database:

```bash
export PATH="$PATH:/c/Program Files/PostgreSQL/10/bin"
winpty psql -U postgres -d flask_db
flask_db=# \dt
# You should see two tables: `products` and `alembic_version`!
flask_db#= \d products
# You should see the two columns of the table `product`: `id` and `name`
flask_db#= \q
```

See how easy it was?

## Updating a model

Alembic (the package behind `manage.py db`) shines when we update a model. It will automatically generate a new migration with the "diff" on this model definition.

```python
# models.py

class Product(db.Model):
    # [...]
    description = db.Column(db.Text())
```

Go back to the terminal and run the `migrate -m "add description to products"` command. What happened in `migrations/versions`? Read this new file and then run the `upgrade` command. You can check that this worked with:

```bash
export PATH="$PATH:/c/Program Files/PostgreSQL/10/bin"
winpty psql -U postgres -d flask_db
flask_db#= \d products
# You should now see three columns in this table
flask_db#= \q
```

## Inserting a record

Our database schema is ready. We used the command line `psql` to query it. We can now use pgAdmin 4 to query the database for records. Launch pgAdmin from the Windows Start menu. It should open `localhost:53042` in Chrome. In the tree, go to `Servers` > `PostgreSQL 10` > `Databases` > `flask_db` > `Schemas` > `public` > `Tables` > `products` and right clic on it: `View/Edit Data` > `All rows`. It will generate the `SELECT` SQL query for you. Click on the button with a little thunder ⚡️ to run the query. There should be _no_ records.

Let's insert two products in the Database! We can use the [flask shell feature](http://flask.pocoo.org/docs/1.0/cli/#open-a-shell).

```bash
pipenv run flask shell
>>> from models import Product
>>> from wsgi import db
>>> skello = Product()
>>> skello.name = "Skello"
>>> socialive = Product()
>>> socialive.name = "Socialive.tv"
>>> db.session.add(skello)
>>> db.session.add(socialive)
>>> db.session.commit()
>>> quit()
```

Go back to pgAdmin 4 in Chrome and re-click on the thunder ⚡ button. Hooray! You now have two records in the database!

## Creating our first API endpoint

We are going to code the `/products` endpoint, listing _all_ products (we don't paginate here).

Yesterday, we used a fake database and did not had any trouble with `jsonify`. Now that we retrieve data from the database and we use `db.Model` subclasses, we will have **serialization** problems. To anticipate those we must introduce yet another package: [`marshmallow`](https://marshmallow.readthedocs.io/)

```bash
pipenv install flask-marshmallow marshmallow-sqlalchemy
```

We can now instantiate the `Marshmallow` app with:

```python
# wsgi.py

# [...]

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow # Order is important here!
db = SQLAlchemy(app)
ma = Marshmallow(app)
```

We also need to define a serialization schema for each model we want to output as a JSON resource through our API endpoints:

```bash
touch schemas.py
```

```python
# schemas.py
from wsgi import ma
from models import Product

class ProductSchema(ma.Schema):
    class Meta:
        model = Product
        fields = ('id', 'name') # These are the fields we want in the JSON!

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
```

Now we have our schemas we can actually use them and implement our API endpoint!

```python
# wsgi.py
# [...]

from models import Product
from schemas import products_schema

# [...]

@app.route('/products')
def products():
    products = db.session.query(Product).all() # SQLAlchemy request => 'SELECT * FROM products'
    return products_schema.jsonify(products)
```

And that should be it! Launch your server and head to `localhost:5000/products`. You should see the two products in the database as JSON!

## Heroku deployment

It's time to push our awesome code to production. We will create a new Heroku application, but before that we need to set up the `Procfile`. With SQLAlchemy, there is a slight change:

1. We will need to tell Heroku that we need a PostgreSQL database
1. We need Heroku to run `manage.py db upgrade` at every deployment to keep the production database schema in sync with the code!

```bash
touch Procfile
```

```bash
release: python manage.py db upgrade
web: gunicorn wsgi:app --access-logfile=-
```

Let's deploy:

```bash
git add .
git commit -m "First Deployment to Heroku"

heroku create --region=eu
git push heroku master
```

Once more, you can enjoy Heroku's **magic**! From the `Pipfile`, it detected the package psycopg2 so it automatically reserver a (free - hobby plan) PostgreSQL instance and configured the `DATABASE_URL`. You can check it with:

```bash
heroku config:get DATABASE_URL
```

Open your app!

```bash
heroku open
```

:question: You should get the `Hello world` from the Home page. Head to `/products`. How many products do you see? Why is it different from `localhost`?

<details><summary>View solution</summary><p>

The production database and the local (development) database are **different**!

To add products to the production database, you can use the Flask shell, remotely connecting to the Heroku dyno (_à la SSH_):

```bash
heroku run flask shell

>>> from models import Product
>>> from wsgi import db
>>> skello = Product()
>>> skello.name = "Skello"
>>> db.session.add(skello)
>>> db.session.commit()
>>> quit()
```

Now reload the page. See, you get the newly added product!

</p></details>

## Your turn!

We layed down the basic Flask architecture using SQLAlchemy and a serialization package to output JSON from those models. You should now implement the following:

- `READ`: The endpoint to list **a single product** from its id.
- `CREATE`: The endpoint to create a new product from a `POST` request body
- `DELETE`: The endpoint to remove a product from a database
- `UPDATE`: The endpoint to update an existing product from a `PATCH` request body and its id in the URL

These documentation links should help you:

- [SQLAlchemy - `Query.get()`](http://docs.sqlalchemy.org/en/latest/orm/query.html#sqlalchemy.orm.query.Query.get)
- [SQLAlchemy - Adding and Updating Objects](http://docs.sqlalchemy.org/en/latest/orm/tutorial.html#adding-and-updating-objects)
