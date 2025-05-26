from pylab import * 
from rules import evaluate_music_political_and_age
from Agent import Agent
from plotting import plot_seggreations

# Evolución de opiniones en jurados deliberativos

agents_data = {
  'genders': ['M', 'F', 'X'],
  'religions': ['Christian', 'Muslim', 'Jewish', 'Hindu', 'Buddhist', 'Atheist'],
  'occupations': ['Doctor', 'Engineer', 'Artist', 'Teacher', 'Scientist', 'Lawyer', 'Chef', 'Driver'],
  'skin_tones' : [ "very light", "light", "light-medium", "medium", "medium-dark", "dark", "very dark"],
  'sports': ['Soccer', 'Basketball', 'Tennis', 'Baseball', 'Swimming'],
  'music_genres': ['Rock', 'Pop', 'Hip-Hop', 'Jazz', 'Classical'],
  'political_positions': ['Left', 'Center', 'Right'],
}

def initialize(n):
  global agents
  
  agents = []
  for _ in range(n):
    ag = Agent()
    
    ag.age = randint(1, 80)
    ag.sex = randint(0, 2)  # 0: Masculino, 1: Femenino
    ag.gender = choice(agents_data['genders'])
    ag.religion = choice(agents_data['religions'])
    ag.skin_color = choice(agents_data['skin_tones'])
    ag.occupation = choice(agents_data['occupations'])
    ag.sports_like = choice(agents_data['sports'])
    ag.music_like = choice(agents_data['music_genres'])
    ag.political_position = choice(agents_data['political_positions'])
    
    agents.append(ag)

def observe(iteration: int):
    global agents

    cla()
    plot([ag.x for ag in agents], [ag.y for ag in agents], 'o', markersize=2)
    title(f'Iteration {iteration}')
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
    should_move = evaluate_music_political_and_age(ag, neighbors)
    
    if should_move:
      # Mover el agente a una nueva posición aleatoria
      ag.x, ag.y = random(), random()

def make_seggreation_plots():
  global agents
  plot_seggreations(agents)

__all__ = ['agents', 'initialize', 'update', 'make_seggreation_plots']
