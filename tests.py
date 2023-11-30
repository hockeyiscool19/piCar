import os

import pytest

# Access the environment variable
foo = os.getenv('FOO', 'Default Value')

bar = os.getenv("BAZZ", None)

if bar:
    print("Got secret")
else:
    print("Oh no")
def test_foo_env_variable():
    # Your test here
    assert foo == "Bar"  # Replace "Bar" with the expected value of FOO

def test_sample():
    assert 2 == 2

