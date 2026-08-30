import random

N = int(input("Enter how many points to generate: "))

n = 0

fixed_round = 0

while fixed_round != N:
    random_x = random.uniform (-1, 1)
    random_y = random.uniform (-1, 1)
    print (random_x)
    print (random_y)
    fixed_round = fixed_round + 1
    if ((random_x)*(random_x)) + ((random_y)*(random_y)) < 1:
        n = n + 1

pi = (4 * n) / N

print (f"Approximation of pi: {pi}")

# Note for myself: Had to add fixed round. Reason: I was adding a while N > 0, but then my pi calculation did not work because I was dividing by 0.
