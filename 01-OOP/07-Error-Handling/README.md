# Error Handling

Errors and Exceptions are part of every programming language. At runtime, our code may not behave like we expect. Suppose you have a dictionary and try to access a key which _does not exist_. That's an error, and Python actually provide types for those (here it would be a `KeyError`). Fortunately, there is a way to deal with these errors in the code.

Start by reading Chapter 8 of the Python Tutorial about [Errors and Exceptions](https://docs.python.org/3.7/tutorial/errors.html).

## Syntax

Every language will come up with specific language **keywords** to deal with errors.

Here are the important ones you should know in Python:

- `try / except` for the control flow to handle errors from called code
- `raise` when your code raises an Error
- `finally` to **always** execute some code after a `try`
- `with` is specific to Python and helps with properly closing IO streams ([cf 8.7](https://docs.python.org/3.7/tutorial/errors.html#predefined-clean-up-actions))

## Exercise

Let's experiment in the Python [REPL](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop) with the built-in function [`int()`](https://docs.python.org/3/library/functions.html#int). This function is really handy as it takes a String and converts it to an Integer. It's useful when reading information from a file or a network stream where everything is just characters.

```bash
python

>>> int("1")
1

>>> int("not_a_number")
# => What happens?
```

You just triggered a `ValueError`. Let's code a `try / except` block.

Open the `square.py` file and read the code:

```python
import sys

if __name__ == "__main__":
    print(type(sys.argv[1]))
```

Before running the code, try to guess the behavior of this little program. Ready?

```bash
pipenv run python square.py
```

What is happenning? How can we mitigate this behavior? There are two valid answers to this question, can you code both versions?

Now that we have handled the case where the user does not provide an argument, let's provide some:

```bash
pipenv run python square.py 42
pipenv run python square.py wagon
```

It's now time to use `int()` to convert those string arguments and use them. When run, your program should display the number square. If the argument is not a number, it should display "Not a number". To test your code, just run the commands above 👆, there is no unit test associated with this exercise. Call a teacher if you need some help.
