from environment import TicTacToe
from agent import QLearningAgent
import numpy as np

def main():
    env = TicTacToe()
    agent = QLearningAgent(actions=[(i, j) for i in range(3) for j in range(3)])
    episodes = 1000  # Number of training episodes
    print("Training started...")

    for episode in range(episodes):
        state = env.reset()
        done = False
        while not done:
            action = agent.choose_action(str(state))
            try:
                # Take the action and get the next state
                next_state, done = env.step(action, player=1)
                reward = 1 if env.winner == 1 else 0  # Reward for the human player winning
                agent.update(str(state), action, reward, str(next_state))
                state = next_state  # Move to the next state
            except ValueError:
                # Skip invalid moves and continue
                continue

        # Optionally print some training progress information
        if (episode + 1) % 100 == 0:
            print(f"Episode {episode + 1}/{episodes} completed...")

    print("Training complete!")
    print("Q-Table:")
    for key, value in agent.q_table.items():
        print(f"State: {key[0]} Action: {key[1]} Q-value: {value}")

if __name__ == "__main__":
    main()
