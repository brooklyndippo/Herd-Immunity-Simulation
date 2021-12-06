import random, sys
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):

    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
    
        '''Variables declared to start the simulation'''
        # VIRUS (object) - includes :
        # name (str)
        # reproduction rate (float)
        # mortality rate (float))
        self.virus = virus 
        # POPULATION (integer)
        self.pop_size = pop_size
        # VACC PERCENTAGE (float)
        self.vacc_percentage = vacc_percentage
        # INITIAL INFECTED (integer)
        self.initial_infected = initial_infected 


        '''Initialize the logger'''
        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(
            virus_name, pop_size, vacc_percentage, initial_infected)
        logger = Logger(self.file_name) 
        self.logger = logger
        logger.write_metadata(self.virus.virus_name, self.virus.repro_rate, self.virus.mortality_rate, self.pop_size, self.vacc_percentage, self.initial_infected)

        '''Population statistics'''
        self.population = [] # List of Person objects
        self.next_person_id = 0 # Int
        self.current_infected = [] # Int
        self.total_infected = 0 # Int
        self.total_immune = 0 #people who are vaccinated or naturally immune
        self.total_dead = 0 # Int

        #add people here as infected
        self.newly_infected = []

        #build the population
        self._create_population()

    def _create_population(self):
        person_id = 1
        while person_id < (self.pop_size + 1) :
            while person_id < (self.initial_infected + 1):
                person = Person(person_id, False, self.virus)
                self.population.append(person)
                self.current_infected.append(person)
                self.total_infected += 1
                person_id += 1
            #TO-DO: Add an adjusted vaccination rate that takes out the initial infected as unvaccinated and still keeps the overall vax rate
            is_vaccinated = (random.randint(0, 1) <= self.vacc_percentage)
            person = Person(person_id, is_vaccinated)
            self.population.append(person)
            person_id += 1
            if person.is_vaccinated:
                self.total_immune += 1 # add vaccinated people to total immune
        return self.population


    def _simulation_should_continue(self):
        if self.total_dead + self.total_immune == self.pop_size:
            return False
        else:
            return True

    def run(self):
        ''' Run the simulation'''
        while self._simulation_should_continue():
            self.time_step()

    def time_step(self):
        for person in self.current_infected:
            print(person._id)
            random_people = random.sample(self.population, 3)
            for random_person in random_people:
                self.interaction(person, random_person)
            self.current_infected.remove(person)

        self.logger.log_time_step
            

    def interaction(self, person, random_person):
        #print('interaction')
        assert person.is_alive == True
        assert random_person.is_alive == True

        if random_person.is_vaccinated:
            self.logger.log_interaction(person, random_person)
        elif random_person.virus != None:
            self.logger.log_interaction(person, random_person)
        elif random_person.is_vaccinated == False and random_person.natural_immunity == False:
            bad_luck = random.randint(0,1)
            if bad_luck < self.virus.repro_rate:
                self.logger.log_interaction(person, random_person)
                self.total_infected += 1
                self.newly_infected.append(random_person)
                self._infect_newly_infected()
            else:
                self.logger.log_interaction(person,random_person)




    def _infect_newly_infected(self):
        for sick_person in self.newly_infected:
            sick_person.virus = self.virus
            if sick_person.did_survive_infection():
                self.logger.log_infection_survival(sick_person)
                self.current_infected.append(sick_person)
                self.total_immune += 1
                
            else:
                self.logger.log_infection_survival(sick_person, True)
                self.population.remove(sick_person)
                self.total_dead += 1
                print(f'total dead: {self.total_dead}')
                
            

        self.newly_infected = []


if __name__ == "__main__":
    params = sys.argv[1:]

    #virus arguments
    virus_name = str(params[0])
    repro_rate = float(params[1])
    mortality_rate = float(params[2])

    #population arguments
    pop_size = int(params[3])
    vacc_percentage = float(params[4])

    if len(params) == 6:
        initial_infected = int(params[5])
    else:
        initial_infected = 1

    virus = Virus(virus_name, repro_rate, mortality_rate)

    print(virus.virus_name)

    sim = Simulation(virus, pop_size, vacc_percentage, initial_infected)

    #stretch goal - Prompt to enter each of these attributes individually

    sim.run()

# call the function: VIRUS NAME (str), REPRODUCTION RATE (float), MORTALITY (float), POPULATION (int), VACC PERCENTAGE (float), INITIAL INFECTED (int)
# python3 simulation.py 'Covid' .3 .2 40 .2 5