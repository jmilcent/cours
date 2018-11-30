# Authentication

Let's go back to our Twitter API:

```bash
mkdir -p ~/code/ssaunier
cd ~/code/ssaunier
git clone git@github.com:ssaunier/twitter-api.git
cd twitter-api
git checkout sqlalchemy

pipenv install --dev
```

Let's reset the DB:

```bash
touch .env
```

```bash
# .env
DATABASE_URL="postgresql://postgres:<password_if_necessary>@localhost/flask_db"
```

```bash
winpty psql -U postgres -c "DROP DATABASE twitter_api_flask"
winpty psql -U postgres -c "CREATE DATABASE twitter_api_flask"

pipenv run python manage.py db upgrade
```

All the API endpoints are available for anyone to call. Nothing is protected. Still, we need to apply some basic security rules like:

- A user must be "logged in" to the API to create a Tweet
- Only a user may delete their tweet
- etc.

## Key Based Authentication

You should have a `User` model. If you don't, add one.

Add a new column to your model: `api_key`. The goal is to store a long, unique and random token for a user at creation. You can achieve this with a [`before_insert` event](https://stackoverflow.com/a/12513904/197944).

Once a user has an API key, implement the logic to make sure that a valid user can create a tweet / only a tweet author can delete his/her tweet.

The API key can be used in the `Authorization` HTTP request header or an `?api_key=...` query string argument. A handy package to implement this feature is [`flask-login`](https://flask-login.readthedocs.io/en/latest/).

We want to protect the following three APIs routes behind a user auth (as a tweet can be only maniupated by its creator)

- `POST /tweets/` (we need a login user to tie it to the new tweet)
- `PATCH /tweets/1` (only the tweet author can edit it)
- `DELETE /tweets/1` (only the tweet author can delete it)


## OAuth with a sample code

```bash
pipenv install flask-oauthlib
```

Consider the official Twitter API, or the GitHub API. THey both provide authentication through OAuth meaning they allow third-party developers to let their users connect to Twitter/GitHub and grand access to a given `scope` of their API.

As we are building an API ourselves, we may want to protect it using the same kind of mechanism. Instead of having an API key for each user stored in the database, we may provide third-party developers who want to use our API with a OAuth service. This way, they would let users of our service log in through our OAuth server, and generate a token for them to use and query the API.

- [Twitter OAuth](https://developer.twitter.com/en/docs/basics/authentication/overview/oauth.html)
- [GitHub OAuth](https://developer.github.com/apps/building-oauth-apps/)

Before you jump to the server code, you may want to impersonate a third-party developer of an API using OAuth. You can do so with the GitHub one!

1. Go to [github.com/settings/applications/new](https://github.com/settings/applications/new) and register a new OAuth application
1. Download [this code](https://github.com/lepture/flask-oauthlib/blob/master/example/github.py) to a `./github.py` file in your project
1. Update the `consumer_key` and `consumer_secret` with the actual value you got from step 1.
1. Launch the server with: `pipenv run python github.py`

Now open the browser and navigate to `localhost:5000`. What is happenning?

1. You are redirected to a GitHub page where you, as a GitHub user, decide to grant (or not) this `github.py` service with an access (with a given **scopre**) to your GitHub information
1. Once accepted, you are redirected to your local service. The code stores _in session_ (that could be in DB!) the `github_token`.
1. With that token, the code is able to perform requests to the GitHub API **on the user's behalf**.

How can you update the `twitter-api` to use this GitHub OAuth gateway instead of an key-based auth?
