# Classes

Python belongs to the family of object-oriented languages. In OOP, the basic building block is a **Class**. Classes provide a means of bundling data and functionality (or behavior) together. Creating a new class creates a new **type** of object, allowing new **instances** of that type to be made. Each class instance can have **attributes** attached to it for maintaining its **state**. Class instances can also have **methods** (defined by its class) for modifying its state.

Take some time to read [9.3 - A first look at classes](https://docs.python.org/3/tutorial/classes.html#a-first-look-at-classes) until the `9.4`.

## Getting Started

```bash
cd ~/code/<your_username>/reboot-python
cd 01-OOP/08-Classes
subl .
```

## Your first class

Open the `vehicle.py` file and implement a simple class following these specs:

- A vehicle has a brand and a color
- A vehicle is started or stopped
- A vehicle can be started or stopped _via_ a call

To help you through this task, we implemented some tests you can run:

```bash
pipenv run nosetests
```

Do not hesitate to open and **read** the test file in `tests/test_vehicle.py`!
It will help you figure out how the `Vehicle` class is called, which is the
spec of what you should do translated to code.

💡 If you want to use the debugger introduced earlier with `nosetests`, you need to run the tests with the [`--no-capture` flag](http://nose.readthedocs.io/en/latest/man.html#cmdoption-s) (shortcut: `-s`).

