from datetime import time
from functools import partial
from random import random, randint

from tiling import Shape,Canvas
from typing import List,Callable,Tuple
Genome = Canvas
Population = List[Canvas]
FitnessFunc = Callable[[Genome],int]
PopulateFunc = Callable[[], Population]
SelectionFunc = Callable[[Population, FitnessFunc], Tuple[Genome, Genome]]
CrossOverFunc = Callable[[Genome, Genome], Tuple[Genome, Genome]]
MutationFunc = Callable[[Genome], Genome]

# 10] Create a program that finds each and every (unique) way to fill a Canvas (with or without black cells)
# with the maximum number of Shapes given (with or without rotation and flipping allowed).
def generate_genome(c:Canvas) -> Genome:
    # TODO what params do we get? the characteristics that we want as starting points
    pass

def generate_population(size: int, genome_length: int) -> Population:
    # TODO
    pass

def mutation(genome: Genome, num: int = 1, probability: float = 0.5) -> Genome:
    # TODO
    pass

def population_fitness(population: Population, fitness_func: FitnessFunc) -> int:
    return sum([fitness_func(genome) for genome in population])

def selection_pair(population: Population, fitness_func: FitnessFunc) -> Population:
    # TODO
    pass


def sort_population(population: Population, fitness_func: FitnessFunc) -> Population:
    return sorted(population, key=fitness_func, reverse=True)

def genome_to_string(genome: Genome) -> str:
    return "".join(map(str, genome))


def single_point_crossover(a: Genome, b: Genome) -> Tuple[Genome, Genome]:
    if len(a) != len(b):
        raise ValueError("Genomes a and b must be of same length")
    length = len(a)
    if length < 2:
        return a, b
    p = randint(1, length - 1)
    return a[0:p] + b[p:], b[0:p] + a[p:]

def run_evolution(
    populate_func: PopulateFunc,
    fitness_func: FitnessFunc,
    fitness_limit: int,
    selection_func: SelectionFunc = selection_pair,
    crossover_func: CrossOverFunc = single_point_crossover,
    mutation_func: MutationFunc = mutation,
    generation_limit: int = 100
) -> Tuple[Population, int]:
    population = populate_func()

    for i in range(generation_limit):
        population = sorted(
            population,
            key=lambda genome: fitness_func(genome),
            reverse=True
        )

        if fitness_func(population[0]) >= fitness_limit:
            break

        next_generation = population[0:2]

        for j in range(int(len(population) / 2) - 1):
            parents = selection_func(population, fitness_func)
            offspring_a, offspring_b = crossover_func(parents[0], parents[1])
            offspring_a = mutation_func(offspring_a)
            offspring_b = mutation_func(offspring_b)
            next_generation += [offspring_a, offspring_b]

        population = next_generation

    population = sorted(
        population,
        key=lambda genome: fitness_func(genome),
        reverse=True
    )

    return population, i

start_time = time.time()
populations, generations = run_evolution(
    populate_func=partial(
        generate_population,
        size=10,
        genome_length=10 # edw 8a xreiastein a mpei to size apo to thing poy 8a exoume
    ),
    fitness_func=partial(
        population_fitness,
        target="Hello, World!" # edw prepei na mpei weight kai thing
    ),
    fitness_limit=13,
    generation_limit=100
)
end_time = time.time()

print(f"number of generations: {generations}")
print(f"time: {end_time - start_time}s")
print(f"result: {genome_to_string(populations[0])}")