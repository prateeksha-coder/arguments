def countdown(n):
    """this is a function to show recursive countdown """
    if n == 0:          # stopping condition
        print("Done!")
    else:
        print(n)
        countdown(n - 1)   # function calls itself

countdown(5)
print(countdown.__doc__)