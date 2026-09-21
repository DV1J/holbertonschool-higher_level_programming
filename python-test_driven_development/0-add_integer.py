"""
A function adds 2 values
returns the added value in type integer

"""
def add_integer(a, b=98):
        """
        checking if a and b are of int and float type if not raise TypeError with custom message
        """
        if type(a) != int and type(a) != float:
                raise TypeError('a must be an integer')
        if type(b) != int and type(b) != float:
                raise TypeError('b must be an integer')
        add = a + b
        return (int(add))