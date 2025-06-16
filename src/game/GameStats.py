
class GameStats:
    # Stats only for gameplay levels, should not be updated on test levels

    def __init__(self):
        # First index is for total value, rest for values for each level
        self.times = [0 for _ in range(7)]
        self.deaths = [0 for _ in range(7)]


    def calculateTotal(self):
        timeTotal = 0
        for time in self.times:
            timeTotal += time

        self.times[0] = timeTotal

        deathsTotal = 0
        for deaths in self.deaths:
            deathsTotal += deaths

        self.deaths[0] = deathsTotal

