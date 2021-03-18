from random import random
from math import floor
from random import randint


def wieght_func(x, w):
    sumw = 0
    for i in range(len(x)):
        sumw += (w[i]*x[i])
    return sumw


def value_func(x, v):
    sumv = 0
    for i in range(len(x)):
        sumv += (v[i]*x[i])
    return sumv


class individual():

    def __init__(self, length, w, max_wieght):  # constructor
        average = round(sum(w)/length)
        rand = round(max_wieght/average)
        listt = [randint(0, rand) for x in range(length)]
        self.position = listt

        self.pbestPosition = [0 for x in range(length)]
        self.pbestfittness = 0
        self.velocity = [0 for x in range(length)]

    def evaluate(self, w, v, max_value):
        value = value_func(self.position, v)
        wieght = wieght_func(self.position, w)

        if(wieght <= max_value):  # check if wieght lower than max_wieght

            # check to see if the current position is an individual best
            if(value > self.pbestfittness):
                self.pbestfittness = value
                self.pbestPosition = self.position
    # update new particle velocity

    def update_velocity(self, gbestPosition):
        # constant inertia weight (how much to weigh the previous velocity)
        w = 0.5
        c1 = 2        # cognative constant
        c2 = 0.5     # social constant

        for i in range(0, len(self.velocity)):
            r1 = random()
            r2 = random()

            vel_global = c1*r1*(self.pbestPosition[i]-self.position[i])
            vel_local = c2*r2*(gbestPosition[i]-self.position[i])
            self.velocity[i] = floor(w*self.velocity[i]+vel_global+vel_local)

    # update the particle position based off new velocity updates
    def update_position(self, bound=0):
        for i in range(0, len(self.velocity)):
            self.position[i] = self.position[i]+self.velocity[i]

            if self.position[i] < bound:
                self.position[i] = bound

# i will here minimize position if wieght more than max random


class PSO():
    def __init__(self, v, w, max_wieght, lenght, count, max_iteration):

        gbestfittness = 0                  # best error for group
        # best position for group
        gbestPosition = [0 for x in range(lenght)]

        # establish the swarm
        population = [individual(lenght, w, max_wieght) for x in range(count)]

        # begin optimization loop
        i = 0
        while i < max_iteration:
            # print i,err_best_g
            # cycle through particles in swarm and evaluate fitness
            for j in range(0, count):
                population[j].evaluate(w, v, max_wieght)

                # determine if current particle is the best (globally)
                if population[j].pbestfittness > gbestfittness:
                    gbestPosition = list(population[j].position)
                    gbestfittness = population[j].pbestfittness

            print(gbestfittness)  # maximum value
            print(gbestPosition)  # which items are selected
            # cycle through swarm and update velocities and position
            for j in range(0, count):
                population[j].update_velocity(gbestPosition)
                population[j].update_position()

            i += 1


w = [24, 10, 10, 7]
v = [24, 18, 18, 10]
max_wieght = 25
lenght = 4
count = 1
max_iteration = 5
z = PSO(v, w, max_wieght, lenght, count, max_iteration)
