from environment import TicTacToe
from agent import QLearningAgent

def print_board(state):
    """Print the board in a more readable format"""
    print("Current Board:")
    for row in state:
        print(" | ".join(str(x) if x != 0 else " " for x in row))
        print("-" * 5)

def human_move(state):
    """Get human input for the move"""
    while True:
        try:
            row, col = map(int, input("Enter your move (row, col): ").split())
            if state[row][col] == 0:  # Check if the cell is empty
                state[row][col] = 1  # Human is represented by '1'
                break
            else:
                print("Cell is already occupied! Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and col as two integers (0-2).")

def agent_move(state, agent):
    """Get the agent's move"""
    action = agent.choose_action(str(state))
    print(f"Agent chooses action: {action}")
    state[action[0]][action[1]] = 2  # Agent is represented by '2'

def main():
    env = TicTacToe()
    agent = QLearningAgent(actions=[(i, j) for i in range(3) for j in range(3)])
    print("Game Start! You are 'X' (1), and the Agent is 'O' (2).")
    
    state = env.reset()
    done = False
    while not done:
        print_board(state)

        # Human player's turn
        print("\nYour turn!")
        human_move(state)
        if env.check_winner(1):  # Check if human wins
            print_board(state)
            print("You win!")
            break
        
        # Check if the game is a draw
        if np.all(state != 0) and not env.check_winner(1) and not env.check_winner(2):
            print_board(state)
            print("It's a draw!")
            break

        # Agent's turn
        print("\nAgent's turn...")
        agent_move(state)
        if env.check_winner(2):  # Check if agent wins
            print_board(state)
            print("Agent wins!")
            break

    print("Game over!")

if __name__ == "__main__":
    main()
