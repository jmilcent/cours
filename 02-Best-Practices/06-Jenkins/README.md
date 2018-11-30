# Jenkins

In the previous [Continuous Integration](../04-Continuous-Integration) exercise, we have covered how to use the cloud provider [Travis CI](https://travis-ci.com/) to quickly put in place a "build farm" for our GitHub repository. The tight integration between GitHub and Travis CI combined with the usage of GitHub's OAuth capabilities gets any developer up & running in minutes. The trickiest part of this setup is always getting the `.travis.yml` configuration right.

In this exercise, we will replace Travis CI with **Jenkins**.

## Context

[Jenkins](https://jenkins.io/) is an _open-source_ automation server written in java. It is a server-based system that runs in servlet containers such as Apache Tomcat. Released under the MIT License, Jenkins is free software.

Jenkins was first released in **2011** and is widely used by companies around the world. Corporations who don't want to trust the cloud provider Travis CI turn to Jenkins and host this software on their own servers. For this exercise, Le Wagon is providing an instance of Jenkins hosted on AWS EC2. Back at your company, you might be able to use the Jenkins instances provided by your IT teams if such instances exist.

## Starting from scratch

Let's create a new simple project to be configured in Continuous Integration with Jenkins.

```bash
cd ~/code/$YOUR_GITHUB_USERNAME
mkdir morse
cd morse

pipenv --python 3.7
pipenv install nose pylint --dev
```

Let's create the files for our project:

```bash
touch morse.py
mkdir tests
touch tests/test_morse.py
```

Let's write an empty class definition for our `morse.py` main package:

```python
# morse.py
# pylint: disable=missing-docstring

class Morse:
    def decode(self, message):
        pass # TODO: implement the behavior!
```

Our goal is to code a [Morse code](https://en.wikipedia.org/wiki/Morse_code) **decoder** which behaves like this:

```python
morse = Morse()
sentence = morse.decode(".- .-.. .-.. / -.-- --- ..- / -. . . -.. / .. ... / -.-. --- -.. .")
# => ALL YOU NEED IS CODE
```

We want to use Jenkins, so we need tests! let's write a few unit tests for the `decode()` method:

```python
# tests/test_game.py
import unittest
from morse import Morse

class TestMorse(unittest.TestCase):
    def test_empty_message(self):
        self.assertEqual(Morse().decode(""), "")

    def test_a(self):
        self.assertEqual(Morse().decode(".-"), "A")

    def test_b(self):
        self.assertEqual(Morse().decode("-..."), "B")

    def test_c(self):
        self.assertEqual(Morse().decode("-.-."), "C")

    def test_d(self):
        self.assertEqual(Morse().decode("-.."), "D")

    def test_e(self):
        self.assertEqual(Morse().decode("."), "E")

    def test_f(self):
        self.assertEqual(Morse().decode("..-."), "F")

    def test_g(self):
        self.assertEqual(Morse().decode("--."), "G")

    def test_h(self):
        self.assertEqual(Morse().decode("...."), "H")

    def test_i(self):
        self.assertEqual(Morse().decode(".."), "I")

    def test_j(self):
        self.assertEqual(Morse().decode(".---"), "J")

    def test_k(self):
        self.assertEqual(Morse().decode("-.-"), "K")

    def test_l(self):
        self.assertEqual(Morse().decode(".-.."), "L")

    def test_m(self):
        self.assertEqual(Morse().decode("--"), "M")

    def test_n(self):
        self.assertEqual(Morse().decode("-."), "N")

    def test_o(self):
        self.assertEqual(Morse().decode("---"), "O")

    def test_p(self):
        self.assertEqual(Morse().decode(".--."), "P")

    def test_q(self):
        self.assertEqual(Morse().decode("--.-"), "Q")

    def test_r(self):
        self.assertEqual(Morse().decode(".-."), "R")

    def test_s(self):
        self.assertEqual(Morse().decode("..."), "S")

    def test_t(self):
        self.assertEqual(Morse().decode("-"), "T")

    def test_u(self):
        self.assertEqual(Morse().decode("..-"), "U")

    def test_v(self):
        self.assertEqual(Morse().decode("...-"), "V")

    def test_w(self):
        self.assertEqual(Morse().decode(".--"), "W")

    def test_x(self):
        self.assertEqual(Morse().decode("-..-"), "X")

    def test_y(self):
        self.assertEqual(Morse().decode("-.--"), "Y")

    def test_z(self):
        self.assertEqual(Morse().decode("--.."), "Z")

    def test_sos(self):
        self.assertEqual(Morse().decode("... --- ..."), "SOS")

    # NOTE: we will add a test for *sentences* later
```

In your terminal, run the tests:

```bash
pipenv run nosetests
```

You should get 28 failing tests! Great, we have the "red" step of TDD. Let's proceed with the Jenkins configuration before making the tests green.

Before we can do that, we need our project to be pushed to GitHub:

```bash
git init
git add .
git commit -m "Morse code. Failing tests. Pending Jenkins configuration"
```

Go to [github.com/new](https://github.com/new) and create a `morse` repository. Push your code:

```bash
git remote add origin git@github.com:YOUR_GITHUB_USERNAME/morse.git
git push origin master
```

## Jenkins configuration

Go to [jenkins.lewagon.com](http://jenkins.lewagon.com) and sign in with your GitHub account. If all goes well you should arrive on the following log-in screen.

![](../../img/jenkins-after-login.png)

Click on "New item" to create a new configuration.

![](../../img/jenkins-create-project.png)

You should arrive on this screen:

![](../../img/jenkins-add-1.png)

Once "GitHub" has been selected as a source, it gets trickier. The idea is that we will provide a way for Jenkins to:

1. Download the source from GitHub. For a public repo it mights seems obvious as the code is open-source, so no auth needed right? Well, that's true but would defat the second item:
1. Set the status of every commit of every branch and Pull Request, allowing the developers to be aware of breakage directly from GitHub

![](../../img/jenkins-add-2.png)

Select the project to store the credentials (and not a global Jenkins configuration). You will be prompted with a pop-in asking you for a username and password. **Don't put your password** in here. Go to [github.com/settings/tokens](https://github.com/settings/tokens) to generate a new one.

You need the following permissions:

- `repo:status`
- `public_repo`
- `read:org`
- `user:email`

![](../../img/jenkins-add-3.png)

![](../../img/jenkins-add-4.png)

Save your credentials configuration, it will close the pop up. It's now time to select the right GitHub repository as a source.

![](../../img/jenkins-add-5.png)

Finally it should scan your repository for branches. In each branch, it will look for a `Jenkinsfile`, which it won't find.

![](../../img/jenkins-add-6.png)

### Jenkinsfile

Let's add a `Jenkinsfile` to our project to tell Jenkins how to build it. It's the strict equivalent to `.travis.yml` we had before.

```bash
touch Jenkinsfile
```

Open this file in Sublime Text and copy-paste the following configuration:

```groovy
pipeline {
    agent {
        docker {
            image 'python:3.7'
        }
    }
    environment {
        HOME = "${env.WORKSPACE}"
    }
    stages {
        stage('build') {
            steps {
                sh 'pip install pipenv --user'
                sh '~/.local/bin/pipenv install --dev'
            }
        }
        stage('test') {
            steps {
                sh '~/.local/bin/pipenv run nosetests'
            }
        }
    }
}
```

Compare this to the `.travis.yml` you had in a previous exercise. What is similar? What is different? Discuss with your buddy.

Before we commit and push, we need to link GitHub and Jenkins by configuring a webhook on the repository. Go to the following address:

```
https://github.com/YOUR_GITHUB_NICKNAME/morse/settings/hooks
```

And click on the top-right button "Add webhook".

You want to add a Webhook for the following events:

- Pull Requests
- Pushes

It should look like this:

![](../../img/github-add-webhook.png)

That's it! GitHub will report Jenkins everytime you push or open a Pull Request.

So let's push!

```bash
git add Jenkinsfile
git commit -m "Adding Jenkinsfile"
git push origin master
```

Go to Jenkins and watch a **#1** build start, finish and be **red**.

![](../../img/jenkins-first-build-red-1.png)

![](../../img/jenkins-first-build-red-2.png)

![](../../img/jenkins-first-build-red-3.png)

### Turning Jenkins's project green (blue)

Jenkins uses a blue circle :large_blue_circle: to visualize a passing build and a red circle :red_circle: for a failing one. Right now, our `master` branch is red on Jenkins. We must fix it!

Take some time to implement the `decode(self, message)` function in `morse.py`. To run the tests, you can locally launch:

```bash
pipenv run nosetests
```

Stuck? Ask your buddy! Still stuck? Ask a TA!

<details><summary>View solution</summary><p>

```python
class Morse:
    ALPHABET = {
        '.-':   'A',
        '-...': 'B',
        '-.-.': 'C',
        '-..':  'D',
        '.':    'E',
        '..-.': 'F',
        '--.':  'G',
        '....': 'H',
        '..':   'I',
        '.---': 'J',
        '-.-':  'K',
        '.-..': 'L',
        '--':   'M',
        '-.':   'N',
        '---':  'O',
        '.--.': 'P',
        '--.-': 'Q',
        '.-.':  'R',
        '...':  'S',
        '-':    'T',
        '..-':  'U',
        '...-': 'V',
        '.--':  'W',
        '-..-': 'X',
        '-.--': 'Y',
        '--..': 'Z'
    }

    def decode(self, message):
        if message == "":
            return ""

        symbols = message.split(" ")
        letters = [self.ALPHABET[s] for s in symbols]
        return ''.join(letters)
```

</p></details>

Once your test are passing locally, it's time to commit & push:

```bash
git add morse.py
git commit -m "100% passing tests for one-word Morse decoder"
git push origin master
```

Go back to Jenkins, and watch your build run.

![](../../img/jenkins-second-build-green.png)

Hooray! Travis is now passing.

### Using Jenkins in a Pull Request

The implementation of our `decode()` method only supports one-word sentences. We are not yet parsing the ` / ` word separator. Let's do it in a **branch**!


```bash
git checkout -b multi-word-decode
```

Open the `tests/test_morse.py` file and add the following test at the bottom:

```bash
    def test_whole_sentence(self):
        message = Morse().decode(".- .-.. .-.. / -.-- --- ..- / -. . . -.. / .. ... / -.-. --- -.. .")
        self.assertEqual(message, "ALL YOU NEED IS CODE")
```

Go back to the terminal and run the tests:

```bash
pipenv run nosetests
```

You should have 29 tests running and one in failure:

```bash
.........................E...
======================================================================
ERROR: test_whole_sentence (test_morse.TestMorse)
----------------------------------------------------------------------
Traceback (most recent call last):
[...]
----------------------------------------------------------------------
Ran 29 tests in 0.013s

FAILED (errors=1)
```

Before we try to actually turn this test green by implementing the feature in the `morse.py` file, let's commit and push this branch:

```bash
git add tests/test_morse.py
git commit -m "Adding a multi-word test. Red for now"
git push origin multi-word-decode
```

Go back to Jenkins, up in your project (don't stay in the `master` branch). The URL should look something like this:

```
http://jenkins.lewagon.com/jenkins/me/my-views/view/all/job/YOUR_GITHUB_NICKNAME-morse/
```

You now have 2 branches! And you can see that the `multi-word-decode` branch is actually red.

**Your turn**! Try to make this branch green by implementing the feature. If you are stuck, talk to your buddy. Ask a TA for help.

<details><summary>View solution</summary><p>

```python
    def decode(self, message):
        if message == "":
            return ""

        words = message.split(" / ")
        decoded_words = [self.decode_word(word) for word in words]
        return ' '.join(decoded_words)

    def decode_word(self, word):
        symbols = word.split(" ")
        letters = [self.ALPHABET[s] for s in symbols]
        return ''.join(letters)
```

</p></details>

Commit your work and push your branch. Go on GitHub and click on the "New pull request" button. You want to merge the `multi-word-decode` (`HEAD`) into `master` (base branch). Create the Pull Request and enjoy the integration between Jenkins and GitHub, thanks to the webhook **and** you personal access token.

Go ahead and merge the branch. Go back to Jenkins, you should see `master` build one more time (as merging a branch on GitHub actually creates on more commit, a merge commit). You can visualize it here:

```
https://github.com/YOUR_GITHUB_NICKNAME/morse/network
```

![](../../img/github-morse-network.png)

## Conclusion

Like for Travis CI, adding tests to a repository and coupling GitHub with Jenkins gives the developer peace of mind when adding code, checking for possible regressions, exercising the whole test suite for _every single_ commit!

Bear in mind that depending on your project, the `Jenkinsfile` will vary. For this exercise, we are using a **Docker agent** run by Jenkins, with `pipenv` to install dependencies from the `Pipfile` and `nose` as a test launcher. Other projects might use a Python distribution like [Anaconda](https://www.anaconda.com/) and [`tox`](https://tox.readthedocs.io/en/latest/) as virtualenv manager / test launcher. Talk with your team!
