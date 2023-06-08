
from pymtl3 import *
from pymtl3.passes.backends.verilog import *

class MinMaxUnit(Component):

    # Constructor
    def construct(s, nbits = 8):

        s.in0 = InPort(nbits)
        s.in1 = InPort(nbits)
        s.in2 = InPort(nbits)
        s.out_min = OutPort(nbits)
        s.out_max = OutPort(nbits)
        
        
        
        
