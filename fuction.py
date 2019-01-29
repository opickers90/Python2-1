def add(x, y):
  return x + y

def do_twice(func, x, y):
  return func(func(x, y), func(x, y))

def do_third(func, x, y):
  return func(func(x, y), func(x, y))

a = 5
b = 10

print(do_third(do_twice(add,a, b), a, b))
