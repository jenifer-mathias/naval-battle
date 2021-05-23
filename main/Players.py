import random
import time

from main.Main import Main


class Players:

    def attacksMachine(self, attackOcean, listOfAttacks, machine):
        while True:
            attack = random.randint(0, len(attackOcean) - 1),
            random.randint(0, len(attackOcean) - 1)
            if attack not in listOfAttacks:
                listOfAttacks.append(attack)
                self.attacksUser(self, int(attack[0]), int(attack[1]), machine)
                break

    def attacksUser(self, line, column, user):
        listOfPossibilities = []
        for vessel in Main.strikeGroup:
            listOfPossibilities.append(vessel.get('sigla'))
        if self[line][column] in listOfPossibilities:
            self[line][column] = 'x'
            print('{} ACERTOU'.format(user))
            time.sleep(1)
        else:
            print('{} ERROU'.format(user))
            time.sleep(1)

    def checkWinner(self, enemyOcean):
        iAmAlive = False
        machineIsAlive = False
        listOfPossibilities = []
        for vessel in Main.strikeGroup:
            listOfPossibilities.append(vessel.get('sigla'))
            for line in Main.strikeGroup:
                for value in line:
                    if value in listOfPossibilities:
                        iAmAlive = True
                        break
                    for line in enemyOcean:
                        for value in line:
                            if value in listOfPossibilities:
                                machineIsAlive = True
                            break
                    if iAmAlive and machineIsAlive:
                        return False
                    elif iAmAlive and not machineIsAlive:
                        print('Você venceu!')
                        return True
                    else:
                        print('A máquina venceu!')
                        return True
