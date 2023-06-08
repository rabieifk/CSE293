
from pymtl3 import *
import numpy as np

class MatrixMultiplier(Component):
    def construct(s, n, m, p, nbits=8):
        s.n = n
        s.m = m
        s.p = p
        
        # Inputs
        s.mat_a = [[ InPort (nbits) for _ in range(m)] for _ in range(n)] # Matrix A 
        s.mat_b = [[ InPort (nbits) for _ in range(p)] for _ in range(m)] # Matrix B

        # Output
        s.mat_c = [[ OutPort (nbits) for _ in range(p)] for _ in range(n)] # Matrix C
        s.operation_ctr = OutPort ( nbits )
        
        
