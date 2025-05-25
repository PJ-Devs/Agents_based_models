from pylab import * 
from rules import evaluate_rules
from Agent import Agent
from rules import set_thresholds

# Evolución de opiniones en jurados deliberativos

agents_data = {
  'genders': ['M', 'F', 'X'],
  'religions': ['Christian', 'Muslim', 'Jewish', 'Hindu', 'Buddhist', 'Atheist'],
  'occupations': ['Doctor', 'Engineer', 'Artist', 'Teacher', 'Scientist', 'Lawyer', 'Chef', 'Driver'],
  'skin_tones' : [ "very light", "light", "light-medium", "medium", "medium-dark", "dark", "very dark"],
  'sports': ['Soccer', 'Basketball', 'Tennis', 'Baseball', 'Swimming', 'Cycling', 'Running', 'Hiking', 'Yoga', 'Dancing', 'Martial Arts', 'Boxing', 'Golf'],
  'music_genres': ['Rock', 'Pop', 'Hip-Hop', 'Jazz', 'Classical', 'Country', 'Reggae', 'Blues', 'Electronic', 'Folk', 'R&B', 'Metal', 'Punk', 'Indie', 'Latin', 'Gospel', 'Soul', 'Disco'],
  'political_positions': ['Left', 'Center', 'Right'],
}

def initialize(n):
  global agents
  
  agents = []
  for _ in range(n):
    ag = Agent()
    
    ag.age = randint(1, 80)
    ag.sex = randint(0, 1)  # 0: Masculino, 1: Femenino
    ag.gender = choice(agents_data['genders'])
    ag.religion = choice(agents_data['religions'])
    ag.skin_color = choice(agents_data['skin_tones'])
    ag.occupation = choice(agents_data['occupations'])
    ag.sports_like = choice(agents_data['sports'])
    ag.music_like = choice(agents_data['music_genres'])
    ag.political_position = choice(agents_data['political_positions'])
    
    agents.append(ag)

def observe():
    global agents

    cla()
    plot([ag.x for ag in agents], [ag.y for ag in agents], 'o', markersize=2)
    title('Agentes')
    xlabel('X')
    ylabel('Y')
    axis('image')
    axis([0, 1, 0, 1])

def update(r):
  global agents
  
  # Seleccionar un agente al azar
  ag = choice(agents)
  
  # Filtrar vecinos en el radio de vecindad
  neighbors = [nb for nb in agents
                if (ag.x - nb.x)**2 + (ag.y - nb.y)**2 < r**2 and nb != ag]
  
  if len(neighbors) > 0:
    should_move = evaluate_rules(ag, neighbors)
    
    if should_move:
      print(f"Se mueve")
      # Mover el agente a una nueva posición aleatoria
      ag.x= random()
      ag.y= random()
    else:
      print(f"No se mueve")

# pycxsimulator.GUI().start(func=[initialize, observe, update])

__all__ = ['agents', 'initialize', 'update']
