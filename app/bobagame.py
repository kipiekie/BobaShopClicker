"""
Basic logic for game
"""

class BobaGame:
    def __init__(self):
        """
        """
        self.basicButtonCounter = 0

    def increment(self):
        self.basicButtonCounter += 1
        return self.basicButtonCounter
    
    def get_count(self):
        return self.basicButtonCounter
    
# Creating game instance
game = BobaGame()