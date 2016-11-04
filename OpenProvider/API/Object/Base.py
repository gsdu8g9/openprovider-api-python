import re

def convert_to_snake(string):
    """Convert camel to snake case"""
    # Add an underscore before a single uppercase character
    string = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', string)
    # Add an underscore before a group of numbers
    string = re.sub('(.)([0-9]+)', r'\1_\2', string)
    # Add an underscore before a uppercase character that has a lowercase
    # character before it
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', string).lower()

class Map(dict):
    def __init__(self, *args, **kwargs):
        super(Map, self).__init__(*args, **kwargs)
        for arg in args:
            if isinstance(arg, dict):
                for key, value in arg.items():
                    # Convert camel to snake case
                    key = convert_to_snake(key)
                    if isinstance(value, dict):
                        self[key] = Map(value)
                    else:
                        self[key] = value

        if kwargs:
            for key, value in kwargs.items():
                self[key] = value

    def __getattr__(self, attr):
        return self.get(attr)

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __setitem__(self, key, value):
        super(Map, self).__setitem__(key, value)
        self.__dict__.update({key: value})

    def __delattr__(self, item):
        self.__delitem__(item)

    def __delitem__(self, key):
        super(Map, self).__delitem__(key)
        del self.__dict__[key]

class Base(Map):
    pass
