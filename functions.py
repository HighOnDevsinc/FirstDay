from functools import partial

""" detect a prime number """


def is_prime(n):
    flag = False
    for x in range(2, n):
        if n % x == 0:
            flag = True
    return flag


if is_prime(11) is True:
    print("Not a prime number")
else:
    print("Prime number")


""" recursive call """


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(6))


""" partial functions """


def fun(a, b, c, x):
    return 1000*a + 100*b + 10*c + x


g = partial(fun, 3, 1, 4)
print(g(5))


""" lambda function """

# greet_user = lambda name, hel: print('Hey there,', name, 'in', hel)
# greet_user('Delilah', 'delemma')
