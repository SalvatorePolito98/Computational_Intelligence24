from random import choices, randint,random,sample
from lab9_lib import make_problem

class EA_MIO:
    def __init__(self, genome_length, population_size, generations, mutation_rate, fitness_function):
        self.genome_length = genome_length
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.fitness_function = fitness_function
        self.population = None

    def start(self):
        #I start with a panmittic population that is a representation of population without any constraint with the neighbors
        return [choices([0, 1], k=self.genome_length) for _ in range(self.population_size)]

    def run(self):
        # Initialize population
        self.population = self.start()
        offspring = []
        best_individual = None
        parents=[]
        
        ##################################################################
        #  Strategy Used is Mutation+ recombination similar to Strategy1 #
        ##################################################################
        
        for _ in range(self.generations):
            
            fitnesses = [self.fitness_function(individual) for individual in self.population]
            lista_ordinata = sorted(self.population, key=lambda x: sum(x), reverse=True)
            ##Here we have parent selection that i did selecting the elements in the population that have a lot of 1 inside.
            parents1=lista_ordinata[0]
            parents2=lista_ordinata[1]
            parents=[parents1,parents2]
            
            #Mutation of elements of parents   
            for i in range(len(parents)):
                if i%3==0:    
                    mutation_index = randint(0, self.genome_length - 1)
                    parents[i][mutation_index] = 1 - parents[i][mutation_index]
                     
            # Crossover (One cut crossover strategy or multi point crossover -> there are two different points but i decided to to multi point)
            while len(offspring) < self.population_size:
                parent1, parent2 = choices(parents, k=2)
                crossover_index = randint(1, self.genome_length - 1)
                crossover_index_list = [randint(1, self.genome_length-1) for _ in range(7)]
                crossover_index_list_ordinata = sorted(crossover_index_list)
                for i in range(len(crossover_index_list_ordinata)-1):
                    if random() < self.mutation_rate:
                        child = parent1[:crossover_index_list_ordinata[i]] + parent2[crossover_index_list_ordinata[i]:crossover_index_list_ordinata[i+1]] + parent1[crossover_index_list_ordinata[1+1]:]   
                    else:
                        child = parent2[:crossover_index_list_ordinata[i]] + parent1[crossover_index_list_ordinata[i]:crossover_index_list_ordinata[i+1]] + parent2[crossover_index_list_ordinata[1+1]:]
                offspring.append(child)
            self.population = offspring
        best_individual = max(self.population, key=self.fitness_function)

        # Print the best individual and its fitness value and the total number of fitness call
        print(f"Best Individual: {''.join(str(g) for g in best_individual)}")
        print(f"Fitness: {self.fitness_function(best_individual):.1%}")
        print(f"Total Fitness Calls: {self.fitness_function.calls}")
        
fitness_problem = make_problem(10)
fitness_problem1 = make_problem(5)
fitness_problem2 = make_problem(2)
fitness_problem3 = make_problem(1)

# Create EA instance and run
print("ISTANCE #10")
ea = EA_MIO(genome_length=1000, population_size=100, generations=100, mutation_rate=0.3, fitness_function=fitness_problem)
ea.run()

# Create EA instance and run
print("\nISTANCE #5")
ea1 = EA_MIO(genome_length=1000, population_size=100, generations=100, mutation_rate=0.3, fitness_function=fitness_problem1)
ea1.run()

# Create EA instance and run
print("\nISTANCE #2")
ea2 = EA_MIO(genome_length=1000, population_size=100, generations=100, mutation_rate=0.3, fitness_function=fitness_problem2)
ea2.run()

# Create EA instance and run
print("\nISTANCE #1")
ea3 = EA_MIO(genome_length=1000, population_size=100, generations=100, mutation_rate=0.3, fitness_function=fitness_problem3)
ea3.run()
