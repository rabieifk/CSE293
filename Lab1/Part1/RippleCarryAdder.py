
#=========================================================================
# RippleCarryAdder
#=========================================================================

from pymtl3 import *


class FullAdderFR(Component):

  def construct(s):
    s.a = InPort()
    s.b = InPort()
    s.cin = InPort()
    s.sum = OutPort()
    s.cout = OutPort()

    @update
    def upblk():
      s.sum @= s.cin ^ s.a ^ s.b
      s.cout @= ((s.a ^ s.b) & s.cin) | (s.a & s.b)


class RippleCarryAdder(Component):

  def construct(s):
    s.in0 = InPort(4)
    s.in1 = InPort(4)
    s.out = OutPort(5)

    s.w_CARRY = Wire(5)

    s.w_SUM = Wire(4)

    s.w_CARRY[0] //= 0

    s.fas = FullAdderFR()
    s.in0[0] //= s.fas.a
    s.in1[0] //= s.fas.b
    s.fas.cin //= s.w_CARRY[0]
    s.w_SUM[0] //= s.fas.sum
    s.w_CARRY[1] //= s.fas.cout

    s.fas2 = FullAdderFR()

    s.in0[1] //= s.fas2.a
    s.in1[1] //= s.fas2.b
    s.w_CARRY[1] //= s.fas2.cin
    s.w_SUM[1] //= s.fas2.sum
    s.w_CARRY[2] //= s.fas2.cout

    s.fas4 = FullAdderFR()

    s.in0[2] //= s.fas4.a
    s.in1[2] //= s.fas4.b
    s.w_CARRY[2] //= s.fas4.cin
    s.w_SUM[2] //= s.fas4.sum
    s.w_CARRY[3] //= s.fas4.cout

    s.fas6 = FullAdderFR()

    s.in0[3] //= s.fas6.a
    s.in1[3] //= s.fas6.b
    s.w_CARRY[3] //= s.fas6.cin
    s.w_SUM[3] //= s.fas6.sum
    s.w_CARRY[4] //= s.fas6.cout

    @update
    def upA():
      s.out @= concat(s.w_CARRY[4], s.w_SUM)


#-------------------------------------------------------------------------
# main
#-------------------------------------------------------------------------

if __name__ == "__main__":

  dut = RippleCarryAdder()
  dut.apply(DefaultPassGroup(textwave=True))
  dut.sim_reset()

  dut.in0 @= 2
  dut.in1 @= 0
  dut.sim_tick()

  dut.in0 @= 4
  dut.in1 @= 6
  dut.sim_tick()

  dut.in0 @= 2
  dut.in1 @= 2
  dut.sim_tick()

  dut.in0 @= 0x1
  dut.in1 @= 0x2
  dut.sim_tick()
  dut.sim_tick()

  dut.print_textwave()
