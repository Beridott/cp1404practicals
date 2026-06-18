import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1? A: A random integer between 5 and 20.
# What was the smallest number you could have seen, what was the largest? A: 5, 20

# What did you see on line 2? A: A random odd integer from the choices 3, 5, 7, or 9.
# What was the smallest number you could have seen, what was the largest? A: 3, 9
# Could line 2 have produced a 4? A: No, because the step is 2 starting from 3, which only produces odd numbers.

# What did you see on line 3? A: A random floating-point number between 2.5 and 5.5.
# What was the smallest number you could have seen, what was the largest? A: 2.5, 5.5.

print(random.randint(1, 100))
