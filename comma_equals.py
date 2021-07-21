def do_something():
  x = 1
  y = [2]

  x, = [2]
  primes = { 2, 3, 5, 7, 11 }
  evens = { 2, 4, 6, 8, 10 }

  x, = primes.intersection(evens)
  print(x)


if __name__ == '__main__':
    do_something()
