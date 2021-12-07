import random, sys
from person import Person
from logger import Logger
from virus import Virus

class Simulation(object):

    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1, average_interactions=100):
    
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
        # AVG INTERACTIONS (integer)
        self.average_interactions = average_interactions


        '''Initialize the logger'''
        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(
            virus.virus_name, pop_size, vacc_percentage, initial_infected)
        logger = Logger(self.file_name) 
        self.logger = logger
        logger.write_metadata(self.virus.virus_name, self.virus.repro_rate, self.virus.mortality_rate, self.pop_size, self.vacc_percentage, self.initial_infected)

        '''Population statistics'''
        self.population = [] # List of Person objects
        self.next_person_id = 0 # Int
        self.current_infected = [] # Int
        self.total_infected = 0 # Int
        self.total_immune = 0 #people who are vaccinated or naturally immune
        self.newly_dead = 0
        self.total_dead = 0 # Int

        '''Calculate herd immunity'''
        self.herd_immunity = 1 - 1/(10*self.virus.repro_rate/(1 - self.virus.mortality_rate)) 
        self.conclusion = None #log the conclusion of the simulation

        #add people here as infected
        self.newly_infected = []

        #build the population
        self._create_population()
        for person in self.current_infected:
            print(f'infected person: {person._id}')

    def _create_population(self):
        person_id = 1
        while person_id < (self.pop_size + 1) :
            while person_id < (self.initial_infected + 1):
                person = Person(person_id, False, self.virus)
                self.population.append(person)
                self.current_infected.append(person)
                self.total_infected += 1
                person_id += 1
            is_vaccinated = ((random.random() < self.vacc_percentage))
            person = Person(person_id, is_vaccinated)
            self.population.append(person)
            person_id += 1
            if person.is_vaccinated:
                self.total_immune += 1 # add vaccinated people to total immune
        return self.population

    def _simulation_should_continue(self):
        
        if self.total_immune >= (self.herd_immunity* len(self.population)):
            print('Herd Immunity has been achieved.')
            self.conclusion = 'herd immunity'
            self.logger.log_conclusion(self.conclusion, self.total_dead, len(self.population), self.total_immune)
            return False
        elif len(self.current_infected) == 0:
            print('There are no more active infections.')
            self.conclusion = 'no infections'
            self.logger.log_conclusion(self.conclusion, self.total_dead, len(self.population), self.total_immune)
            return False
        elif len(self.population) == 0:
            self.logger.log_conclusion('everyone died', self.total_dead, len(self.population), self.total_immune)
        else:
            return True


    def run(self):
        ''' Run the simulation'''
        step_num = 1
        while self._simulation_should_continue() == True:
            print(f'======TIME STEP {step_num}=======')
            self.time_step()
            self.current_infected = []
            self._infect_newly_infected()
            self.logger.log_time_step(step_num, len(self.newly_infected), self.newly_dead, self.total_infected, self.total_dead, self.total_immune, len(self.population), self.herd_immunity)
            self.newly_infected = []
            self.newly_dead = 0
            step_num += 1
            print(f'population size: {len(self.population)}')


    def time_step(self):
        print(self.current_infected)
        for person in self.current_infected:
            print(f'infected person: {person._id}')
            #every sick person should randomly interact with number of average interactions
            random_people = random.sample(self.population, self.average_interactions)
            for random_person in random_people:
                self.interaction(person, random_person)
            

    def interaction(self, person, random_person):
        print(f'{person._id} interaction with {random_person._id}')
        assert person.is_alive == True
        assert random_person.is_alive == True

        if random_person.is_vaccinated:
            self.logger.log_interaction(person, random_person)
        elif random_person.natural_immunity:
            self.logger.log_interaction(person, random_person)
        elif random_person.virus != None:
            self.logger.log_interaction(person, random_person)
        elif random_person.is_vaccinated == False and random_person.natural_immunity == False:
            bad_luck = random.random()
            if bad_luck < self.virus.repro_rate:
                #if the person is not actively infected
                if any(x._id == random_person._id for x in self.newly_infected) == False:
                    print(f'{random_person._id} caught virus')
                    self.logger.log_interaction(person, random_person, True)
                    self.total_infected += 1
                    self.newly_infected.append(random_person)
                else:
                    print('DUPLICATE CAUGHT**************')
            else:
                self.logger.log_interaction(person,random_person)




    def _infect_newly_infected(self):
        for sick_person in self.newly_infected:
            sick_person.virus = self.virus
            if sick_person.did_survive_infection():
                print(f'{sick_person._id} is actively infected.')
                self.logger.log_infection_survival(sick_person)
                self.current_infected.append(sick_person)
                self.total_immune += 1
                
            else:
                self.logger.log_infection_survival(sick_person, True)
                self.population.remove(sick_person)
                self.newly_dead += 1
                self.total_dead += 1
                print(f'{sick_person._id} died from the infection')                
