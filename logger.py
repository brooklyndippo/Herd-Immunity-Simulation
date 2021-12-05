class Logger(object):
    ''' Utility class responsible for logging all interactions during the simulation. '''
    # TODO: Write a test suite for this class to make sure each method is working
    # as expected.

    # PROTIP: Write your tests before you solve each function, that way you can
    # test them one by one as you write your class.

    def __init__(self, file_name):
        self.file_name = file_name
        self.file = f'{self.file_name}.txt'

    def write_metadata(self, virus_name, repro_rate, mortality_rate, pop_size, vacc_percentage, initial_infected):

        file = open(self.file, 'a')
        file.write('HERD IMMUNITY SIMULATION\n\n\n')

        # write virus statistics
        file.write('----- VIRUS STATS -----\n')
        file.write(f'Virus: {virus_name}\n')
        file.write(f'Reproduction Rate: {repro_rate}\n')
        file.write(f'Mortality Rate: {mortality_rate}\n')
        
        # write population statistics
        file.write('--- POPULATION STATS ---\n')
        file.write(f'Population: {pop_size}\n')
        file.write(f'Vaccination Rate: {vacc_percentage}\n')
        file.write(f'Initial Infections: {initial_infected}\n')

        file.close()
        
 
        

    def log_interaction(self, person, random_person, random_person_sick=None,
                        random_person_vacc=None, did_infect=None):
        
        
        file = open(self.file, 'a')
        file.write('\n\n')
        file.write('*** INTERACTION ***\n')
        
        if random_person.virus != None: 
            file.write(f'{person._id} did not infect {random_person._id} because they are already sick.\n')
        elif random_person.natural_immunity: 
            file.write(f'{person._id} did not infect {random_person._id} because they are naturally immune.\n')
        elif random_person.is_vaccinated:
            file.write(f'{person._id} did not infect {random_person._id} because they are vaccinated.\n')
        else: 
            file.write(f'{person._id} has infected {random_person._id}\n')

        file.close()


    def log_infection_survival(self, person, did_die_from_infection):
        ''' The Simulation object uses this method to log the results of every
        call of a Person object's .resolve_infection() method.

        The format of the log should be:
            "{person.ID} died from infection\n" or "{person.ID} survived infection.\n"
        '''
        # TODO: Finish this method. If the person survives, did_die_from_infection
        # should be False.  Otherwise, did_die_from_infection should be True.
        # Append the results of the infection to the logfile
        pass

    def log_time_step(self, time_step_number):
        ''' STRETCH CHALLENGE DETAILS:

        If you choose to extend this method, the format of the summary statistics logged
        are up to you.

        At minimum, it should contain:
            The number of people that were infected during this specific time step.
            The number of people that died on this specific time step.
            The total number of people infected in the population, including the newly infected
            The total number of dead, including those that died during this time step.

        The format of this log should be:
            "Time step {time_step_number} ended, beginning {time_step_number + 1}\n"
        '''
        # TODO: Finish this method. This method should log when a time step ends, and a
        # new one begins.
        # NOTE: Here is an opportunity for a stretch challenge!
        pass


''' These are simple tests to ensure that you are instantiating your Person class correctly. '''
def test_logger_instantiation():
    # create some people to test if our init method works as expected
    logger = Logger('herd_immunity_simulation')
    assert logger.file_name == 'herd_immunity_simulation'
    assert logger.file == 'herd_immunity_simulation.txt'
