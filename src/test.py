from environment import TicTacToe
from agent import QLearningAgent

def main():
    env = TicTacToe()
    agent = QLearningAgent(actions=[(i, j) for i in range(3) for j in range(3)])
    print("Testing...")

    state = env.reset()
    done = False
    while not done:
        action = agent.choose_action(str(state))
        print(f"Action chosen: {action}")
        state, done = env.step(action, player=1)
        print(f"State:\n{state}")
    print("Game over!")

if __name__ == "__main__":
    main()
