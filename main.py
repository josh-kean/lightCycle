import pygame
import car
import math
import random

pygame.init()

playerNames = []
linePosition = []
crashPositions = []
playerScores = {}
playerColors = {}
crashCoordinates = []

width, height = 1000, 1000
colors = {'white': (255, 255, 255), 'black': (0,0,0)}
display = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()
def random_color():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

def random_starting_location():
    return (random.randint(50, int(width/2)), random.randint(int(height/4), int(height*3/4)))

def create_player(playerName, width, length):
    startingPosition = random_starting_location()
    playerScores[playerName] = 0
    playerNames.append(playerName)
    playerColors[playerName] = random_color()
    return car.Car(playerColors[playerName], playerName, [startingPosition[0], startingPosition[1]], width, length)
    #function also checks to make sure random color isn't in list of playerColors

#creates a line 10 car lengths back
def create_line_position(x, y, length, width):
    lineLength = 20
    linePosition.append([x,y, length, width])
    # if len(linePosition) > lineLength:
    #     del linePosition[0]
    # creates list of just x and y coordinates
    crashPositions.append([x,y])
    # if len(crashPositions) > lineLength:
    #     del crashPositions[0]


#draws line from function create_line_position
def draw_line(linePositions, display, color, length, width):
    for position in linePositions:
        pygame.draw.rect(display, color, (position[0], position[1],
            position[2], position[3]))

def clear_lists():
    crashPositions = []
    linePosition = []

def declare_winner(playerName):
    playerNames[playerName] +=1

def light_cycle(display):
    carWidth = 20
    carLength = int(carWidth)
    playerOne = create_player('josh', carWidth, carLength)
    crashed = False

    #have car start in motion going up
    xChange, yChange = carWidth, 0
    event = pygame.event.poll()
    while crashed == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if playerOne.location[0] > width-50 or playerOne.location[0] < 50 or playerOne.location[1] > height-50 or playerOne.location[1] < 50:
            crashed = True
            pygame.quit()
            quit()
        display.fill(colors['white'])
        if playerOne.location in crashPositions[:-1]:
            crashed = True
            pygame.quit()
            quit()

        draw_line(linePosition, display, playerOne.color, playerOne.length, playerOne.width)
        pygame.draw.rect(display, playerOne.color, (playerOne.location[0],
            playerOne.location[1], playerOne.width, playerOne.length))
        carPosition = playerOne.KeyBoard(event, xChange, yChange)
        xChange, yChange = carPosition[0], carPosition[1]
        playerOne.location[0] += carPosition[0]
        playerOne.location[1] += carPosition[1]
        create_line_position(playerOne.location[0],playerOne.location[1], playerOne.width, playerOne.length)
        pygame.display.update()
        clock.tick(20)

def start_screen():
    while True:
        for action in pygame.event.get():
            if action.type == pygame.QUIT:
                pygame.quit()
                quit()
        display.fill(colors['white'])

        light_cycle(display)
        pygame.display.update()

start_screen()
