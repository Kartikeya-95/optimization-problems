# -*- coding: utf-8 -*-
"""
@author: Kartikeya Sharma
"""

import pyomo.environ as pyo
from variable_manager import Timer

class ConstraintManager:
    """
    This class manages the constraints for the optimization problem
    """
    def __init__(self, model):
        self.model = model
        self.model.C1 = pyo.ConstraintList()
        self.model.C2 = pyo.ConstraintList()
        self.model.C3 = pyo.ConstraintList()
        self.model.C4 = pyo.ConstraintList()
    
    @Timer.timeit
    def createConstraints(self, x, m, t):
        """
        Creates Constraints for the optimization problem
        """
        
        print("Creating Constraints.....")
        x = x
        m = m
        t = t
        
        for i in range(1, t+1):
            self.model.C1.add(
                expr=2*x[2,i]-8*x[3,i] <= 0
                )
            
            self.model.C2.add(
                expr=sum(x[m,i] for m in range(1,5)) <= 50
                )
            
            if i > 2:
                self.model.C3.add(
                    expr=x[2,i]-2*x[3,i-2]+x[4,i] >= 1
                    )
                
            if i > 1:
                self.model.C4.add(
                    expr=x[1,i]+x[2,i-1]+x[3,i]+x[4,i] <= 10
                    )
        