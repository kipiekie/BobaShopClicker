"""
Basic logic for game
"""

class BobaGame:
    def __init__(self):
        self.basicButtonCounter = 0

        self.buttonUpgrades = {
            "ten": False
        }

    def increment(self):
        if self.buttonUpgrades["ten"]:
            self.basicButtonCounter += 10
        else:
            self.basicButtonCounter += 1
        return self.basicButtonCounter
    
    def get_count(self):
        return self.basicButtonCounter
    
    def basicButtonUpgrade(self):
        if self.buttonUpgrades["ten"] == False and self.basicButtonCounter >= 10:
            self.buttonUpgrades["ten"] = True
            self.basicButtonCounter -= 10
            return True
        return False

    
# Creating game instance
game = BobaGame()