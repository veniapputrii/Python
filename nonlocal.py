#used in functions inside functions to create anonymous functions

#for example :
def out():
    x = "Welcome"
    def inner():
        nonlocal x
        x = "to Flexible"
    inner()
    return x
print(out())