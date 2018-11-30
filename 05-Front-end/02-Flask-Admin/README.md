## Flask Admin

If you want to easily add a back-office to your application, the [`flask-admin`](https://flask-admin.readthedocs.io/en/latest/) package might help you. The main idea of this package is to build a simple CRUD app from a few python lines.

Here is a [live example](http://examples.flask-admin.org/sqla/simple/admin/post/) of this tool

## Product back-office

Once again, we can use our product app to test the `flask-admin` package:

```bash
cd ~/code/<github_username>/flask-with-sqlalchemy
```

Make sure your `git status` is clean and don't forget to work in a branch! This way it's easy to [discard the WIP](https://stackoverflow.com/a/14075772/197944).

```bash
git checkout -b experiment-with-flask-admin
```

Jump straight to the [Getting Started](https://flask-admin.readthedocs.io/en/latest/introduction/#getting-started) part of the documentation. The important lines are:

```python
from flask_admin import Admin

# [...] Flask `app` and `db` creation

admin = Admin(app, name='Back-office', template_mode='bootstrap3')
admin.add_view(ModelView(Product, db.session)) # `Product` needs to be imported before
```

Your new endpoint will be available at `/admin` ! Of course that's something you may need to [protect](https://flask-admin.readthedocs.io/en/latest/introduction/#authorization-permissions) in a real-life situation.
