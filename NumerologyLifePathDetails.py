###Harold Stevens
###Code Classes and Numerology with Inheritance
###11/30/2024

# NumerologyLifePathDetails.py

from Numerology import Numerology  # Importing the original Numerology class

class NumerologyLifePathDetails(Numerology):
    def __init__(self, name, date_of_birth):
        # Call the parent class constructor
        super().__init__(name, date_of_birth)

    # Rewriting all getters as properties using decorators
    @property
    def Name(self):
        return self.getName()

    @property
    def Birthdate(self):
        return self.getBirthdate()

    @property
    def Attitude(self):
        return self.getAttitude()

    @property
    def BirthDay(self):
        return self.getBirthDay()

    @property
    def LifePath(self):
        return self.getLifePath()

    @property
    def Personality(self):
        return self.getPersonality()

    @property
    def PowerName(self):
        return self.getPowerName()

    @property
    def Soul(self):
        return self.getSoul()

    @property
    def LifePathDescription(self):
        # Using a dictionary instead of if/elif/else for LifePathDescription
        descriptions = {
            1: "The Independent: Wants to work/think for themselves",
            2: "The Mediator: Avoids conflict and wants love and harmony",
            3: "The Performer: Likes music, art and to perform or get attention",
            4: "The Teacher/Truth Seeker: Is meant to be a teacher or mentor and is truthful",
            5: "The Adventurer: Likes to travel and meet others, often a extrovert",
            6: "The Inner Child: Is meant to be a parent and/or one that is young at heart",
            7: "The Naturalist: Enjoy nature and water and alternative life paths, open to spirituality",
            8: "The Executive: Gravitates to money and power",
            9: "The Humanitarian: Helps others and/or experiences pain and learns the hard way"
        }
        return descriptions.get(self.LifePath, "Unknown Life Path")
