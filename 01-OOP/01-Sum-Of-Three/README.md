# Sum of Three

Let's start with a very simple exercise to understand how these exercises are going to work.

## Getting started

```bash
cd ~/code/lewagon/reboot-python
git pull origin master # Retrieve the latest version of the exercise

cd 01-OOP/01-Sum-Of-Three
subl . # Open the folder in Sublime Text
```

## Procedure

Your goal is to implement the method `sum3` in the `sum_of_three.py` file. Before you actually try to do it, run the **tests** that we prepared:

```bash
pipenv run nosetests # or `pr nosetests`
```

You should get three failing tests. Read the error (especially the `AssertionError`) to understand what is wrong and try implementing the `sum3` method. When you are done, run the command above once again.

Repeat until all tests turn pass (i.e. `0 FAILED`)

Then check your style with:

```bash
pipenv run pylint sum_of_three.py
```

If you get style errors, fix them, save and re-run the command above.

## Conclusion

The goal of this exercise was to show you how to run the tests to automatically evaluate your code (both style & content) and introduce you to this tight feedback loop.

Once you are done, please go to the [`02-System-Parameters`](../02-System-Parameters) exercise :pray:
