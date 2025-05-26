from pylab import *

class Sworn:
  def __init__(
    self, 
    decision: str = None,
    conviction: float = None,
  ):
    self.decision = decision
    self.conviction = conviction
    self.x = random()
    self.y = random()

  def __repr__(self):
    return (
      f"decision={self.decision}, "
      f"conviction={self.conviction}, "
      f"x={self.x}, "
      f"y={self.y})"
    )