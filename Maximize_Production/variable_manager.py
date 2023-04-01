# -*- coding: utf-8 -*-
"""
@author: Kartikeya Sharma
"""

import pyomo.environ as pyo
from time import time

class Timer:
    def timeit(func):
        """
        Shows the execution time of a function in seconds
        """
        def wrapper(*args, **kwargs):
            t1 = time()
            result = func(*args, **kwargs)
            t2 = time()
            print(f"Function: {func.__name__} executed in {(t2-t1):.2f} sec")
            return result
        return wrapper

class VariableManager:
    """
    This class manages the constraints for the optimization problem
    """
    def __init__(self, model, m=4, t=10):
        self.model = model
        self.m = m
        self.t = t
    
    @Timer.timeit
    def defineVars(self):
        """
        Defines variables with indices for the problem
        ----------------------------------------------------------------
        Returns instance of declared variables of type <class 'pyomo.core.base.var.IndexedVar'>
        """
        
        print("Defining Variables.....")
        m, t = self.m, self.t
        self.model.x = pyo.Var(range(1, m+1), range(1, t+1), within=pyo.Integers, bounds=(0,10))
        return self.model.x
    
    def fetchVars():
        pass
