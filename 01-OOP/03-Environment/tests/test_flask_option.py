import os
from nose.tools import eq_
from flask_option import start

def test_start_with_flask_env_development():
    os.environ['FLASK_ENV'] = 'development'
    eq_(start(), "Starting in development mode...")

def test_start_with_flask_env_production():
    os.environ['FLASK_ENV'] = 'production'
    eq_(start(), "Starting in production mode...")

def test_start_with_no_flask_env():
    del os.environ['FLASK_ENV']
    eq_(start(), "Starting in production mode...")
