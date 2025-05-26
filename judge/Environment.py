class Environment:
  def __init__(
    self,
    remaining_time: int = 10,
    social_temperature: float = 0.5,
    positive_evidence: float = 0.5,
    negative_evidence: float = 0.5,
  ):
    self.remaining_time = remaining_time
    self.social_temperature = social_temperature
    self.positive_evidence = positive_evidence
    self.negative_evidence = negative_evidence

  def __repr__(self):
    return (
      f"Environment(remaining_time={self.remaining_time}, "
      f"social_temperature={self.social_temperature}, "
      f"positive_evidence={self.positive_evidence}, "
      f"negative_evidence={self.negative_evidence}, "
    )
