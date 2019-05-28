import pygame
import car
import math
import random

pygame.init()

playerNames = []
playerScores = {}
playerColors = {}
crashCoordinates = []

width, height = 750, 750
colors = {'white': (255, 255, 255), 'black': (0,0,0)}
display = pygame.display.set_mode((width, height))

def random_color():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

# def random_starting_location():
#     return (random.randint(50, 750), random.randint(50, 750))

def create_player(playerName, width, length):
    playerScores[playerName] = 0
    playerNames.append(playerName)
    playerColors[playerName] = random_color()
    return car.Car(playerColors[playerName], playerName, (100, 200), width, length)
    #function also checks to make sure random color isn't in list of playerColors

def declare_winner(playerName):
    playerNames[playerName] +=1

def detect_crash(location, player):
    if location in crashCoordinates:
        #other player is declared winner
        winner = string(playerNames.pop(player))
    declare_winner(player)

def light_cycle(display):
    carLength = 50
    carWidth = int(carLength/2)
    playerOne = create_player('josh', carWidth, carLength)
    crashed = False
    while crashed == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.draw.rect(display, playerOne.color, (playerOne.location[0],
            playerOne.location[1], playerOne.width, playerOne.length))
        pygame.display.update()

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
