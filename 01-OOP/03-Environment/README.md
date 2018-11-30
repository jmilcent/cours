# Environment

Another way of modifying the behavior of a Python script (other than command line arguments) is to use the **environment variables**.

## Getting started

```bash
cd ~/code/<your_username>/reboot-python
cd 01-OOP/03-Environment
subl .
pipenv run nosetests
pipenv run pylint flask_option.py
```

## Exercise

Open the `flask_option.py` file and implement the `start` method. It should return a `String` depending on the presence and value of the `FLASK_ENV` environment variable.

Here is the expected behavior:

```bash
FLASK_ENV=development pipenv run python flask_option.py
# => "Starting in development mode..."

FLASK_ENV=production pipenv run python flask_option.py
# => "Starting in production mode..."

pipenv run python flask_option.py
# => "Starting in production mode..."
```

:bulb: **Tip**: have a look at the [`os`](https://docs.python.org/3/library/os.html) module.
