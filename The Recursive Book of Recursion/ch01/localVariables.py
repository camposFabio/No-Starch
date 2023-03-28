def a():
    Spam = 'Ant'
    print('spam is ' + Spam)
    b()
    print('spam is ' + Spam)


def b():
    Spam = 'BobCat'
    print('spam is ' + Spam)
    c()
    print('spam is ' + Spam)


def c():
    Spam = 'Coyote'
    print('spam is ' + Spam)


a()
