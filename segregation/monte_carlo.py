import base
from base import initialize, update
import numpy as np
from rules import set_thresholds

# Mean of the proportion of similar agents in radius r

def calculate_segregation(r):
    total_similars = 0
    total_agents = len(base.agents)

    for ag in base.agents:
        neighbors = [nb for nb in base.agents if (ag.x - nb.x)**2 + (ag.y - nb.y)**2 < r**2 and nb != ag]
        if neighbors:
            similars = [nb for nb in neighbors if (
                abs(ag.age - nb.age) <= 5 and  # age difference
                ag.music_like == nb.music_like and
                ag.political_position == nb.political_position
            )]
           # similars_percentage = len(similars) / len(neighbors)
            total_similars += len(similars)

    print(f"Total agents: {total_agents}, Total similars: {total_similars}")
    if total_agents == 0:
        return 0
    return total_similars / total_agents


def monte_carlo(num_iter=30):
    results = []

    for i in range(num_iter):
        n = np.random.randint(100, 1000)
        r = np.random.uniform(1, 10)

        # Generar thresholds aleatorios para algunas reglas
        random_thresholds = {
            'music_and_age': np.random.uniform(0.2, 0.8),
            'political_and_music': np.random.uniform(0.2, 0.8),
        }
        set_thresholds(random_thresholds)

        initialize(n)
        for _ in range(20):
            update(r)

        segregation = calculate_segregation(r)
        results.append({
            'n': n,
            'r': r,
            **random_thresholds,
            'segregation': segregation
        })
        print(f"Iteration {i+1}: Segregation={segregation:.2f}, Thresholds={random_thresholds}")

    return results

# Llamar a la simulación
if __name__ == '__main__':
    monte_carlo(30)
