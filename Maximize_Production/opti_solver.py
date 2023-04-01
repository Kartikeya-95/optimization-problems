# -*- coding: utf-8 -*-
"""
@author: Kartikeya Sharma
"""

from variable_manager import VariableManager, Timer
from objective_manager import ObjectiveManager
from constraint_manager import ConstraintManager
import pyomo.environ as pyo
from pyomo.opt import SolverFactory
import pandas as pd


class Solver:
    """
    This class manages the solver and pyomo model
    """
    def __init__(self, solver='glpk'):
        """
        Initialize solver and pyomo model to define variables, constraints and objective(s)
        """
        print("Attempt to initialize solver.....")
        self.model = pyo.ConcreteModel()
        self.opt = SolverFactory(solver)
        print(f"{solver} is initialized successfully")
    
    @Timer.timeit
    def solveProblem(self):
        """
        Defines Variables, Constraints and Objectives by calling appropriate functions
        ---------------------------------------------------------------------------------
        Prints the summary of the model and export optimization results in an excel
        Returns: None
        """
        
        # Defining Variables
        x = VariableManager(self.model).defineVars()
        m = VariableManager(self.model).m
        t = VariableManager(self.model).t
        
        # Defining Constraints
        ConstraintManager(self.model).createConstraints(x, m, t)
        
        # Defining Objective
        obj = ObjectiveManager(self.model).createObjective(x, m, t)
        
        # Solving the optimization problem
        print("Solving the optimization problem.....")
        result = self.opt.solve(self.model)
        
        print()
        print("Below is the Summary of the problem")
        print(self.model.pprint())
        
        print("\n Exporting results to excel")
        sol_dict = {}
        for i in range(1, m+1):
            for j in range(1, t+1):
                sol_dict[i,j] = pyo.value(x[i,j])
                
        df = pd.DataFrame(
            data=sol_dict.values(),
            index=['x'+str(i) for i in list(sol_dict.keys())],
            columns=['Production_Quantity']
            )
        
        df.to_excel("Optimization_Results.xlsx")
        
if __name__ == '__main__':
    Solver().solveProblem()
        
        
        