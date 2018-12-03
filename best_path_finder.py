#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 04:00:37 2018

@author: jcarraascootarola

this is not meant to work properly but to show that some problems my need to adjust the genetic algorithm. 
In this case the regular implementation of the GA's mutation and crossover does not account for no repeated genes.
"""
from random import randint
from GeneticAlgorithm import GeneticAlgorithm
import time
import matplotlib.pyplot as plt
import math




#hiperparameters
mutationRate = 0.10
populationSize = 40
numberOfGenes = 5

#stopCondition Parameters
maxGenerations=100

#problem parameters
xSize=100
ySize=100

points = []
geneValues=[]

def generatePoints():
    for i in range(numberOfGenes):
        points.append([randint(0,ySize),randint(0,xSize)])
        geneValues.append(i)
        
        
def fitnessFunction(individual):
    traveledDistance = 0
    for i in range(len(individual)-1):
        traveledDistance+=distance(points[individual[i]],points[i+1])
            
    return 1/(traveledDistance+1)
    
def distance(pointA,pointB):
    return math.sqrt((pointA[0]+pointB[0])**2 + (pointA[1]+pointB[1])**2 )
    
    
def stopCondition(algorithmInstance):          

    if algorithmInstance.numberOfGenerations == maxGenerations:
        return True
    return False

generatePoints ()

print("Entrenando, esto puede tomar un tiempo ...")
start = time.time()
ga = GeneticAlgorithm(mutationRate, populationSize, fitnessFunction, numberOfGenes, geneValues, stopCondition)
ga.startAlgorithm()
end = time.time()
print("time elapsed: "+str(end - start))
plt.figure(1) 
plt.plot(ga.generation, ga.bestFitness)
plt.xlabel('Generation')
plt.ylabel('Fittest individual fitness')
plt.title("Best individual performance")

plt.figure(2) 
plt.plot(ga.generation, ga.averageFitness)
plt.xlabel('Generation')
plt.ylabel('Population average fitness')
plt.title("Average generation performance")
plt.show()