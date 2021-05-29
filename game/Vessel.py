import random
import NavalBattle
import Ocean


class Vessel:
    portaAvioes = {'nome': 'Porta-aviões',
                   'comprimento': 5,
                   'sigla': 'P',
                   'quantidade': 1}

    cruzadores = {'nome': 'Cruzador',
                  'comprimento': 4,
                  'sigla': 'C',
                  'quantidade': 2}

    destroyers = {'nome': 'Destroyer',
                  'comprimento': 3,
                  'sigla': 'D', 'quantidade': 3}

    submarinos = {'nome': 'Submarino',
                  'comprimento': 2,
                  'sigla': 'S',
                  'quantidade': 3}

    def positionVessel(self, strikeGroup, ocean):
        for vessel in strikeGroup:
            for i in range(vessel.get('quantidade')):
                sortedLine, sortedColumn, direction = self.positionVesselHelper(vessel.get('comprimento'), ocean)
                if direction == 'horizontal':
                    for column in range(sortedColumn, sortedColumn + vessel.get('comprimento')):
                        ocean[sortedLine][column] = vessel.get('sigla')
                else:
                    for line in range(sortedLine, sortedLine + vessel.get('comprimento')):
                        ocean[line][sortedColumn] = vessel.get('sigla')

    def positionVesselHelper(self, sizeVessel, ocean):
        OK = False
        HORIZONTAL = 0
        VERTICAL = 1
        if random.randint(0, 1) == HORIZONTAL:
            direction = 'horizontal'
        else:
            direction = 'vertical'
        while not OK:
            sortedLine, sortedColumn = NavalBattle.generatesRandomPosition(
                (len(ocean) - 1) - sizeVessel, direction, ocean)
            if direction == 'horizontal':
                for column in range(sortedColumn, sortedColumn + sizeVessel, 1):
                    if ocean[sortedLine][column] == Ocean.OCEAN_VALUE:
                        OK = True
                    else:
                        OK = False
                    break
            else:
                for line in range(sortedLine, sortedLine + sizeVessel, 1):
                    if ocean[line][sortedColumn] == Ocean.OCEAN_VALUE:
                        OK = True
                    else:
                        OK = False
                    break
        return sortedLine, sortedColumn, direction
