def methodception(another):
    return another()

def add_two_numbers():
    return 35 + 77
def add_three_numbers():
    return 1+2+3

print (methodception(add_two_numbers))
print (methodception(add_three_numbers))
