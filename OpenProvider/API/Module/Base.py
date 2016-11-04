class Base(object):
    def __init__(self, parent=None):
        self.parent = parent

    def request(self, dict, **kwargs):
        return self.parent.performRequest(dict, **kwargs)
