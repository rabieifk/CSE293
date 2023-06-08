
from collections import deque
from copy import deepcopy

from pymtl3 import *

from SortUnitFL import sort_fl
from random     import randint, seed

class SortUnitCL( Component ):
  
  def construct( s, nbits=8, m=4, nstages=4 ):

    s.in_val = InPort ()
    s.in_    = [ InPort (nbits) for _ in range(m) ]

    s.out_val = OutPort()
    s.out     = [ OutPort(nbits) for _ in range(m) ]
    
    
    
