from matplotlib import pylab as plt
import os

# Get the absolute path to the project root directory
current_dir = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(current_dir)
SEGREGATION_DIR = os.path.join(PROJECT_ROOT, 'segregation')
PLOTS_DIR = os.path.join(SEGREGATION_DIR, 'plots')

# Create plots directory if it doesn't exist
os.makedirs(PLOTS_DIR, exist_ok=True)

def plot_seggreagtion_by_age(agents: list):
  '''
  Plots the segregation by age.

  Divides the age in intervals of 10 years.

  Args:
    agents: list of agents

  Returns:
    None
  '''
  groups_by_ages = [[] for _ in range(8)]

  for agent in agents:
    age_index = agent.age // 10
    groups_by_ages[age_index].append(agent)
    
  plot_colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink', 'brown']
  
  for i, group in enumerate(groups_by_ages):
    plt.scatter([agent.x for agent in group], [agent.y for agent in group], color=plot_colors[i], label=f'Age {i*10}-{(i+1)*10-1}')
  
  plt.title('Segregation by Age')
  plt.legend(loc='upper right')
  output_path = os.path.join(PLOTS_DIR, 'segregation_by_age.png')
  plt.savefig(output_path)
  plt.close()

def plot_seggreagtion_by_sex(agents: list):
  males = [agent for agent in agents if agent.sex == 0]
  females = [agent for agent in agents if agent.sex == 1]
  
  plt.scatter([ag.x for ag in males], [ag.y for ag in males], color='blue', label='Males')
  plt.scatter([ag.x for ag in females], [ag.y for ag in females], color='red', label='Females')
  
  plt.title('Segregation by Sex')
  plt.legend(loc='upper right')
  output_path = os.path.join(PLOTS_DIR, 'segregation_by_sex.png')
  plt.savefig(output_path)
  plt.close()

def plot_seggreagtion_by_gender(agents: list):
  groups_by_gender = {
    'M': [agent for agent in agents if agent.gender == 'M'],	
    'F': [agent for agent in agents if agent.gender == 'F'],
    'X': [agent for agent in agents if agent.gender == 'X'],
  }
  
  plot_colors = ['blue', 'red', 'green']
  for i, (gender, group) in enumerate(groups_by_gender.items()):
    plt.scatter([agent.x for agent in group], [agent.y for agent in group], color=plot_colors[i], label=gender)
  
  plt.title('Segregation by Gender')
  plt.legend(loc='upper right')
  output_path = os.path.join(PLOTS_DIR, 'segregation_by_gender.png')
  plt.savefig(output_path)
  plt.close()

def plot_seggreagtion_by_religion(agents: list):
  religions = ['Christian', 'Muslim', 'Jewish', 'Hindu', 'Buddhist', 'Atheist']

  plot_colors = ['blue', 'red', 'green', 'yellow', 'purple', 'orange']
  for i, religion in enumerate(religions):
    group = [agent for agent in agents if agent.religion == religion]
    plt.scatter([agent.x for agent in group], [agent.y for agent in group], color=plot_colors[i], label=religion)
  
  plt.title('Segregation by Religion')
  plt.legend(loc='upper right')
  output_path = os.path.join(PLOTS_DIR, 'segregation_by_religion.png')
  plt.savefig(output_path)
  plt.close()

def plot_seggreagtion_by_skin_color(agents: list):
  skin_tones = [ "very light", "light", "light-medium", "medium", "medium-dark", "dark", "very dark"]

  plot_colors = ['blue', 'red', 'green', 'yellow', 'purple', 'orange', 'pink']
  for i, skin_tone in enumerate(skin_tones):
    group = [agent for agent in agents if agent.skin_color == skin_tone]
    plt.scatter([agent.x for agent in group], [agent.y for agent in group], color=plot_colors[i], label=skin_tone)
  
  plt.title('Segregation by Skin Color')
  plt.legend(loc='upper right')
  output_path = os.path.join(PLOTS_DIR, 'segregation_by_skin_color.png')
  plt.savefig(output_path)
  plt.close()

def plot_seggreagtion_by_occupation(agents: list):
  occupations = ['Doctor', 'Engineer', 'Artist', 'Teacher', 'Scientist', 'Lawyer', 'Chef', 'Driver']

  plot_colors = ['blue', 'red', 'green', 'yellow', 'purple', 'orange', 'pink', 'brown']
  for i, occupation in enumerate(occupations):
    group = [agent for agent in agents if agent.occupation == occupation]
    plt.scatter([agent.x for agent in group], [agent.y for agent in group], color=plot_colors[i], label=occupation)
  
  plt.title('Segregation by Occupation')
  plt.legend(loc='upper right')
  output_path = os.path.join(PLOTS_DIR, 'segregation_by_occupation.png')
  plt.savefig(output_path)
  plt.close()

def plot_seggreagtion_by_sports_likes(agents: list):
  sports = ['Soccer', 'Basketball', 'Tennis', 'Baseball', 'Swimming']
  plot_colors = ['blue', 'red', 'green', 'yellow', 'purple']

  for i, sport in enumerate(sports):
    group = [agent for agent in agents if agent.sports_like == sport]
    plt.scatter([agent.x for agent in group], [agent.y for agent in group], color=plot_colors[i], label=sport)
  
  plt.title('Segregation by Sports Likes')
  plt.legend(loc='upper right')
  output_path = os.path.join(PLOTS_DIR, 'segregation_by_sports_likes.png')
  plt.savefig(output_path)
  plt.close()

def plot_seggreagtion_by_music_likes(agents: list):
  music_genres = ['Rock', 'Pop', 'Hip-Hop', 'Jazz', 'Classical']
  plot_colors = ['blue', 'red', 'green', 'yellow', 'purple']

  for i, music_genre in enumerate(music_genres):
    group = [agent for agent in agents if agent.music_like == music_genre]
    plt.scatter([agent.x for agent in group], [agent.y for agent in group], color=plot_colors[i], label=music_genre)
  
  plt.title('Segregation by Music Likes')
  plt.legend(loc='upper right')
  output_path = os.path.join(PLOTS_DIR, 'segregation_by_music_likes.png')
  plt.savefig(output_path)
  plt.close()

def plot_seggreagtion_by_political_position(agents: list):
  political_positions = ['Left', 'Center', 'Right']
  plot_colors = ['blue', 'red', 'green']
  
  for i, political_position in enumerate(political_positions):
    group = [agent for agent in agents if agent.political_position == political_position]
    plt.scatter([agent.x for agent in group], [agent.y for agent in group], color=plot_colors[i], label=political_position)

  plt.title('Segregation by Political Position')
  plt.legend(loc='upper right')
  output_path = os.path.join(PLOTS_DIR, 'segregation_by_political_position.png')
  plt.savefig(output_path)
  plt.close()

def plot_seggreations(agents: list):
  plot_seggreagtion_by_age(agents)
  plot_seggreagtion_by_gender(agents)
  plot_seggreagtion_by_music_likes(agents)
  plot_seggreagtion_by_occupation(agents)
  plot_seggreagtion_by_political_position(agents)
  plot_seggreagtion_by_religion(agents)
  plot_seggreagtion_by_sex(agents)
  plot_seggreagtion_by_skin_color(agents)
  plot_seggreagtion_by_sports_likes(agents)