from pylab import *

class Agent:
  def __init__(
    self, 
    age: int = None,
    sex: int = None,
    gender: str = None, 
    religion: str = None,
    skin_color: str = None,
    occupation: str = None,
    sports_like: str = None,
    music_like: str = None,
    political_position: str = None,
  ):
    self.age = age
    self.sex = sex
    self.gender = gender
    self.religion = religion
    self.skin_color = skin_color
    self.occupation = occupation
    self.sports_like = sports_like
    self.music_like = music_like
    self.political_position = political_position
    
    # Define possible values for each attribute
    self.x = random()
    self.y = random()
    