import numpy as np
import random

class QLearningAgent:
    def __init__(self, actions, alpha=0.1, gamma=0.9, epsilon=1.0):
        self.q_table = {}
        self.actions = actions
        self.alpha = alpha  # Learning rate
        self.gamma = gamma  # Discount factor
        self.epsilon = epsilon  # Exploration rate

    def get_q_value(self, state, action):
        return self.q_table.get((state, action), 0.0)

    def choose_action(self, state):
        if random.random() < self.epsilon:
            return random.choice(self.actions)
        else:
            q_values = [self.get_q_value(state, action) for action in self.actions]
            return self.actions[np.argmax(q_values)]

    def update(self, state, action, reward, next_state):
        old_value = self.get_q_value(state, action)
        next_max = max([self.get_q_value(next_state, a) for a in self.actions], default=0)
        new_value = old_value + self.alpha * (reward + self.gamma * next_max - old_value)
        self.q_table[(state, action)] = new_value
