import random
global justate

def firstonmap():
    return [random.randint(0, 9), random.randint(0, 9)]

class Sheep:
    def __init__(self, name):
        self.name = name
        self.position = firstonmap()
        print(self.name + ' first on ' + str(self.position))

    def __del__(self):
        pass

    def dead(self):
        global justate
        justate = self.name
        print(self.name + ' is dead')
        Sheep.__del__

    def walk(self):
        direction = random.choice(['x', 'y'])
        if direction == 'x':
            step = random.choice([-1, 1])
            if self.position[0] + step > 9:
                self.position[0] = 18 - self.position[0] - step
            elif self.position[0] + step < 0:
                self.position[0] = 0 - self.position[0] - step
            else:
                self.position[0] += step
        else:
            step = random.choice([-1, 1])
            if self.position[1] + step > 9:
                self.position[1] = 18 - self.position[1] - step
            elif self.position[1] + step < 0:
                self.position[1] = 0 - self.position[1] - step
            else:
                self.position[1] += step

        print(self.name + ' now on ' + str(self.position))

class Wolf:
    def __init__(self , name):
        self.name = name
        self.energy = 100
        self.position = firstonmap()
        print(self.name + ' first on ' + str(self.position))

    def walk(self):
        direction = random.choice(['x', 'y'])
        if direction == 'x':
            step = random.choice([-2, 2, -1, 1])
            if self.position[0] + step > 9:
                self.position[0] = 18 - self.position[0] - step
            elif self.position[0] + step < 0:
                self.position[0] = 0 - self.position[0] - step
            else:
                self.position[0] += step
        else:
            step = random.choice([-2, 2, -1, 1])
            if self.position[1] + step > 9:
                self.position[1] = 18 - self.position[1] - step
            elif self.position[1] + step < 0:
                self.position[1] = 0 - self.position[1] - step
            else:
                self.position[1] += step
            
        self.energy = self.energy - 1
        print(self.name + ' now on ' + str(self.position))
    
    def eat(self):
        self.energy = self.energy + 20
        print('/!/!/!/!/!/Wolf just ate ' + justate + '/!/!/!/!/!/!/')

def Play(): 
    sheeps = [Sheep('Sheep' + str(i)) for i in range(1, 11)]
    wolf = Wolf('wolf')
    sum = 0

    while True:
        sum += 1
        print('-------------')
        print('ROUND '+ str(sum))
        print('-------------')

        for sheep in sheeps:
            sheep.walk()
        wolf.walk()

        for sheep in sheeps:
            if wolf.position == sheep.position:
                sheep.dead()
                wolf.eat()
                sheeps.remove(sheep)

        if len(sheeps) == 0:
            print("All sheeps have been ate")
            print("Game Over!")
            break
        
        elif wolf.energy <= 0:
            print("Wolf too tired")
            print("Game Over!")
            break

Play()