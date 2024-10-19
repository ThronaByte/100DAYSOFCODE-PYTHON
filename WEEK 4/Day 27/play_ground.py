
def add(*args):
    y = 0
    for n in args:
        y+=n
    print(y)
add(5,6,7)

def calc(**kw):
    print(kw)
calc(k=3,m=5,j='me')