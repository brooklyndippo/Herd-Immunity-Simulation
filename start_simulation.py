from simulation import Simulation
from virus import Virus
from validate_input import validate_input

virus_name = validate_input('What is the virus name?  ', str)
repro_rate = validate_input('What is the reproduction rate?  ')/100
mortality_rate = validate_input('What is the mortality rate?  ')/100

virus = Virus(virus_name, repro_rate, mortality_rate)

population_size = validate_input('What is the population size?  ')
vacc_percentage = validate_input('What percentage of the population is vaccinated?  ')/100
initial_infected = validate_input('How many people are initially infected?  ')
average_interactions = validate_input('What are the average number of interactions each person should have?  ')

sim = Simulation (virus, population_size, vacc_percentage, initial_infected, average_interactions)


sim.run()
