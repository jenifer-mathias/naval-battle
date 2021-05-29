import random

import Players
import Utils


class NavalBattle:

    def generatesRandomPosition(self, direction, ocean):
        if direction == 'horizontal':
            return random.randint(0, len(ocean) - 1), random.randint(0, self)
        else:
            return random.randint(0, self), random.randint(0, len(ocean) - 1)

    def showBattleLattice(self):
        Utils.clearScreen(self)
        for line in range(len(self)):
            for column in range(len(self[line])):
                if column == 9:
                    print(self[line][column])
                else:
                    print(self[line][column], end=' ')

    def startGame(self, enemyOcean):
        # listOfMachineAttacks = []
        while True:
            line = int(input('Insira linha que deseja atacar: ').strip())
            column = int(input('Insira a coluna que deseja atacar: ').strip())
            # self.attacksMachine(enemyOcean,listOfMachineAttacks, 'Máquina')
            Players.attacksUser(enemyOcean, line, column, 'Você')
            coord = int(input('Insira a cordenada que deseja atacar: ').strip().split(''))
            Players.attacksUser(enemyOcean, coord[0], column[1], 'Você')
            # self.attacksMachine(ownOcean, listOfMachineAttacks,'Máquina')
            # ------- shows the current status of the enemy map -------
            print('Mapa inimigo:')
            NavalBattle.showBattleLattice(enemyOcean)
            # ------- shows the current status of your map -------
            # print('\nMeu mapa:')
            NavalBattle.showBattleLattice(self)
            # ------- checks if the game is over -------
            if Players.checkWinner(self, enemyOcean): break
        return
