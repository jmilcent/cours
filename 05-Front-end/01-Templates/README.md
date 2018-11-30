# Flask templates

In this exercise, we will re-use the yesterday's application from the [01-SQLAlchemy-Recap](../../04-Database/01-SQLAlchemy-Recap) exercise:

```bash
cd ~/code/<github_username>/flask-with-sqlalchemy
```

Make sure your `git status` is clean (`add` and `commit` the WIP), and that your server can still be started:

```bash
FLASK_ENV=development pipenv run flask run
```

## Homepage

The goal of this exercise will be to replace the following action:

```python
@app.route('/')
def hello():
    return "Hello World!"
```

Instead of returning a plain text sentence, we want to actually build a nice html pages. This time, we won't guide you too much to achieve the result, but give you some pointers:

We want you to build two pages: a home page with a grid of products (`/`), and a dynamic "show" page with a given product (`/:id`). When a user browses the home page, it should be able to easily go to a "show" page with a click on a link

First take some time to read the [Flask Templates](http://flask.pocoo.org/docs/1.0/tutorial/templates/) documentation. This is part of the `flask` package. Take also some time to read more about [Jinja](http://jinja.pocoo.org/docs/2.10/templates/), the templating language used by Flask.

```bash
mkdir templates
touch templates/base.html
```

Let's start with the [Bootstrap template](https://getbootstrap.com/docs/4.1/getting-started/introduction/) adapted to insert a Jinja **block**

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css">

    <title>Products</title>
  </head>
  <body>
    <div class="container">
      {% block content %}{% endblock %}
    </div>

    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"></script>
  </body>
</html>

```

In the controller (`wsgi.py`, you can instantiate

```python
from flask import Flask, render_template

# [...]

    # Use this in the home route
    products = db.session.query(Product).all()
    return render_template('home.html', products=products)
```

Now you can create a new file `templates/home.html` and use the `products` variable you passed thanks to `render_template`:

```html
{% extends 'base.html' %}

{% block content %}
  <h1>Products</h1>

  <ul class="list-unstyled">
    {% for product in products %}
      <li>{{ product.name }}</li>
    {% endfor %}
  </ul>
{% endblock %}
```

The `list-unstyled` class is from [Bootstrap](https://getbootstrap.com/docs/4.1/content/typography/#unstyled).

The content within the `block content` is inserted back into the `base.html`.

## Product page

Now it's your turn to do some work. We want you to add a route to display information about a single product. Put links (`<a href=""></a>`) from the home page to this new page.

Don't hesitate to enrich the `Product` model with other fields and enrich the existing data in the database (via `flask shell` for instance).

**NB**: Those endpoints are different from the API endpoints we implemented yesterday. Don't try to tie them together!
