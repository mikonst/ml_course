#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 12:42:04 2017

@author: kelvin
"""

import numpy as np
import matplotlib.pyplot as plt
import random

""" DATA """
# 'size, m2'
X = np.array([42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70])
# 'price, $1000'
Y = np.array([41, 46, 44, 49, 48, 56, 51, 52, 59, 58, 66, 61, 68, 66, 71])


""" this function just plotting
    your data and linear model """
def plot_result(X, Y, model):
    b = model[0]
    w = model[1]
    t = np.arange(X.min(), X.max(), 0.01)
    plt.xlabel('size, m2')
    plt.ylabel('price, $1000')
    plt.plot(X,Y, 'bo', # 'bo' - means 'b'-blue 'o'-dots, you can use 'ro' or 'gx' ('x' for cross) =)
             t, w*t+b , 'k'
             )
    plt.show()
    return 0


my_model = [2, 0.95] # [b, k] just an example [ y = 0.95*x + 2 ] this represents your model as a linear function y = k*x + b
plot_result(X,Y, my_model)


""" this function predicts the cost depends
    on X (size, m2) value and your model """
def linear_model(X, model):
    b = model[0]
    w = model[1]
    y_pred = w*X+b
    return y_pred


""" this is our loss function, we want
    to find the model with smallest loss """
def mean_square_error(X, Y, model):
    J = 0
    m = len(Y)
    for i, y in enumerate(Y):
        J += (1/(2*m))*(linear_model(X[i], model)-Y[i])**2
    return J


""" this function generate initian
    random-gen population of size p """
def generate_population(p, w_size):
    population = []
    for i in range(p):
        model = []
        for j in range(w_size + 1): # +1 for b (bias term)
            model.append(2 * random.random() - 1)  # random initialization from -1 to 1 for b and w
        population.append(model)
    return np.array(population)


""" this function change the gen by adding some
    random value from [-m,m] with probability = t """
def mutation(genom, t=0.5, m=0.025):
    mutant = []
    for gen in genom:
        if random.random() <= t:
            gen += m*(2*random.random() -1)
        mutant.append(gen)
    return mutant


""" this function select the best n = population
    gens from all offspring in this generation """
def selection(offspring, population):
    offspring.sort()
    population = [kid[1] for kid in offspring[:len(population)]]
    return population


""" this function simulates Darwin's evolution
    using basic ideas of evolutionary biology """
def evolution(population, X_in, Y, number_of_generations, children):
    for i in range(number_of_generations):
        offspring = []
        for genom in population:
            for j in range(children):
                child = mutation(genom)
                child_loss = mean_square_error(X, Y, child)
                offspring.append([child_loss, child])
            population = selection(offspring, population)
            print(offspring[0][0])
            plot_result(X_in, Y, population[0])
    return population

# run our program
population = generate_population(3, 1)
population = evolution(population, X, Y, 100, 3)
