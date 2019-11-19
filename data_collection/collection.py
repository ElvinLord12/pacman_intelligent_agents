from pacman.pacman_board import PacmanBoard
from pacman.pacman_driver import tiles
from pacman.pacman_agents import *
from pacman.ghost_agents import GhostRandom
from pacman.pacman_game import PacmanGame
from copy import deepcopy
from pacman.board_raw import *

def main():
    board = PacmanBoard(tiles)

    ghost1 = GhostRandom(vector(-180, 160), vector(10, 0), board)
    ghost2 = GhostRandom(vector(-180, -160), vector(0, 10), board)
    ghost3 = GhostRandom(vector(100, -160), vector(-10, 0), board)
    ghost4 = GhostRandom(vector(100, -140), vector(-10, 0), board)

    ghosts = list()
    ghosts.append(ghost1)
    ghosts.append(ghost2)
    ghosts.append(ghost3)
    ghosts.append(ghost4)
    pacman = PacmanRandom(vector(-40, 80), vector(0, 5), board)

    game = PacmanGame(board, deepcopy(pacman), deepcopy(ghosts))
    game.game_setup()

if __name__ == '__main__':
    main()