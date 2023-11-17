from random import shuffle

successes = 0
failures = 0
master_loop_count = 1
while master_loop_count < 101:
    # Create the prisoner participants by assigning each one a number
    prisoner_number = []
    loop_count = 1
    while loop_count < 101:
        prisoner_number.append(loop_count)
        loop_count += 1

    # Create chest of drawers with 100 random tickets in each drawer
    tickets = []
    loop_count = 1
    while loop_count < 101:
        tickets.append(loop_count)
        loop_count += 1
    shuffle(tickets)

    # Fill drawers with tickets randomly assigned
    drawers = {}
    drawer_count = 1
    shuffle_count = 0
    while drawer_count < 101:
        drawers[drawer_count] = tickets[shuffle_count]
        drawer_count += 1
        shuffle_count += 1

    # Simulate prisoners completing the exercise
    x = 0
    failure_signal = 0
    while x < 100:
        selected_drawer = drawers[prisoner_number[x]]
        loop_limit = 1

        while loop_limit < 51:
            if selected_drawer == prisoner_number[x]:
                loop_limit = 100
            else:
                selected_drawer = drawers[selected_drawer]
                loop_limit += 1
                if loop_limit == 51:
                    failures = failures + 1
                    failure_signal = 1
        if failure_signal == 1:
            break
        x += 1

    if failure_signal == 0:
        successes = successes + 1

    master_loop_count += 1

print("Successes = " + str(successes))
print("Failures = " + str(failures))
