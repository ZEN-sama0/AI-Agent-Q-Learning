from environment import TicTacToe
from agent import QLearningAgent

def main():
    env = TicTacToe()
    agent = QLearningAgent(actions=[(i, j) for i in range(3) for j in range(3)])
    episodes = 1000

    for episode in range(episodes):
        state = env.reset()
        done = False

        while not done:
            action = agent.choose_action(str(state))
            try:
                next_state, done = env.step(action, player=1)
                reward = 1 if env.winner == 1 else 0
                agent.update(str(state), action, reward, str(next_state))
                state = next_state
            except ValueError:
                continue

    print("Training complete!")
    print(f"Q-Table: {agent.q_table}")

if __name__ == "__main__":
    main()
