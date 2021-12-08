from simulation import Simulation
from virus import Virus
from validate_input import validate_input

print('\n\nWelcome to the Herd Immunity Simulator!')
print('- - - - - - - - - - - - - - - - - - - - - - -  - - - - - - -')
print('You will be prompted for data to run a simulation.')
print('Please enter all rates/percentages as a number between 1-100.')
print('After running the simulation, you can access macrodata \nand microdata in the output files.')
print('- - - - - - - - - - - - - - - - - - - - - - -  - - - - - - -')
print('🦠 🦠 🦠 🦠 🦠 🦠 🦠 🦠 🦠 🦠 🦠 🦠 🦠 🦠 🦠 🦠 🦠 🦠 🦠 🦠 🦠\n')

virus_name = validate_input('What is the virus name?  ', str)
repro_rate = validate_input('What is the reproduction rate?  ')/100
mortality_rate = validate_input('What is the mortality rate?  ')/100

virus = Virus(virus_name, repro_rate, mortality_rate)

population_size = validate_input('What is the population size?  ')
vacc_percentage = validate_input('What percentage of the population is vaccinated?  ')/100
initial_infected = validate_input('How many people are initially infected?  ')
average_interactions = validate_input('How many interactions should each infected person have?  ')

sim = Simulation (virus, population_size, vacc_percentage, initial_infected, average_interactions)


sim.run()
