import random
import datetime

geneSet = [0,1,2,3,4]
target = [0,1,4,3,2,3,1,2,0,4,0,3,4,1,2,2,0,3,4,1,2,1,3,4,0]

def generate_parent(length):
    genes = []
    while len(genes) < length:#passar 25
        sampleSize = min(length - len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, sampleSize))
    return genes

def get_fitness(guess):
    return sum(1 for expected, actual in zip(target, guess)
                if expected == actual)

def mutate(parent):
    index = random.randrange(0, len(parent))
    childGenes = list(parent)
    newGene, alternate = random.sample(geneSet, 2)
    childGenes[index] = alternate \
        if newGene == childGenes[index] \
        else newGene
    return childGenes

def display(guess):
    timeDiff = datetime.datetime.now() - startTime
    fitness = get_fitness(guess)
    print("{0}\t{1}\t{2}".format(guess, fitness, str(timeDiff)))

def main():
    random.seed()
    global startTime
    startTime = datetime.datetime.now()
    bestParent = generate_parent(len(target))
    bestFitness = get_fitness(bestParent)
    display(bestParent)
    while True:
        child = mutate(bestParent)
        childFitness = get_fitness(child)
        if bestFitness >= childFitness:
            continue
        display(child)
        if childFitness >= len(bestParent):
            break
        bestFitness = childFitness
        bestParent = child

if __name__ == '__main__':
    main()