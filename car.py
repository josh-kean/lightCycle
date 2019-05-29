import pygame

class Car:
    def __init__(self, color, player, location, width=50, length=100):
        self.width = width
        self.length = length
        self.color = color
        self.player = player
        self.location = location


    def displayCar(self, display):
        # self.display = display
        pygame.draw.rect(display, self.color, (self.location[0], self.location[1], self.width, self.length))

    def leaveRail(self, time=60):
        #keep a square at cars previous location for set amount of time
        pass

    def KeyBoard(self, event, x_change, y_change):
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT and x_change == 0:
                x_change = -self.length
                y_change = 0
            elif event.key == pygame.K_RIGHT and x_change == 0:
                x_change = self.length
                y_change = 0
            elif event.key == pygame.K_UP and y_change == 0:
                y_change = -self.length
                x_change = 0
            elif event.key == pygame.K_DOWN and y_change == 0:
                y_change = self.length
                x_change = 0
        return [x_change, y_change]
