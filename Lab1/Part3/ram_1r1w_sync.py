

from pymtl3 import *

class RAM_1W1R_sync(Component):

    def construct(s, width_p=8, depth_p=128, filename_p="memory_init_file.hex"):
        s.filename_p = filename_p
        
        s.wr_valid_i = InPort(Bits1)
        s.wr_data_i = InPort( width_p)
        s.wr_addr_i = InPort( math.ceil(math.log(depth_p, 2)))
        s.rd_addr_i = InPort( math.ceil(math.log(depth_p, 2)))
        s.rd_data_o = OutPort( width_p)
        
        
        
