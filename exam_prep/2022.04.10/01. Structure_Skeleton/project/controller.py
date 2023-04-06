from typing import List

from project.player import Player
from project.supply.supply import Supply


class Controller:
    def __init__(self):
        self.players: List[Player] = []
        self.supplies: List[Supply] = []

    def add_player(self, *player: Player):
        result = []
        for p in player:
            if p not in self.players:
                result.append(p)
        self.players.extend(result)

        return f"Successfully added: {', '.join(p.name for p in result)}"

    def add_supply(self, *supply: Supply):

        for s in supply:
            if s not in self.supplies:
                self.supplies.append(s)

    def __find_player_by_name(self, player: str):
        for p in self.players:
            if p.name == player:
                return p

    def sustain(self, player_name: str, sustenance_type: str):
        p = self.__find_player_by_name(player_name)
        if p:
            player = p
        if player not in self.players:
            return
        if sustenance_type not in ["Food", "Drink"]:
            return

        if player.stamina == 100:
            return f"{player_name} have enough stamina."

        for s in self.supplies[::-1]:
            if sustenance_type == "Food":
                if s.__class__.__name__ != "Food":
                    raise Exception("There are no food supplies left!")
            if sustenance_type == "Drink":
                if s.__class__.__name__ != "Drink":
                    raise Exception("There are no drink supplies left!")
            player._sustain_player(s.energy)
            self.supplies.pop(s)
            return f"{player_name} sustained successfully with {s.name}."

    @staticmethod
    def attack(first_p, second_p):
        while first_p.stamina or second_p.stamina:
            if first_p.stamina < second_p.stamina:
                second_p.stamina -= first_p.stamina / 2
                first_p.stamina -= second_p.stamina / 2
                if first_p.stamina < 1:
                    first_p.stamina = 0
                    return f"Winner: {second_p.name}"
            else:
                first_p.stamina -= second_p.stamina / 2
                second_p.stamina -= first_p.stamina / 2
                if second_p.stamina < 1:
                    second_p.stamina = 0
                    return f"Winner: {first_p.name}"

    def duel(self, first_player_name: str, second_player_name: str):
        first_p = self.__find_player_by_name(first_player_name)
        second_p = self.__find_player_by_name(second_player_name)
        zero_stamina = []
        for p in (first_p, second_p):
            if p.stamina <= 0:
                zero_stamina.append(f"Player {p.name} does not have enough stamina.")
        if zero_stamina:
            return '\n'.join(zero_stamina)
        self.attack(first_p, second_p)

    def next_day(self):
        for p in self.players:
            p.stamina -= p.age * 2
            if p.stamina < 0:
                p.stamina = 0
            self.sustain(p.name, "Food")
            self.sustain(p.name, "Drink")

    def __str__(self):
        str = []
        for p in self.players:
            str.append(p.__str__())
        for s in self.supplies:
            str.append(s.details())
        return '\n'.join(str)