from copy import deepcopy


class Prototype:

    def __init__(self):
        self._name = None
        self._reference = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, value):
        self._reference = value
        
