# News Client - Livecode

We built a REST API all day. Let's do the opposite: **consume** one.

We will use the [News API](https://newsapi.org/) with the following API Key: `367f28d82c3b42e2bb224b79b0ef480e`. This API has 2 endpoints we want to use:

- `https://newsapi.org/v2/top-headlines`
- `https://newsapi.org/v2/everything`

From the [HTTP section of `awesome-python`](https://github.com/vinta/awesome-python#http) we find the `requests` package to easily send HTTP requests. The [Quickstart](http://docs.python-requests.org/en/master/user/quickstart/) is very useful.

## Setup

```bash
mkdir news && cd $_
pipenv --python 3.7
pipenv install requests
pipenv install nose --dev

touch main.py
mkdir client
touch client/__init__.py

mkdir -p tests
touch tests/test_news.py

# We now can run:
pipenv run nosetests # => 0 tests for now
```

Here is the start code for the different files.

```python
# main.py
from client import News

def main():
    pass

if __name__ == '__main__':
    main()

```

```python
# client/__init__.py
import requests

class News:
    pass
```

```python
# tests/test_news.py
import unittest

from client import News

class NewsTest(unittest.TestCase):
    pass
```

## Let's code!

Who's volunteering? Here are the different steps to follow:

- Implement a `News` class to serve as REST client, with 2 methods: `headlines(country)` and `search(keyword`). use TDD for this step (NB: it will be integration testing)
- Open the `main.py` and use this new class to code an **interactive** cli like this one:

```bash
$ pipenv run python main.py
Country headlines [default] or Search [hit s]?
>
Country?
> us
# - Trump: 'I don't do anything ... just for political gain.' - POLITICO
# - SpaceX Falcon 9 rocket spied at Pad 39A as December launch quartet aligns - Teslarati
# - [...]

$ pipenv run python main.py
Country headlines [default] or Search [hit s]?
> s
What are you looking for?
> france
# - Trump Heads to France, Embracing a Post-Election Presidential Tradition
# - Europe Edition: Brexit, Ukraine, France: Your Monday Briefing
# - Are French riots a curse or a blessing for Macron?
# - [...]
```

## Solution

Please do not peek _before_ the livecode session!

<details><summary>View solution</summary><p>

```python
# tests/test_news.py
import unittest

from client import News

class NewsTest(unittest.TestCase):
    def test_french_headlines(self):
        news = News()
        articles = news.headlines("fr")
        self.assertEqual(type(articles), list)
        self.assertGreater(len(articles), 0)

    def test_search(self):
        news = News()
        articles = news.search("france")
        self.assertEqual(type(articles), list)
        self.assertGreater(len(articles), 0)
```

```python
# client/__init__.py
import requests

class News:
    API_KEY = "367f28d82c3b42e2bb224b79b0ef480e"
    BASE_URL = "https://newsapi.org/v2"

    def headlines(self, country = "us"):
        payload = { 'country': country, 'apiKey': self.API_KEY }
        response = requests.get(f"{self.BASE_URL}/top-headlines", params=payload)
        return response.json()['articles']

    def search(self, keyword):
        payload = { 'q': keyword, 'apiKey': self.API_KEY }
        response = requests.get(f"{self.BASE_URL}/everything", params=payload)
        return response.json()['articles']
```

```python
# main.py
from client import News

def main():
    news = News()

    choice = input("Country headlines [default] or Search [hit s]?\n> ")
    if choice == "s":
        keyword = input("What are you looking for?\n> ")
        for article in news.search(keyword):
            print(f"- {article['title']}")
    else:
        country = input("Country?\n> ")
        for article in news.headlines(country):
            print(f"- {article['title']}")

if __name__ == '__main__':
    main()
```

</p></details>
