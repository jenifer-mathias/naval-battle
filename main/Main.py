from main.NavalBattle import NavalBattle
from main.Ocean import Ocean
from main.Vessel import Vessel


class Main:
    strikeGroup = [Vessel.portaAvioes, Vessel.cruzadores, Vessel.destroyers, Vessel.submarinos]

    def main(self):
        # --------------------- Create and position my vessels -----------------------

        ownOcean = Ocean.makeOcean(self)
        Vessel.positionVessel(Main.strikeGroup, ownOcean)
        NavalBattle.showBattleLattice(ownOcean)
        print()

        # --------------------- Creates and positions machine vessels ----------------

        enemyOcean = Ocean.makeOcean(self)
        Vessel.positionVessel(Main.strikeGroup, enemyOcean)
        NavalBattle.showBattleLattice(enemyOcean)

        # --------------------- Start game --------------------------------------------

        NavalBattle.startGame(ownOcean, enemyOcean)

        print()

    def __init__(self):
        self.main()
