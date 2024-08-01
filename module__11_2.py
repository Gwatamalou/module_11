################################
# Какое задание такое и решение
# Всё в кашу смешали да так что ниче не понятно
##############################################

import inspect
from pprint import pprint
class Plane():
    def __init__(self):
        self.name = 'a320'

    def func1(self):
        pass

    def func2(self):
        pass

def  introspection_info(obj):
    res = {
        'type':type(obj),
        'attributes': dir(obj),
        'methods': [method for method in dir(obj) if not method.startswith('__')],
        'module': obj.__class__.__module__
    }
    return res

plane = Plane()
number_info = introspection_info(plane)
pprint(number_info)

