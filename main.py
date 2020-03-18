# Author: Tonia Sanzo
# Date: March 13, 2020
# Acknowlegdements: John Guttag, MIT 6.0002 Introduction to Computational Thinking and Data Science, Fall 2016
#
# Monte Carlo Simulation

from roads import Roads
import math

# Run the simulation return probability of an avalanche  
def runSimulation(numSimulations, probability):
    numSuccess = 0.0
    totSims = 0.0
    road = Roads(probability)
    for i in range (0, numSimulations):
        if road.simulate():
            numSuccess += 1.0
        totSims += 1.0
    return numSuccess / totSims

# given a list of samples and a mean, return the standard deviation
def standardDeviation(samples, mean):
    rtnVal = 0.0
    for i in range(0, len(samples)):
        rtnVal += (samples[i] - mean) * (samples[i] - mean)
    rtnVal = rtnVal / (len(samples) - 1)
    return math.sqrt(rtnVal)
if __name__ == "__main__":
    # run simulation with the number of simulations equal to 3, 100, 10K, and 1Million
    simulationsRun = [100000000]

    for i in range(1):
        mean = 0.0
        stdDev = 0.0
        samples = []

        print 'Simulate avalanches 20 trials with', simulationsRun[i], 'avalanches' 
        for j in range (0, 20):
            samples.append(100.0 * runSimulation(simulationsRun[i], .3))
            mean += samples[j]
        mean = mean / 20
        stdDev = standardDeviation(samples, mean)
        print 'LB:', mean - stdDev * 1.96, 'mean:', mean, 'UB:', mean + stdDev * 1.96 
