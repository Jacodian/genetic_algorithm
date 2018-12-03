#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: jcarraascootarola
"""


from random import randint
from random import random
from statistics import mean 



class GeneticAlgorithm:

    population =[]
    popFitness =[]
    bestFitness = []
    averageFitness = []
    generation = []
    best = None
    numberOfGenerations = 0
    
    def __init__(self,mutationRate, populationSize, fitnessFunction, numberOfGenes, geneValues, stopCondition):
        self.mutationRate = mutationRate
        self.populationSize = populationSize
        self.fitnessFunction = fitnessFunction
        self.numberOfGenes = numberOfGenes
        self.geneValues = geneValues
        self.stopCondition = stopCondition
        #k is the tournament selection size
        self.k = populationSize//2

        
    def startAlgorithm(self):
        self.popCreation()
        while True:
            self.generation.append(self.numberOfGenerations)
            self.evaluateFitness()
            self.bestFitness.append(max(self.popFitness))
            
            if self.best == None or self.bestFitness[-1] > self.fitnessFunction(self.best):
                self.best = self.population[self.popFitness.index(max(self.popFitness))]
            
            if self.stopCondition(self):
                break
            self.reproduction()
            self.numberOfGenerations+=1
            
    def popCreation(self):
        for i in range(self.populationSize):
            self.population.append(self.individualCreation())
    
    def individualCreation(self):
        individual=[]
        for i in range(self.numberOfGenes):
            individual.append(self.geneValues[randint(0,len(self.geneValues)-1)])
        return individual
            
    def evaluateFitness(self):
        self.popFitness = []
        for i in range(self.populationSize):
            self.popFitness.append(self.fitnessFunction(self.population[i]))
        self.averageFitness.append(mean(self.popFitness))
            
    def selection(self):
        best = None
        bestIndex = 0
        for i in range(self.k):
            index = randint(0, self.populationSize-1)
            if best == None or self.popFitness[index] > self.popFitness[bestIndex]:
                best = self.population[index]
                bestIndex = index
        return best
    
    def reproduction(self):
        newPopulation = []
        for i in range(self.populationSize):
            parent1 = self.selection()
            parent2 = self.selection()
            baby = self.crossOver(parent1,parent2)
            baby = self.mutate(baby)
            newPopulation.append(baby)
        self.population = newPopulation
            
    def crossOver(self,parent1 ,parent2):
        mixingPoint = randint(0, len(parent1)-2)
        baby =[]
        for i in range(mixingPoint):
            baby.append(parent1[i])
        for i in range(mixingPoint,len(parent1)):
            baby.append(parent2[i])

        return baby
        
    def mutate(self,individual):
        mutatedIndividual=individual
        for i in range(len(individual)):
            if random() < self.mutationRate:
                mutatedIndividual[i] = self.geneValues[randint(0,len(self.geneValues)-1)]
        return mutatedIndividual
            
      
    
            
            
            
            
        
        
        