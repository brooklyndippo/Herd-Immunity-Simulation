import random
from virus import Virus


class Person(object):
    ''' Person objects will populate the simulation. '''

    def __init__(self, _id, is_vaccinated, virus=None):
 
        self._id = _id  # int
        self.is_alive = True  # boolean
        self.natural_immunity = False # boolean (recovered, but not vaccinated)
        self.is_vaccinated = is_vaccinated  # boolean
        self.virus = virus  # Virus object

    def did_survive_infection(self):
        if self.virus: 
            random_mortality = random.randint(0,1)
            if random_mortality <= self.virus.mortality_rate:
                print(f'{self._id} died')
                self.is_alive = False
                return False
            else:
                self.natural_immunity = True
                self.virus = None
                return True
        

''' These are simple tests to ensure that you are instantiating your Person class correctly. '''
def test_vacc_person_instantiation():
    # create some people to test if our init method works as expected
    person = Person(1, True)
    assert person._id == 1
    assert person.is_alive is True
    assert person.is_vaccinated is True
    assert person.virus is None


def test_not_vacc_person_instantiation():
    person = Person(2, False)
    assert person._id == 2
    assert person.is_alive is True
    assert person.is_vaccinated is False
    assert person.virus is None


def test_sick_person_instantiation():
    virus = Virus("Dysentery", 0.7, 0.2)
    person = Person(3, False, virus)

    assert person._id == 3
    assert person.is_alive is True
    assert person.is_vaccinated is False
    assert person.virus is virus


def test_did_survive_infection():
    virus = Virus("Dysentery", 0.7, 0.2)
    person = Person(4, False, virus)
    
    assert person._id == 4
    assert person.is_alive is True
    assert person.is_vaccinated is False
    assert person.virus is virus

    # Resolve whether the Person survives the infection or not
    survived = person.did_survive_infection()
    
    if survived:
        assert person.is_alive is True
        assert person.natural_immunity is True

    else:
        assert person.is_alive is False