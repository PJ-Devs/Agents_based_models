from Agent import Agent

THRESHOLDS = {
    'music_and_age': 0.5,
    'sex_and_sports': 0.5,
    'genre_and_occupation': 0.5,
    'skin_color_and_religion': 0.5,
    'political_and_music': 0.5,
    'age_sex_and_sports': 0.5,
    'religion_and_profession': 0.5,
    'genre_music_and_sports': 0.5,
    'skin_color_and_age': 0.5,
    'political_and_religion': 0.5
}

def set_thresholds(new_thresholds: dict):
    global THRESHOLDS
    THRESHOLDS.update(new_thresholds)

def music_and_age_compatibility(agent: Agent, nghs: list):
    '''
    This function checks if the agent's music preference and age are compatible with its neighbors.
    The function returns True if the agent should move, and False if it should not move.
    '''
    match_probability = THRESHOLDS['music_and_age']
    print('match_probability music and age', match_probability)
    age_offset = 10
    
    # Check which neighbors are within the age offset and have the same music preference
    matching_neighbors = [ngh for ngh in nghs if abs(agent.age - ngh.age) <= age_offset and agent.music_like == ngh.music_like]
    
    # If the proportion of matching neighbors is less than the 30% of total neighbors, return True (The agent should move)
    # Otherwise, return False (The agent should not move)
    if len(matching_neighbors) / len(nghs) < match_probability:
        return True

    return False

def sex_and_sports_compatibility(agent: Agent, nghs: list):
    '''
    This function checks  if the agent's sex and sports preference are compatible with its neighbors.
    The function returns True if the agent should move, and False if it should not move.
    '''
    match_probability = THRESHOLDS['sex_and_sports']
    
    # Check which neighbors has the same sex and sports preference
    matching_neighbors = [ngh for ngh in nghs if agent.sex == ngh.sex and agent.sports_like == ngh.sports_like]
    
    # If the proportion of matching neighbors is less than the 40% of total neighbors, return True (The agent should move)
    # Otherwise, return False (The agent should not move)
    if len(matching_neighbors) / len(nghs) < match_probability:
        return True
    return False

def genre_and_occupation_compatibility(agent: Agent, nghs: list):
    '''
    This function checks if the agent's gender and occupation are compatible with its neighbors.
    The function returns True if the agent should move, and False if it should not move. 
    '''
    match_probability = THRESHOLDS['genre_and_occupation']
    
    # Check which neighbors has the same gender and occupation
    matching_neighbors = [ngh for ngh in nghs if agent.gender == ngh.gender and agent.occupation == ngh.occupation]

    # If the proportion of matching neighbors is less than the 50% of total neighbors, return True (The agent should move)
    # Otherwise, return False (The agent should not move)
    if len(matching_neighbors) / len(nghs) < match_probability:
        return True
    return False

def skin_color_and_religion_compatibility(agent: Agent, nghs: list):
    '''
    This function checks if the agent's skin color and religion are compatible with its neighbors.
    The function returns True if the agent should move, and False if it should not move.
    '''
    match_probability = THRESHOLDS['skin_color_and_religion']
    
    # Check which neighbors has the same skin color and religion
    matching_neighbors = [ngh for ngh in nghs if agent.skin_color == ngh.skin_color and agent.religion == ngh.religion]
    
    # If the proportion of matching neighbors is less than the 60% of total neighbors, return True (The agent should move)
    if len(matching_neighbors) / len(nghs) < match_probability:
        return True
    return False

def political_position_and_music_compatibility(agent: Agent, nghs: list):
    '''
    This function checks if the agent's political position and music preference are compatible with its neighbors.
    The function returns True if the agent should move, and False if it should not move.
    '''
    match_probability = THRESHOLDS['political_and_music']

    print('match_probability political and music', match_probability)
    
    # Check which neighbors has the same political position and music preference
    matching_neighbors = [ngh for ngh in nghs if agent.political_position == ngh.political_position and agent.music_like == ngh.music_like]
    
    # If the proportion of matching neighbors is less than the 70% of total neighbors, return True (The agent should move)
    # Otherwise, return False (The agent should not move)
    if len(matching_neighbors) / len(nghs) < match_probability:
        return True
    return False

