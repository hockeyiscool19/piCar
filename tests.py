impot os
import pytest

# Access the environment variable
foo = os.getenv('FOO', 'Default Value')

def test_foo_env_variable():
    # Your test here
    assert foo == "Bar"  # Replace "Bar" with the expected value of FOO

def test_sample():
    assert 2 == 2
r
