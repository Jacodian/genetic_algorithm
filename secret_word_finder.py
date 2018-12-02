#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: jcarraascootarola
"""

from GeneticAlgorithm import GeneticAlgorithm
import time
import matplotlib.pyplot as plt


wordToGuess="paralelepipedo"

#hiperparameters
mutationRate = 0.05
populationSize = 40
numberOfGenes = len(wordToGuess)

#stopCondition Parameters
maxGenerations=100


geneValues=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]

def fitnessFunction(individual):
    total=0
    for i in range(len(individual)):
        if wordToGuess[i]==individual[i]:
            total+=1
    return total
    

def stopCondition(algorithmInstance):          

    if algorithmInstance.numberOfGenerations == maxGenerations or fitnessFunction(algorithmInstance.best) == numberOfGenes:
        return True
    return False
    

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


    