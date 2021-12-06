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

        repro_rate = repro_rate * 100
        mortality_rate = mortality_rate * 100
        vacc_percentage = vacc_percentage * 100

        
        file = open(self.file, 'a')
        file.write('HERD IMMUNITY SIMULATION\n\n\n')

        # write virus statistics
        file.write('----- VIRUS STATS -----\n')
        file.write(f'Virus: {virus_name}\n')
        file.write(f'Reproduction Rate: {repro_rate}%\n')
        file.write(f'Mortality Rate: {mortality_rate}%\n')
        
        # write population statistics
        file.write('\n--- POPULATION STATS ---\n')
        file.write(f'Population: {pop_size}\n')
        file.write(f'Vaccination Rate: {vacc_percentage}%\n')
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
            file.write(f'{person._id} has infected {random_person._id}.\n')

        file.close()


    def log_infection_survival(self, person, did_die_from_infection=False):
        file = open(self.file, 'a')
        file.write('\n')
        file.write('     INFECTION OUTCOME:\n')
        if did_die_from_infection:
            file.write(f'     {person._id} did not survive the infection.\n')
        else:
            file.write(f'     {person._id} survived and has natural immunity now.\n')

        file.close()

    def log_time_step(self, time_step):

        next_time_step = time_step + 1
        
        file = open(self.file, 'a')
        file.write(f'Time step {time_step} ended, beginning {next_time_step}\n')
        file.close()
        return next_time_step
        
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


''' These are simple tests to ensure that you are instantiating your Logger class correctly. '''
def test_logger_instantiation():
    # create some people to test if our init method works as expected
    logger = Logger('herd_immunity_simulation')
    assert logger.file_name == 'herd_immunity_simulation'
    assert logger.file == 'herd_immunity_simulation.txt'
