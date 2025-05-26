from Sworn import Sworn
from Environment import Environment
from pylab import *
import numpy as np
from random import random, choice, uniform

class JurySimulation:
    def __init__(self):
        self.sworns = []
        self.environment = None
        self.TR_0 = 200
        self.alpha = 0.8

    def initialize(self):
        self.sworns = [Sworn(
            decision=choice(['culpable', 'inocente']),
            conviction=random()
          ) for _ in range(50)]
        self.environment = Environment(
            remaining_time=self.TR_0,
            social_temperature=0.5,
            positive_evidence=0.2,
            negative_evidence=0.8
        )

    def update(self):
        # Calcula la temperatura social 
        decisions = [1 if j.decision == 'culpable' else 0 for j in self.sworns]
        dispersion = np.std(decisions)
        tr = self.environment.remaining_time
        self.environment.social_temperature = 1 - (tr / self.TR_0) + self.alpha * dispersion

        # Evaluación de cambio de opinión
        for jurado in self.sworns:
            prob_social = self.environment.social_temperature * (1 - jurado.conviction)
            evidencia_contraria = (
                self.environment.negative_evidence if jurado.decision == 'inocente'
                else self.environment.positive_evidence
            )
            prob_evidencia = evidencia_contraria * (1 - jurado.conviction)

            print(jurado.conviction, prob_evidencia + prob_social)
            if jurado.conviction < prob_social + prob_evidencia:
                jurado.decision = 'culpable' if jurado.decision == 'inocente' else 'inocente'
                jurado.conviction = uniform(0.4, 1.0)

        self.environment.remaining_time -= 1

    def observe(self):
      cla()
      
      colors = ['red' if j.decision == 'culpable' else 'green' for j in self.sworns]
      xs = [j.x for j in self.sworns]
      ys = [j.y for j in self.sworns]
      
      count_favorable = sum(1 for j in self.sworns if j.decision == 'culpable')
      count_unfavorable = len(self.sworns) - count_favorable

      text(0.5, 0.95, f"Decisiones: Culpable={count_favorable}, Inocente={count_unfavorable}",
           fontsize=10, ha='center', va='center', color='black')
      text(0.5, 0.90, f"Temperatura social: {self.environment.social_temperature:.2f}",
           fontsize=10, ha='center', va='center', color='black')
      
      for i, jurado in enumerate(self.sworns):
          text(jurado.x, jurado.y, f"{jurado.decision} ({jurado.conviction:.2f})", 
               fontsize=8, ha='center', va='center', color=colors[i])
      scatter(xs, ys, c=colors, s=80, alpha=0.8, edgecolors='k')
      title(f"Opiniones de los Jurados - Tiempo restante: {self.environment.remaining_time}")
      xlabel("X")
      ylabel("Y")
      grid(True)
      xlim(0, 1)
      ylim(0, 1)

    def save_plot(self):
        colors = ['red' if j.decision == 'culpable' else 'green' for j in self.sworns]
        xs = [j.x for j in self.sworns]
        ys = [j.y for j in self.sworns]

        figure(figsize=(6, 6))
        scatter(xs, ys, c=colors, s=80, alpha=0.8, edgecolors='k')
        title(f"Opiniones de los Jurados")
        xlabel("X")
        ylabel("Y")
        grid(True)
        xlim(0, 1)
        ylim(0, 1)
        tight_layout()

        path = "jurado_simulacion.png"
        savefig(path)
        close()
        return path


test_simulation = JurySimulation()
test_simulation.initialize()

while test_simulation.environment.remaining_time > 0:
    test_simulation.observe()
    pause(0.25)
    test_simulation.update()
test_simulation.save_plot()