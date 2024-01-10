import pytest
from series.series import fibonacci, lucas, fibonacciIteration, sum_series

def test_fibonacci_one():
  actual = fibonacci(1)
  expected = 1
  assert actual == expected

def test_fibonacci_two():
  actual = fibonacci(4)
  expected = 3
  assert actual == expected

def test_fibonacci_three():
  actual = fibonacci(7)
  expected = 13
  assert actual == expected

def test_lucas_one():
  actual = lucas(1)
  expected= 1
  assert actual == expected

def test_lucas_two():
  actual = lucas(4)
  expected = 7
  assert actual == expected

def test_lucas_three():
  actual = lucas(5)
  expected = 11
  assert actual == expected

def test_sum_series_one():
  actual = sum_series(1)
  expected = 1
  assert actual == expected

def test_sum_series_two():
  actual = sum_series(4, 2, 1)
  expected_fibo = 3
  expected_lucas = 7
  assert actual == expected_fibo or expected_lucas

def test_sum_series_three():
  actual = sum_series(2, 7, 3)
  expected = 10
  assert actual == expected

###########################
  
def test_fibonacciIteration_one():
  actual = fibonacciIteration(1)
  expected = 1
  assert actual == expected

def test_fibonacciIteration_two():
  actual = fibonacciIteration(3)
  expected = 2
  assert actual == expected

def test_fibonacciIteration_three():
  actual = fibonacciIteration(7)
  expected = 13
  assert actual == expected



