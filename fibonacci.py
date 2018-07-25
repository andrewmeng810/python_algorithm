def fibonacci(n):
""" return a list of fibonacci sequence """
    fib_list = [0,1]
    if n == 0:
        return []
    elif n == 1:
        return [0]
    else:
        x = 2
        a, b = fib_list[0],fib_list[1]
        while x < n:
            a, b = b , a + b
            fib_list.append(b)
            x += 1
        return fib_list 
