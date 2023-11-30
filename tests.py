import os

import pytest

# Access the environment variable
foo = os.getenv('FOO', 'Default Value')

bar = os.getenv("BAZZ", None)

def test_foo_env_variable():
    # Your test here
    assert foo is not None  # Replace "Bar" with the expected value of FOO

 
def test_bar_env_variable():
    # Your test here
    assert bar is not None  # Replace "Bar" with the expected value of FOO

def test_sample():
    assert 2 == 2

