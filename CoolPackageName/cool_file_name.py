"""
Module Docstring
"""

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"


def main():
    """ 
    Main entry point of the app 
    """
    x = input('First input: ')
    y = input('Second input: ')
    try:
        result = add_inputs(x,y)
        print(result)
    except TypeError:
        print('You have entered a string!')
        main()


def add_inputs(first,second):
    try: 
        first = int(first) 
        second = int(second)
        return int(first) + int(second)
    except ValueError:
        raise TypeError



if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
