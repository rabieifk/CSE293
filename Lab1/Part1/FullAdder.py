
class FullAdderFR(Component):

  def construct(s):
    s.a = InPort()
    s.b = InPort()
    s.cin = InPort()
    s.sum = OutPort()
    s.cout = OutPort()
    
    
    
