def divide(a,b):
    try:
        return (a/b)
    except ZeroDivisionError:
        return ('you are dividing by zero')

print(divide(1,0))