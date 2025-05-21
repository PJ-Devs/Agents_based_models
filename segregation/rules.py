from Agent import Agent

def music_and_age_compatibility(agent: Agent, nghs: list):
    '''
    This function checks if the agent's music preference and age are compatible with its neighbors.
    The function returns True if the agent should move, and False if it should not move.
    '''
    match_probability = 0.3
    age_offset = 5
    
    # Check which neighbors are within the age offset and have the same music preference
    matching_neighbors = [ngh for ngh in nghs if abs(agent.age - ngh.age) <= age_offset and agent.music_like == ngh.music_like]
    
    # If the proportion of matching neighbors is less than the 30% of total neighbors, return True (The agent should move)
    # Otherwise, return False (The agent should not move)
    if len(matching_neighbors) / len(nghs) < match_probability:
        return True

    return False

def sex_and_sports_compatibility(agent: Agent, nghs: list):
    return True

def genre_and_occupation_compatibility(agent: Agent, nghs: list):
    return True

def skin_color_and_religion_compatibility(agent: Agent, nghs: list):
    return True

def political_position_and_music_compatibility(agent: Agent, nghs: list):
    return True

def age_sex_and_sports_compatibility(agent: Agent, nghs: list):
    return True

def religion_and_profession_compatibility(agent: Agent, nghs: list):
    return True

def genre_music_and_sports_compatibility(agent: Agent, nghs: list):
    return True

def skin_color_and_age_compatibility(agent: Agent, nghs: list):
    return True

def political_position_and_religion_compatibility(agent: Agent, nghs: list):
    return True

def evaluate_rules(agent: Agent, nghs: list):
  if not music_and_age_compatibility(agent, nghs) or \
     not sex_and_sports_compatibility(agent, nghs) or \
     not genre_and_occupation_compatibility(agent, nghs) or \
     not skin_color_and_religion_compatibility(agent, nghs) or \
     not political_position_and_music_compatibility(agent, nghs) or \
     not age_sex_and_sports_compatibility(agent, nghs) or \
     not religion_and_profession_compatibility(agent, nghs) or \
     not genre_music_and_sports_compatibility(agent, nghs) or \
     not skin_color_and_age_compatibility(agent, nghs) or \
     not political_position_and_religion_compatibility(agent, nghs):
    return True

  return False