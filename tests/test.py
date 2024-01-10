import pytest
from series.series import fibonacci, lucas 

def test_fibonacci_one():
  actual = fibonacci(1)
  expected = 1
  assert actual == expected