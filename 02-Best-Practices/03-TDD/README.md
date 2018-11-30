# Test Driven Development

Test-driven development (aka **TDD**) is a software development process that relies on the repetition of a very short development cycle: red-green-refactor. The idea of this process is to turn a requirement into one or a couple of specific test cases, run those tests to make sure they are red, then implementing the code to turn those tests green. A third step is to refactor the code while keeping the tests green.

![](../../img/tdd.png)

The testing pattern encouraged is a four-phase one and well described in this [blog article by Thoughtbot](https://robots.thoughtbot.com/four-phase-test)

## Longest Word

Let's practise TDD with a simple game that we will use until the end of the day. We will implement "The Longest Word", a game where given a list of nine letters, you have to find the longest possible English word formed by those letters.

Example:

```
Grid: OQUWRBAZE
Longest word: BAROQUE
```

The word [`baroque`](https://en.wiktionary.org/wiki/baroque) is valid as it exists in the English dictionary (even though its origin is French 🇫🇷 😋)

Note that the word [`bower`](https://en.wiktionary.org/wiki/bower) is also valid. The goal here is **not** to write code which finds the longest word, but to analyze a human player attempt and judge if this word is valid or not against the given grid!

### A first approach

We need to **break down** the problem in tiny pieces. We also need to find the right level of **modelling** against the Object-Oriented paradigm.

In the TDD paradigm, one question we always ask is:

> How can I test this?

Asking this question means you need to think about your code like a black box. It will take some parameters in entry and you will observe the output, comparing them to an expected result.

❓ Take a few minutes to think about the **two main functions** of our game.

<details><summary>View solution</summary><p>

We need a first function to compute a grid of nine random letters:

```python
def random_grid():
    pass
```

We need another function which, given a nine letter grid, tells if a word is valid:

```python
def is_valid(word, grid):
    pass
```

</p></details>

<br>

❓ How can we use the Object-Oriented paradigm on this problem? Again, take some time to think about it.

<details><summary>View solution</summary><p>

We can create a `Game` class which will have the following blueprint:

1. Generate and hold a 9-letter random list
1. Test the validity of a word against this grid

</p></details>

<br>

### Starting the project with TDD

Now that we have a better idea of the object we want to build, we can start writing a test. First of all, let's create a new Python project:

```bash
cd ~/code/$YOUR_GITHUB_USERNAME
mkdir longest-word && cd $_
pipenv --python 3.7
pipenv install nose pylint --dev
pipenv install --pre --dev astroid # Fix for https://github.com/PyCQA/pylint/issues/2241

touch game.py
mkdir tests
touch tests/test_game.py

subl .
```

Let's set up our test class, inheriting from [`unittest.TestCase`](https://docs.python.org/3.7/library/unittest.html#basic-example)

```python
# tests/test_game.py
import unittest
import string
from game import Game

class TestGame(unittest.TestCase):
    def test_game_initialization(self):
        new_game = Game()
        grid = new_game.grid
        self.assertIsInstance(grid, list)
        self.assertEqual(len(grid), 9)
        for letter in grid:
            self.assertIn(letter, string.ascii_uppercase)

```

Read this code. If you have _any_ question about it, ask a teacher. You can copy/paste this code to `tests/test_game.py`.

Now it's time to run it first to make sure those tests are **failing**:

```bash
pipenv run nosetests
```

What next? Now you should **read the error message**, and try to **fix** it, and only this one (don't anticipate). Let's do the first one together:

```bash
E
======================================================================
ERROR: Failure: ImportError (cannot import name 'Game' from 'game' (/Users/seb/code/ssaunier/longest-word/game.py))
----------------------------------------------------------------------
Traceback (most recent call last):
  # [...]
  File ".../longest-word/tests/test_game.py", line 2, in <module>
    from game import Game
ImportError: cannot import name 'Game' from 'game' (.../longest-word/game.py)

----------------------------------------------------------------------
Ran 1 test in 0.004s

FAILED (errors=1)
```

OK so the error message is `ImportError: cannot import name 'Game' from 'game'`. It can't find a `Game` type.

❓ How can we fix it?

<details><summary>View solution</summary><p>

We need to create a `Game` class in the `./game.py` file:

```python
# game.py
class Game:
    pass
```

</p></details>

<br>

Let's run the tests again:

```bash
pipenv run nosetests
```

We get this error message:

```
E
======================================================================
ERROR: test_game_initialization (test_game.TestGame)
----------------------------------------------------------------------
Traceback (most recent call last):
  File ".../longest-word/tests/test_game.py", line 7, in test_game_initialization
    grid = new_game.grid
AttributeError: 'Game' object has no attribute 'grid'

----------------------------------------------------------------------
Ran 1 test in 0.004s

FAILED (errors=1)
```

🎉 PROGRESS!!! We have a **new** error message: `AttributeError: 'Game' object has no attribute 'grid'`.

![](../../img/new-error.jpg)

### Your turn!

Did you get this quick feedback loop? We run the test, we get an error message, we figure out how to fix only this, we run the test again and we move to a new error message!

❓ Try to implement the `Game` code to make this test pass. Don't look at the solution just yet, try to apply TDD on this problem!

💡 You can use `print()` or `import pdb; pdb.set_trace()` in combination with `nosetests -s`.

<details><summary>View solution</summary><p>

One possible implementation is:

```python
# game.py
import string
import random

class Game:
    def __init__(self):
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))
```

</p></details>

<br>

## Checking the validity of a word

Let's move to the second method of our `Game` class.

We use **TDD**, which means that we need to write the test **first**. For the first test, we gave away the code.

❓ It's your turn to implement a test for this new `is_valid(self, word)` method! See, we already gave you the method [signature](https://en.wikipedia.org/wiki/Type_signature#Method_signature)...

<details><summary>View solution</summary><p>

A possible implementation of the test would be:

```python
# tests/test_game.py

# [...]

    def test_empty_word_is_invalid(self):
        new_game = Game()
        self.assertIs(new_game.is_valid(''), False)

    def test_is_valid(self):
        new_game = Game()
        new_game.grid = list('KWEUEAKRZ') # Force the grid to a test case:
        self.assertIs(new_game.is_valid('EUREKA'), True)
        self.assertEqual(new_game.grid, list('KWEUEAKRZ')) # Make sure the grid remained untouched

    def test_is_invalid(self):
        new_game = Game()
        new_game.grid = list('KWEUEAKRZ') # Force the grid to a test case:
        self.assertIs(new_game.is_valid('SANDWICH'), False)
        self.assertEqual(new_game.grid, list('KWEUEAKRZ')) # Make sure the grid remained untouched
```

</p></details>

<br>

Run the tests to make sure they are not passing:

```bash
pipenv run nosetests
```

❓ It's your turn! Update the `game.py` implementation to make the tests pass!

<details><summary>View solution</summary><p>

A possible implemantation is:

```python
# game.py

# [...]

    def is_valid(self, word):
        if not word:
            return False
        letters = self.grid.copy() # Consume letters from the grid
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        return True
```

</p></details>

<br>


## Style

Make sure to make `pylint` happy:

```bash
pipenv run pylint game.py
```

You can disable those rules:

```python
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
```
