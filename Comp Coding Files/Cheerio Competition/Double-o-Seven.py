# Find optimal moves for a game of 007 given opponents moves
# R = reload, F = shoot, B = block

import sys

n = int(sys.stdin.readline())
sequence = sys.stdin.readline()
score, ammo = 0, 0
op_ammo = 0
#testing list
moves = []
for move in sequence:
    if move == "R":
        op_ammo += 1
        if ammo > 0:
            score += 1
            ammo -= 1
            moves.append("F")
        elif ammo == 0:
            ammo += 1
            moves.append("R")

    elif move == "F":
        if op_ammo > 0:
            op_ammo -= 1
            moves.append("B")
        elif op_ammo == 0 and ammo > 0:
            score += 1
            ammo -= 1
            moves.append("F")
        elif op_ammo == 0 and ammo == 0:
            ammo += 1
            moves.append("R")
    elif move == "B":
        ammo += 1
        moves.append("R")
print(score)
