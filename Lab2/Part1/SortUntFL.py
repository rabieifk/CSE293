
from pymtl3 import *
class SortUnitFL( Component ):

  # Constructor

  def construct( s, nbits=8 , m=4):

    s.in_val = InPort ()
    s.in_    = [ InPort (nbits) for _ in range(m) ]

    s.out_val = OutPort()
    s.out     = [ OutPort(nbits) for _ in range(m) ]
    
    
    
