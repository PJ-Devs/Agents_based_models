
import base
from base import initialize, update
import numpy as np
from rules import set_thresholds
from pylab import * 

# Mean of the proportion of similar agents in radius r

def calculate_segregation(r):
    total_percentage = 0
    total_agents_with_neighbors = 0

    for ag in base.agents:
        neighbors = [nb for nb in base.agents if (ag.x - nb.x)**2 + (ag.y - nb.y)**2 < r**2 and nb != ag]
        if neighbors:
            similars = [nb for nb in neighbors if (
                abs(ag.age - nb.age) <= 5 and
                ag.music_like == nb.music_like and
                ag.political_position == nb.political_position
            )]
            porcentaje_similares = len(similars)/ float(len(neighbors))
            total_percentage += porcentaje_similares
            total_agents_with_neighbors += 1
    return float(total_percentage / total_agents_with_neighbors) *100 

def monte_carlo(num_iter=30):
    results = []

    for i in range(num_iter):
        n = np.random.randint(100, 1000)
        r = np.random.uniform(1, 10)

        # Generar thresholds aleatorios para algunas reglas
        random_thresholds = {
            'music_and_age': np.random.uniform(0.2, 1),
            'political_and_music': np.random.uniform(0.2, 1),
        }
        set_thresholds(random_thresholds)

        initialize(n)
        for _ in range(100):
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


results = monte_carlo(10000)

music_thresholds = [res['music_and_age'] for res in results]
political_thresholds = [res['political_and_music'] for res in results]
segregation = [res['segregation'] for res in results]
r_values = [res['r'] for res in results]
n_values = [res['n'] for res in results]

# segregatión vs. music_and_age
figure(figsize=(8,6))
scatter(music_thresholds, segregation, alpha=0.7)
xlabel('Music & Age Threshold')
ylabel('Segregation (%)')
title('Segregation vs. Music & Age Threshold')
show()

# segregatión vs. political_and_music
figure(figsize=(8,6))
scatter(political_thresholds, segregation, alpha=0.7, color='orange')
xlabel('Political & Music Threshold')
ylabel('Segregation (%)')
title('Segregation vs. Political & Music Threshold')
show()

#  segregatión vs. r
figure(figsize=(8,6))
scatter(r_values, segregation, alpha=0.7, color='green')
xlabel('Radio r')
ylabel('Segregation (%)')
title('Segregation vs. Neighborhood Radius')
show()

#  segregatión vs. n
figure(figsize=(8,6))
scatter(n_values, segregation, alpha=0.7, color='purple')
xlabel('Number of Agents')
ylabel('Segregation (%)')
title('Segregation vs. Number of Agents')
show()

colors = ['blue' if music > political else 'red' for music, political in zip(music_thresholds, political_thresholds)]

figure(figsize=(10,6))
scatter(music_thresholds, segregation, c=colors, alpha=0.7)
xlabel('Music & Age Threshold')
ylabel('Segregation (%)')
title('Segregation vs. Thresholds (Color by Dominant Rule)')
grid(True)
show()