# System Parameters

Python scripts can read arguments passed on the command line. This may come in handy when you want to add options to your script.

## Getting started

```bash
cd ~/code/<your_username>/reboot-python
cd 01-OOP/02-System-Parameters
subl .
pipenv run nosetests
pipenv run pylint calc.py
```

## Some words about `sys.argv`

Consider the following code:

```python
# args.py
import sys

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))
```

You can save it to a file `args.py` and run it:

```bash
pipenv run python args.py arg1 arg2 arg3
# Number of arguments: 4 arguments.
# Argument List: ['args.py', 'arg1', 'arg2', 'arg3']
```

[`sys.argv`](https://docs.python.org/3/library/sys.html#sys.argv) is a python **list** containing the command line arguments passed to a Python script. `argv[0]` is always the script name.

## Exercise

Let's write a simple calculator for **integers**. Here's how it should work:

```bash
alias prp="pipenv run python"
prp calc.py 4 + 5
# => 9
prp calc.py 2 \* 6
# => 12
prp calc.py 3 - 9
# => -6
```

Open the `calc.py` file and implement this behavior! You will find that a `main` function that is automatically executed thanks to [this idiom](https://docs.python.org/3/library/__main__.html).


## Going Further

If you have to build a serious CLI tool with Python, please consider the built-in [`argparse`](https://docs.python.org/3/library/argparse.html).
