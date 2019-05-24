class Car:
    def __init__(self, width=50, length=100, color, player):
        self.width = width
        self.length = length
        self.color = color
        self.player = player

    def displayCar(self):
        #draw a square of length, width, and color
        pass

    def leaveRail(self, time=60):
        #keep a square at cars previous location for set amount of time
        pass

    def KeyBoard(event, x_change, y_change):
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