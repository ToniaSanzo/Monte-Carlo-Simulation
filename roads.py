# Author: Tonia Sanzo
# Date: March 13, 2020
# Acknowlegdements: John Guttag, MIT 6.0002 Introduction to Computational Thinking and Data Science, Fall 2016
#
# Monte Carlo Simulation
import random

class Roads():
    # Instance Variables
    avalanche = [False, False, False, False, False]
    probability = 0.0

    # Constructor, with the probability of an avalanche giving
    def __init__(self, probability):
        self.probability = probability

    # Run simulation, return true if town's are still reachable
    def simulate(self):
        rtnBool = True
        for i in range (0, 5):
            if random.random() <= self.probability:
                self.avalanche[i] = True 
        # Every condition that would result in not being able to be reached 
        if (self.avalanche[0] and self.avalanche[1]) or (self.avalanche[3] and self.avalanche[4]) or (self.avalanche[3] and self.avalanche[2] and self.avalanche[1]) or (self.avalanche[4] and self.avalanche[2] and self.avalanche[0]):
            rtnBool = False
        self.reset()
        return rtnBool

    # Reset avalanche list
    def reset(self):
        for i in range(0, 5):
            self.avalanche[i] = False;
