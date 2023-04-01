# -*- coding: utf-8 -*-
"""
@author: Kartikeya Sharma
"""

import pyomo.environ as pyo
from variable_manager import Timer

class ObjectiveManager:
    """
    This class manages the Objective(s) of the optimization problem
    """
    def __init__(self, model):
        self.model = model
    
    @Timer.timeit
    def createObjective(self, x, m, t):
        """
        Creates Objective function
        """
        print("Creating Objective.....")
        x = x
        m = m
        t = t
        
        self.model.obj = pyo.Objective(
            expr = sum(
                    x[i,j] for i in range(1, m+1) for j in range(1, t+1)
                   ),
            sense = pyo.maximize
            )
        
        return self.model.obj
