import random
from .all_winning_moves import winning_moves

data = {
    "user_moves": [],
    "oppo_moves": [],
    "turn": None
}


class ticTacToe():
    def __init__(self):
        self.user = data['user_moves']
        self.oppo = data['oppo_moves']
        self.turn = data['turn'] if data['turn'] else random.choice(["user","oppo"])

    def _change_move(self):
        self.turn = "oppo" if self.turn == "user" else "user"

    def _ask_user(self):
        while True:
            try:
                x, y, z = map(int, input("play -> ").split())
                move = (x, y, z)

                if not (0 <= x < 3 and 0 <= y < 3 and 0 <= z < 3):
                    print("Invalid")
                    continue

                if move in self.user or move in self.oppo:
                    print("used")
                    continue

                return move
            except:
                print("Invalid")

    def _check_win(self, moves):
        for line in winning_moves:
            if all(pos in moves for pos in line):
                return True
        return False

    def play(self):
        while True:
            if self.turn == "user":
                move = self._ask_user()
                self.user.append(move)

                if self._check_win(self.user):
                    print("User wins")
                    break

            else:
                available = [m for m in [
                    (x,y,z)
                    for x in range(3)
                    for y in range(3)
                    for z in range(3)
                ] if m not in self.user and m not in self.oppo]

                move = random.choice(available)
                print("oppo move ->", move)
                self.oppo.append(move)

                if self._check_win(self.oppo):
                    print("Oppo wins")
                    break

            self._change_move()
