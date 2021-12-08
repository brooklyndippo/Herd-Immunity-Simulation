# Simulation Questions & Answers

1. What were the inputs you gave the simulation? (Population size, percent vaccinated, virus name, mortality rate,  reproductive rate)

    The inputs I gave my simulation were:
    
    Virus Data:
        Virus Name
        Reproduction Rate (what percentage of people exposed contract the virus)
        Mortality Rate (what percentage of infected people die from the virus)
    
    Population Data:
        Population Size
        Vaccination Rate
        Initial Infected (how many people have the infection at the start of the simulation)
        Average Interactions (how many people the infected people exposed to the virus)

2. What percentage of the population became infected at some point before the virus burned out?

    In most of my simulations, herd immunity was achieved when around 85% of the population was immune. Herd immunity is a percentage we can calculate based on the reproduction rate, mortality rate, and vaccination rate of the population. That number can vary depending on the parameters of the virus, so my code is designed to be flexible and take these parameters into account when calculating it. 

3.  What percentage of the population died from the virus?

    Again, this depends entirely on the virus, particularly the reproduction rate, mortality rate, and the vaccination rate of the population. In highly vaccinated populations very few people died. But against diseases that don't have proven vaccines (such as Ebola)  you will see very high rates of death before the virus dies out or immunity is achieved. 

    One of the limitations of this model is that it doesn't take into account social distancing, masking, or quarantine for healthy or infected individuals. Presumably when a highly contagious, highly deadly virus enters a population we immediately reduce our interactions to limit risks, which could result in the virus burning out well before herd immunity is achieved or the death toll climbs. 

4.  Out of all interactions sick individuals had during the entire simulation, how many total interactions did we see where a vaccination saved a person from potentially becoming infected?

    This simulation assumes 100% vaccine efficacy so the number of interactions where a vaccination saved a person from infection was equal to the vaccination rate of the population. Even when a vaccine has lower efficacy, the protection is still compounding. The virus would have to overcome the barrier of it's likelihood to infect anyone (the reproduction rate) and the efficacy of the vaccine before it would result in an infection. Those are much better odds than chance.