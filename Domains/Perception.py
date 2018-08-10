import Stimuli.Speech as sp
import Domains.AbstractDomain as abd


class Perception:
    abstract_domain = None
    stimuli = None
    speech = None
    change = None

    def __init__(self, speech):
        self.speech = speech
        self.abstract_domain = abd.AbstractDomain()

    def calculate(self):
        self.change = 0
        self.calculate_conducive_to_goal()
        self.calculate_discrepancy_from_expectation()
        self.calculate_familiarity()
        self.calculate_suddenness()
        self.calculate_urgency()
        self.calculate_valence()
        self.calculate_predictability()

    def calculate_conducive_to_goal(self):
        value = (2 * (.5 - abs(self.speech.intensity)) + self.speech.fluency + 2 * (.5 - abs(self.speech.duration)) +
                 self.speech.pitch_range * -1 + 2 * (.5 - abs(self.speech.volume)) + 2 * (.5 - abs(self.speech.rate)) +
                 self.speech.pitch_variance*-1) / 7
        self.change = abs(self.abstract_domain.conduciveToGoal - value)
        self.abstract_domain.conduciveToGoal = value

    def calculate_discrepancy_from_expectation(self):
        value = (self.speech.fluency*-1 + -2*(.5 - abs(self.speech.pitch_range)) + -2*(.5 - abs(self.speech.volume)) +
                 -2*(.5 - abs(self.speech.rate)) + -2*(.5 - abs(self.speech.pitch_variance))) / 5
        self.change = abs(self.abstract_domain.conduciveToGoal - value)
        self.abstract_domain.discrepancy_from_expectation = value

    def calculate_familiarity(self):
        value = (2*(.5 - abs(self.speech.intensity)) + 2*(.5 - abs(self.speech.fluency)) +
                 2*(.5 - abs(self.speech.duration)) + self.speech.pitch_range*-1 + 2 * (.5 - abs(self.speech.volume)) +
                 2*(.5 - abs(self.speech.rate)) + -1*self.speech.pitch_variance) / 7
        self.change = abs(self.abstract_domain.conduciveToGoal - value)
        self.abstract_domain.familiarity = value

    def calculate_predictability(self):
        self.change = self.change/6
        value = 2*(.5 - abs(self.change))
        self.abstract_domain.predictability = value

    def calculate_suddenness(self):
        value = (self.speech.intensity + -1*self.speech.fluency + -1*self.speech.duration + self.speech.pitch_range +
                 self.speech.volume + self.speech.pitch_variance) / 6
        self.change = abs(self.abstract_domain.conduciveToGoal - value)
        self.abstract_domain.suddenness = value

    def calculate_valence(self):
        value = (self.speech.intensity + self.speech.pitch_range + self.speech.volume + self.speech.rate +
                 self.speech.pitch_variance) / 5
        self.change = abs(self.abstract_domain.conduciveToGoal - value)
        self.abstract_domain.valence = value

    def calculate_urgency(self):
        value = (self.speech.intensity + self.speech.fluency*-1 + self.speech.duration*-1 + self.speech.pitch_range +
                 self.speech.volume + self.speech.rate + self.speech.pitch_variance) / 7
        self.change = abs(self.abstract_domain.conduciveToGoal - value)
        self.abstract_domain.urgency = value

