# this is a module - I want to stop people to executing it directly
import sys

if __name__ == '__main__':
    sys.exit()

def myfunc():
    pass

print(__name__)
