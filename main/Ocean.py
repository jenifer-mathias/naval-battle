class Ocean:
    OCEAN_VALUE = 'água'

    def makeOcean(self):
        return [[Ocean.OCEAN_VALUE for i in range(10)] for j in range(10)]
