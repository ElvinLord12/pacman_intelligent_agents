from pacman.pacman_game import PacmanGame
from pacman.pacman_agents import PacmanRandom, PacmanBetterRandom
from pacman.ghost_agents import GhostRandom
from copy import deepcopy
from pacman.board_raw import *
from pacman.pacman_board import PacmanBoard
from datetime import *

def collect_data(num_games=50):

    # defines the board
    board = PacmanBoard(deepcopy(tiles))

    # defines the ghosts
    ghost_1_position = vector(-180, -160)
    ghost_1_direction = vector(10, 0)
    ghost_1 = GhostRandom(ghost_1_position, ghost_1_direction, board)

    ghost_2_position = vector(100, 160)
    ghost_2_direction = vector(-10, 0)
    ghost_2 = GhostRandom(ghost_2_position, ghost_2_direction, board)

    ghost_3_position = vector(100, -160)
    ghost_3_direction = vector(0, 10)
    ghost_3 = GhostRandom(ghost_3_position, ghost_3_direction, board)

    ghost_4_position = vector(100, -140)
    ghost_4_direction = vector(0, -10)
    ghost_4 = GhostRandom(ghost_4_position, ghost_4_direction, board)

    ghost_list = [ghost_1, ghost_2, ghost_3, ghost_4]

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