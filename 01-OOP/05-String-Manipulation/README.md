## String Manipulation

The `String` class is one of the most used class of Python and programming languages in general. A lot of build-in methods already exist to make your life easier and your goal in these exercises will be to:

- Learn to look for the right method in the Python doc
- Get familiar with using the Python interpreter to experiment with new methods and make them yours

The Python interpreter works like this:

```bash
pipenv run python
```

1. It reads the expression written by the user, which can be any valid ruby expression like `"Hello"`, `2+2`, `"hello".upper()` ...
2. It evaluates the result of this expression.
3. It prints this result.
4. It loops back to point 1, waiting for a new user input.

Start it by typing the command "python" in your terminal.

* **Experiment the following lines** on the Python interpreter:

```python
1 + 1
"A string object".lower()
"A string object".upper()
type(4)
```

## Getting started


```bash
cd ~/code/<your_username>/reboot-python
cd 01-OOP/05-String-Manipulation
subl .
pipenv run nosetests
pipenv run pylint string_methods.py
```

In Python, everything (a string, an integer, a floating number, a list...) is an object. We can call methods on these objects. Such methods are called **instance methods** since they can only be called on instances of the class. The object on which we call the method is called the **receiver**.

## Exercise

Find the right Python methods of the [String class](https://docs.python.org/3/library/stdtypes.html#string-methods) to plug in and make the tests pass.

Code is all about being smart and knowing how and where to look for the info you need! Often, the most difficult step is to ask google the right question. To find the methods you'll need for this challenge, use:

* Google and [Stack Overflow](http://stackoverflow.com/)
* [The python doc](https://docs.python.org/3) if you have a rough idea of the method you are looking for.

When you think you've found the method you're looking for, and you think you know how to use it, use the Python interpreter to test this method on something! Experimenting on the Python interpreter is a crucial step for beginners.
