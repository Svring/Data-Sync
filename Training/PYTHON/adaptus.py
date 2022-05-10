def check_mountain_number(n):
    """
    >>> check_mountain_number(103)
    False
    >>> check_mountain_number(153)
    True
    >>> check_mountain_number(123456)
    True
    >>> check_mountain_number(2345986)
    True
    """
    def helper(n, status):
        if not n // 10:
            return True
        if status and n % 10 < ((n // 10) % 10):
            return helper(n // 10, status)
        return (n % 10) > ((n // 10) % 10) and helper(n // 10, False)
    return helper(n, True)

if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)