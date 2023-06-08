
from pymtl3 import *

class MajorityFinder( Component ):
# Constructor

  def construct( s , nbits = 8):
   s.in_ = InPort (nbits)
   s.out = OutPort (nbits)
    
    
    
