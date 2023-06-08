

from pymtl3 import *
from ram_1r1w_sync import RAM_1W1R_sync

class fifo_1r1w(Component):

    def construct(s, width_p=10, depth_p=20):
        s.width_p = width_p
        s.depth_p = depth_p

        s.data_i = InPort(width_p)
        s.valid_i = InPort(Bits1)
        s.yumi_i = InPort(Bits1)

        s.ready_o = OutPort(Bits1)
        s.data_o = OutPort(width_p)
        s.valid_o = OutPort(Bits1)
        
        
        