def age_sex_and_sports_compatibility(agent: Agent, nghs: list):
    '''
    This function checks if the agent's sex, age and sports preference are compatible with its neighbors.
    The function returns True if the agent should move, and False if it should not move.
    '''
    match_probability = THRESHOLDS['age_sex_and_sports']
    age_offset = 10
    
    # Check which neighbors are within the age offset and have the same sex and sports preference
    matching_neighbors = [ngh for ngh in nghs if abs(agent.age - ngh.age) <= age_offset and agent.sex == ngh.sex and agent.sports_like == ngh.sports_like]
    
    # If the proportion of matching neighbors is less than the 35% of total neighbors, return True (The agent should move)
    # Otherwise, return False (The agent should not move)
    if len(matching_neighbors) / len(nghs) < match_probability:
        return True    
    return False

def religion_and_profession_compatibility(agent: Agent, nghs: list):
    '''
    This function checks if the agent's religion and profession are compatible with its neighbors.
    The function returns True if the agent should move, and False if it should not move.
    '''
    
    match_probability = THRESHOLDS['religion_and_profession']
    
    # Check which neighbors has the same religion and profession
    matching_neighbors = [ngh for ngh in nghs if agent.religion == ngh.religion and agent.occupation == ngh.occupation]
    
    # If the proportion of matching neighbors is less than the 45% of total neighbors, return True (The agent should move)
    # Otherwise, return False (The agent should not move)
    if len(matching_neighbors) / len(nghs) < match_probability:
        return True
    return False

def genre_music_and_sports_compatibility(agent: Agent, nghs: list):
    '''
    This function checks if the agent's genre, music preference and sports preference are compatible with its neighbors.
    The function returns True if the agent should move, and False if it should not move.
    '''
    match_probability = THRESHOLDS['genre_music_and_sports']
    
    # Check which neighbors has the same genre, music preference and sports preference
    matching_neighbors = [ngh for ngh in nghs if agent.gender == ngh.gender and agent.music_like == ngh.music_like and agent.sports_like == ngh.sports_like]
    
    # If the proportion of matching neighbors is less than the 55% of total neighbors, return True (The agent should move)
    # Otherwise, return False (The agent should not move)
    if len(matching_neighbors) / len(nghs) < match_probability:
        return True
    return False

def skin_color_and_age_compatibility(agent: Agent, nghs: list):
    '''
    This function checks if the agent's skin color and age are compatible with its neighbors.
    The function returns True if the agent should move, and False if it should not move.
    '''
    match_probability = THRESHOLDS['skin_color_and_age']
    age_offset = 5
    
    # Check which neighbors are within the age offset and have the same skin color
    matching_neighbors = [ngh for ngh in nghs if abs(agent.age - ngh.age) <= age_offset and agent.skin_color == ngh.skin_color]
    
    # If the proportion of matching neighbors is less than the 65% of total neighbors, return True (The agent should move)
    # Otherwise, return False (The agent should not move)
    if len(matching_neighbors) / len(nghs) < match_probability:
        return True
    return False

def political_position_and_religion_compatibility(agent: Agent, nghs: list):
    '''
    This function checks if the agent's political position and religion are compatible with its neighbors.
    The function returns True if the agent should move, and False if it should not move.
    '''
    match_probability = THRESHOLDS['political_and_religion']
    
    # Check which neighbors has the same political position and religion
    matching_neighbors = [ngh for ngh in nghs if agent.political_position == ngh.political_position and agent.religion == ngh.religion]
    
    # If the proportion of matching neighbors is less than the 75% of total neighbors, return True (The agent should move)
    # Otherwise, return False (The agent should not move)
    if len(matching_neighbors) / len(nghs) < match_probability:
        return True
    return False

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

def evaluate_music_political_and_age(agent: Agent, nghs: list):
    if not music_and_age_compatibility(agent, nghs) or not political_position_and_music_compatibility(agent, nghs):
        return False
    return True