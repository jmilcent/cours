# Best Practises - Livecode

Let's practise **TDD** with a Vending Machine problem.

The machine accepts **4 coins**:

- **NICKEL** (5 cents)
- **DIME** (10 cents)
- **QUARTER** (25 cents)
- **DOLLAR** (100 cents)

The machine sells these items:

- **A** - Chocolate biscuits - 1$
- **B** - A can of coca - 1.20$
- **C** - A bottle of water - 0.85$

The vending machine should allow:

- A service man to refill the items
- A user can introduce coins and press one of the keys to get an item, and get some change back.

## Setup

```bash
mkdir vending-machine && cd $_
pipenv --python 3.7
pipenv install nose
mkdir tests
touch machine.py
touch tests/test_machine.py

# We now can run:
pipenv run nosetests # => 0 tests for now
```

Bootstrap the testing class:

```python
# tests/test_machine.py
import unittest

class MachineTest(unittest.TestCase):
    pass
```

## Solution

Please do not peek _before_ the livecode session!

<details><summary>View solution</summary><p>

```python
# test/test_machine.py
import unittest
from machine import Machine, Rack, Coin

class MachineTest(unittest.TestCase):
    def test_can_refill_biscuits(self):
        racks = [ Rack("A", "", 100) ]
        machine = Machine(racks)
        machine.refill("A", 3)
        self.assertEqual(machine.racks["A"].quantity, 3)

    def test_user_can_buy_item_a(self):
        racks = [ Rack("A", "", 100) ]
        machine = Machine(racks, 0)
        machine.refill("A", 1)
        machine.insert(Coin.DOLLAR)
        outcome = machine.press("A")
        self.assertTrue(outcome)
        self.assertEqual(machine.racks["A"].quantity, 0)
        self.assertEqual(machine.amount, 0)
        self.assertEqual(machine.coins[Coin.DOLLAR], 1)

    def test_user_get_its_change_back(self):
        racks = [ Rack("C", "", 85) ]
        machine = Machine(racks, 10) # Ten coins each
        machine.refill("C", 1)
        machine.insert(Coin.DOLLAR)
        outcome = machine.press("C")
        self.assertEqual(machine.coins[Coin.DIME], 9)
        self.assertEqual(machine.coins[Coin.NICKEL], 9)
```

```python
# machine.py
from enum import Enum

class Rack:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price
        self.quantity = 0

class Coin(Enum):
    NICKEL = 5
    DIME = 10
    QUARTER = 25
    DOLLAR = 100

class Machine:
    def __init__(self, racks, coin_count = 10):
        self.racks = dict((r.code, r) for r in racks)
        self.coins = dict((coin, coin_count) for coin in Coin)
        self.amount = 0

    def refill(self, code, quantity):
        self.racks[code].quantity += quantity

    def insert(self, coin):
        self.coins[coin] += 1
        self.amount += coin.value

    def press(self, code):
        rack = self.racks[code]
        if rack.quantity > 0:
            if self.amount >= rack.price:
                self.racks[code].quantity -= 1
                self.__give_change(self.amount - rack.price)
                self.amount -= rack.price
                return True
            else:
                # TODO: give feedback to user that more coins are needed!
                return False
        else:
            # TODO: give feedback to user that this product is sold out!
            return False

    def __give_change(self, change):
        if change == 0:
            return
        else:
            for coin in reversed(Coin):
                count = change // coin.value
                change = change % coin.value
                self.coins[coin] -= count
```

</p></details>
