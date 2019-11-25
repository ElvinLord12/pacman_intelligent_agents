from pacman.pacman_game import PacmanGame
from pacman.pacman_agents import PacmanRandom, PacmanBetterRandom, HumanPacman
from pacman.ghost_agents import GhostRandom, GhostBetter
from copy import deepcopy
from pacman.board_raw import *
from pacman.pacman_board import PacmanBoard
from datetime import *

def collect_data(num_games=50):

    # defines the board
    board = PacmanBoard(deepcopy(tiles))

    pacman = PacmanRandom(position, direction, board)
    pacmanBetter = PacmanBetterRandom(position, direction, board)
    human = HumanPacman(position, direction, board)
    
    ghost = vector(-180,160)
    ghost2 = vector(-180, -160)
    ghost3 = vector(100, 160)
    ghost4 = vector(100, -160)
    ghostDir = vector(5, 0)
    ghostDir1 = vector(0, 5)
    ghostDir2 = vector(0, -5)
    ghostDir3 = vector(-5, 0)

    blinky = GhostBetter(ghost, ghostDir, board, pacman)
    pinky = GhostBetter(ghost2, ghostDir1, board, pacman)
    inky = GhostBetter(ghost3, ghostDir2, board, pacman)
    clide = GhostBetter(ghost4, ghostDir3, board, pacman)

    bae = GhostRandom(ghost, ghostDir, board)
    bae1 = GhostRandom(ghost2, ghostDir1, board)
    bae2 = GhostRandom(ghost3, ghostDir2, board)
    bae3 = GhostRandom(ghost4, ghostDir3, board)


    ghostz = [blinky, pinky, inky, clide]
    badGhosts = [bae, bae1, bae2, bae3]

    game = PacmanGame(board, deepcopy(human), deepcopy(ghostz))
    game.game_setup()

    # defines the pacman
    pacman_position = vector(-40, -80)
    pacman_direction = vector(0, -5)
    pacman_PacmanBetterRandom = PacmanBetterRandom(pacman_position, pacman_direction, board)

    # collects data about each game
    for num in range(num_games):
        result = ""
        game = PacmanGame(deepcopy(board), deepcopy(pacman_PacmanBetterRandom), deepcopy(ghost_list))
        start = datetime.now()
        game.game_setup()
        result = str((datetime.now() - start).total_seconds()) + "," + str(game.state.get('score'))
        print(result)

def test_game():
    position = vector(-40, -80)
    direction = vector(0, -5)

    board = PacmanBoard(deepcopy(tiles))

    pacman = PacmanRandom(position, direction, board)
    pacmanBetter = PacmanBetterRandom(position, direction, board)


    ghost = vector(-180,160)
    ghostDir = vector(10, 0)

    ghosty = GhostRandom(ghost, ghostDir, deepcopy(tiles))
    ghostz = [ghosty]

    game = PacmanGame(board, deepcopy(pacmanBetter), deepcopy(ghostz))
    game.game_setup()

def main():
    collect_data()

if __name__ == '__main__':
    main()