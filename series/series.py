def fibonacci(n):
  """
  Find the nth value in the fibonacci sequence.

  Parameters:
  - takes `n` an integer which is the position in the fibonacci sequence

  returns:
  - Returns the value at the nth position
  """
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)
  
def lucas(n):
  """
  Find the nth value in the Lucas sequence.

  Parameters:
  - takes `n`, an integer which is the position in the Lucas sequence

  returns:
  - Returns the value at the nth position
  """
  if n == 0:
    return 2
  elif n == 1:
    return 1
  else:
    return lucas(n - 1) + lucas(n - 2)
  


def sum_series(n, first_num=0, second_num=1):
  """
  Find the nth value in a custom series.

  Parameters:
  - takes `n`, an integer which will be the position in the custom sequence
  - First num in the custom series, defaults to 0
  - Second num in the custom series, defaults to 1

  Returns:
  - Returns the value at the nth position
  """
  if n == 0:
    return first_num
  elif n == 1:
    return second_num

  return sum_series(n - 1 , first_num, second_num) + sum_series(n - 2, first_num, second_num)


#######################################

def fibonacciIteration(n):
  fibo = [0, 1]
  for i in range(0, 20, 1):
    fibo.append(fibo[i] + fibo[i +1])

  return fibo[n]
