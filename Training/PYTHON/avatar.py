def improve(update, close, guess = 1):
    ''' 
    iterate the answer with the method

    update:the method used to iterate value
    close:the tolerance target
    '''
    while not close(guess):
        guess = update(guess)
    return guess

def approx_eq(x, y, tolerance = 1e-10):
    ''' judge if the tolerance meet the target '''
    return abs(x - y) < tolerance

def newton_update(f, df):
    ''' 
    iterate the function get in

    return the next point
    '''
    def update(x):
        return x - f(x) / df(x)
    return update

def find_zero(f, df):
    ''' core function '''
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero)

def power(x, n):
    ''' return the n'th power of x '''
    product, k = 1, 0
    while k < n:
        product, k = product * x, k + 1
    return product

def nth_root_of_a(n, a):
    def f(x):
        return power(x, n) - a
    def df(x):
        return n * power(x, n - 1)
    return find_zero(f, df)