"""Code was pulled and modified from free-python-games written by Grant Jenks under an Apache License"""

from random import choice
from turtle import *
from freegames import floor, vector

# left | right | up | down
options = [
    vector(5, 0),
    vector(-5, 0),
    vector(0, 5),
    vector(0, -5),
]

class PacmanBoard:
    def __init__(self, board, pacman, ghosts):
        self.state = {'score': 0}
        self.board = board  # defines the board takes a array
        self.pacman = pacman  # defines location of pacman and initializes him
        self.ghosts = ghosts  # defines the locations and faces of ghosts

        self.path = Turtle(visible=False)
        self.writer = Turtle(visible=False)
        self.aim = vector(0, -5)
        # self.going = self.pacman + self.aim

        self.pacman_tragectories = [0, 0, 0, 0]

    def build_board(self, x, y):
      
        self.path.up()
        self.path.goto(x,y)
        self.path.down()
        self.path.begin_fill()

        for count in range(4):
            self.path.forward(20)
            self.path.left(90)

        self.path.end_fill()

    def draw_world(self):  # replaces world function
        bgcolor('black')  # background color
        self.path.color('blue')  # path color

        for index in range(len(self.board)):  # loops through board array to draw
            tile = self.board[index]

            if tile > 0:  # builds walls
                x = (index % 20) * 20 - 200
                y = 180 - (index // 20) * 20
                self.build_board(x, y)

                if tile == 1:  # builds paths
                    self.path.up()
                    self.path.goto(x + 10, y + 10)
                    self.path.dot(2, 'white')  # creates pellets

    def get_offset(self, point):  # replaces offset function
        x = (floor(point.x, 20) + 200) / 20
        y = (180 - floor(point.y, 20)) / 20
        index = int(x + y * 20)
        return index  # returns the offset within the board (for UI purposes)

    def valid_move(self, point):  # replaces valid function
        index = self.get_offset(point)

        if self.board[index] == 0:
            return False

        index = self.get_offset(point + 19)

        if self.board[index] == 0:
            return False

        return point.x % 20 == 0 or point.y % 20 == 0

    def move(self, x, y):  # any change in movement direction is handled here
        if self.valid_move(self.pacman + vector(x, y)):
            self.aim.x = x
            self.aim.y = y
            print("hit change move function")
            print(self.aim)

    def scoring(self, position):  # pellet collection function
        if self.board[position] == 1:
            self.board[position] = 2
            self.state['score'] += 1
            x = (position % 20) * 20 - 200
            y = 180 - (position // 20) * 20
            self.build_board(x, y)

    def kill_pacman(self, pacman, point):
        if abs(pacman - point) < 20:
            return  # exit case
        else:
            pass

    def make_moves(self):
        self.writer.undo()
        self.writer.write(self.state['score'])

        clear()

        # valid moves array

        options = [
            vector(10, 0),
            vector(-10, 0),
            vector(0, 10),
            vector(0, -10),
        ]

        movement = choice(options)

        # valid moves in a direction then move

        if self.valid_move(self.pacman + self.aim):
            self.pacman.move(self.aim)  # executes the move defined by aim on pacman
            self.going = self.pacman + self.aim  # space we are going to

        print(self.pacman)

        '''this is a similar mechanism to the default ghost AI'''
        # valid moves in a direction then move
        if self.valid_move(self.pacman + self.aim):
            self.pacman.move(self.aim)
        else:
            while not self.valid_move(self.pacman + self.aim): # continues to choose a random direction to move in until the selected aim results in a valid move
                self.aim = choice(options)
            self.pacman.move(self.aim)

        self.pacman_tragectories[options.index(self.aim)] += 1
        position = self.get_offset(self.pacman)  # pacman's current position
        self.scoring(position)

        up()
        goto(self.pacman.x + 10, self.pacman.y + 10)
        dot(20, 'yellow')

        # if self.valid_move(self.pacman + self.aim):  # moves pacman
        #     self.pacman.move(self.aim)

        '''this is default ghost AI will interface later focusing on pacman right now '''
        for point, course in self.ghosts:
            if self.valid_move(point + course):
                point.move(course)
                print(course)
            else:
                # left | right | up | down
                options = [
                    vector(10, 0),
                    vector(-10, 0),
                    vector(0, 10),
                    vector(0, -10),
                ]
                plan = choice(options)  # random choice
                course.x = plan.x
                course.y = plan.y

            up()
            goto(point.x + 10, point.y + 10)
            dot(20, 'red')

        print("did we get here?")

        update()  # updates the board

        for point, course in self.ghosts:  # kill pacman function
            if abs(self.pacman - point) < 20:
                return

        ontimer(self.make_moves, 10)  # loops make_moves at 80fps

    def game_setup(self):
        setup(420, 420, 370, 0)
        hideturtle()
        tracer(False)
        self.writer.goto(160, 160)
        self.writer.color('white')
        self.writer.write(self.state['score'])
        listen()
        # input setup (remove when AI)
        '''these are used for the user to make moves instead of the AI'''
        # onkey(lambda: self.move(5, 0), 'Right')
        # onkey(lambda: self.move(-5, 0), 'Left')
        # onkey(lambda: self.move(0, 5), 'Up')
        # onkey(lambda: self.move(0, -5), 'Down')
        self.draw_world()
        '''while loop to continue moving while pacman has not been killed'''
        while not self.is_finished:
            self.make_moves()
        '''this is used to reset the simulation for multiple uses instead of "done" call'''
        clearscreen()
        resetscreen()
        # done()

