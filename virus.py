class Virus(object):
    '''Properties and attributes of the virus used in Simulation.'''

    def __init__(self, virus_name, repro_rate, mortality_rate):
        self.virus_name = virus_name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate




'''TESTING '''
def test_virus_instantiation():
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.name == "HIV"
    assert virus.repro_rate == 0.8
    assert virus.mortality_rate == 0.3

def test_virus_instantiation():
    virus = Virus("Mumps", 0.4, 0.5)
    assert virus.name == "Mumps"
    assert virus.repro_rate == 0.4
    assert virus.mortality_rate == 0.5

def test_virus_instantiation():
    virus = Virus("Chickenpox", 0.95, 0.03)
    assert virus.name == "Chickenpox"
    assert virus.repro_rate == 0.95
    assert virus.mortality_rate == 0.03