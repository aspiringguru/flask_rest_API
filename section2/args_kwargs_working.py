def addition_simplified(*args):
    print (type(args))
    return sum(args)

print ("sum:", addition_simplified(1,2,3,3,4,5,6))

def what_are_kwargs(*args, **kwargs):
    print ("args:", args)
    print ("kwargs", kwargs)


what_are_kwargs(12, 13, 14)
what_are_kwargs(12, 13, 14, name='fred', school="oxford")
what_are_kwargs(12, 13, 14, {'fred', 'oxford'})