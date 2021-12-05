import random, sys
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
    ''' Main class that will run the herd immunity simulation program.
    Expects initialization parameters passed as command line arguments when file is run.

    Simulates the spread of a virus through a given population.  The percentage of the
    population that are vaccinated, the size of the population, and the amount of initially
    infected people in a population are all variables that can be set when the program is run.
    '''

    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
        '''
        The next_person_id is the next available id for all created Persons,
        and should have a unique _id value.

        '''
  
        # TODO: Store each newly infected person's ID in newly_infected attribute.
        # At the end of each time step, call self._infect_newly_infected()
        # and then reset .newly_infected back to an empty list.
    
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
        self.current_infected = 0 # Int
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
                person_id += 1
            #TO-DO: Add an adjusted vaccination rate that takes out the initial infected as unvaccinated and still keeps the overall vax rate
            is_vaccinated = (random.randint(0, 1) <= self.vacc_percentage)
            person = Person(person_id, is_vaccinated)
            self.population.append(person)
            person_id += 1
        for person in self.population:
            print (person._id)
            print (person.is_vaccinated)
            print (person.virus)
        print(len(self.population))
        return self.population


    def _simulation_should_continue(self):
        if self.total_dead + self.total_immune == self.pop_size:
            return False
        else:
            return True

    def run(self):
        ''' This method should run the simulation until all requirements for ending
        the simulation are met.
        '''
        while self._simulation_should_continue():
            pass 
        # TODO: Finish this method.  To simplify the logic here, use the helper method
        # _simulation_should_continue() to tell us whether or not we should continue
        # the simulation and run at least 1 more time_step.

        # TODO: Keep track of the number of time steps that have passed.
        # HINT: You may want to call the logger's log_time_step() method at the end of each time step.
        # TODO: Set this variable using a helper
        time_step_counter = 0
        should_continue = None

        while should_continue:
            # TODO: for every iteration of this loop, call self.time_step() to compute another
            # round of this simulation.
            print(f'The simulation has ended after {time_step_counter} turns.')
            pass

    def time_step(self):
        for person in self.population:
            if person.virus != None:
                random_people = random.sample(self.population, 100)
                for random_person in random_people:
                    self.interaction(person, random_person)
        #If the person is dead, grab another random person from the population.
        #Since we don't interact with dead people, this does not count as an interaction.
            


    def interaction(self, person, random_person):
        assert person.is_alive == True
        assert random_person.is_alive == True

        if random_person.is_vaccinated:
            pass
        if random_person.virus != None:
            pass
        if random_person.virus != None and random_person.is_vaccinated == False and random_person.natural_immunity == False:
            bad_luck = random.randint(0,1)
            if bad_luck < self.virus.repro_rate:
                self.newly_infected.append(random_person)

        '''Call the logger'''
        self.logger.log_interaction()

        # TODO: Finish this method.
        #  The possible cases you'll need to cover are listed below:
            # random_person is healthy, but unvaccinated:
            #     generate a random number between 0 and 1.  If that number is smaller
            #     than repro_rate, random_person's ID should be appended to
            #     Simulation object's newly_infected array, so that their .infected
            #     attribute can be changed to True at the end of the time step.
        # TODO: Calls logger method during this method.
        pass

    def _infect_newly_infected(self):
        for sick_person in self.newly_infected:
            sick_person.virus = self.virus

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
    sim = Simulation(virus, pop_size, vacc_percentage, initial_infected)

    #stretch goal - Prompt to enter each of these attributes individually

    sim.run()

# call the function: VIRUS NAME (str), REPRODUCTION RATE (float), MORTALITY (float), POPULATION (int), VACC PERCENTAGE (float), INITIAL INFECTED (int)
# python3 simulation.py 'Covid' .3 .2 10 .2 2