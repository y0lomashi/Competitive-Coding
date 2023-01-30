# Martha takes a jar of quarters to the casino with the intention of becoming rich. She plays three machines in turn. Unknown to her, the machines are entirely predictable. Each play costs one quarter. The first machine pays 30 quarters every 35 plays. The second machine pays 60 quarters every 100 plays. The third machine pays 9 quarters every 10 plays. Martha plays until she runs out of money. How many times can Martha play before she goes broke?

# Input
coins, m1counter, m2counter, m3counter = int(input()), int(input()), int(input()), int(input())

plays = 0
while True: # while martha has coins
    if coins:
        plays += 1
        m1counter += 1
        coins -= 1
        if m1counter == 35:
            coins += 30
            m1counter = 0
    if coins:
        plays += 1
        m2counter += 1
        coins -= 1
        if m2counter == 100:
            coins += 60
            m2counter = 0
    if coins:
        plays += 1
        m3counter += 1
        coins -= 1
        if m3counter == 10:
            coins += 9
            m3counter = 0
    else:
        break

print(f"Martha plays {plays} times before going broke.")
