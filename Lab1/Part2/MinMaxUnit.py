
from pymtl3 import *

class MinMaxUnit( Component ):

  # Constructor

  def construct( s, nbits ):

    s.in0     = InPort ( nbits )
    s.in1     = InPort ( nbits )
    s.out_min = OutPort( nbits )
    s.out_max = OutPort( nbits )

    @update
    def block():

      if s.in0 >= s.in1:
        s.out_max @= s.in0
        s.out_min @= s.in1
      else:
        s.out_max @= s.in1
        s.out_min @= s.in0

  # Line tracing

  def line_trace( s ):
    return f"{s.in0}|{s.in1}(){s.out_min}|{s.out_max}"
    
    
if __name__ == "__main__":
  dut = MinMaxUnit(2)
  dut.apply(DefaultPassGroup(textwave=True))
  dut.sim_reset()

  dut.in0 @= 2
  dut.in1 @= 0
  dut.sim_tick()

  dut.print_textwave()
