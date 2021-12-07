# Herd Immunity Simulation

Infectious diseases are all around us and our best tool for fighting back is herd immunity. Herd immunity is easiest to achieve through vaccination, but it can also be achieved through a combination of vaccines and natural immunity.
## How the simulator works:

To run the simulator, open the project and move to the directory, then call the following command: 

  python3 start_simulation.py

This will start the simulation and prompt you to input some information about the virus and population that you are modeling. You can input information as a whole number percentage (any integer between 1-100) and the program will automatically convert it to a decimal for calculations.

## Output:

After you run the simulation, you will see two new files appear in your folder. The file populated with the disease name is the MASTER FILE. 

This file includes the metadata about the virus and population, as well as a snapshot of each time step that was run before herd immunity was achieved, the infection died out, or the population died.

How the simulation ends can tell you a lot about the disease:
* Herd Immunity Achieved - this usually happens through a combination of vaccination and natural immunity, which we obtain when we survive a virus. For viruses that are highly contagious but not as deadly, we're likely to achieve herd immunity.
* No More Active Infections - if you have no more active infections, that could mean that a virus has a very low reproductive rate (low contagiousness) and it didn't spread well or it can mean that it has a high mortality rate (very deadly) in which case the carrier usually dies before being able to spread it to the rest of the population.
* Population Died - this is an incredibly unlikely scenario, but one that was considered when building this model. Ultimately, we would only expect this to happen in a very small population with a highly contagious disease with long incubation/contagiousness period a high mortality rate.



  