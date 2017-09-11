import sys


def glass_balls_problem(balls, floors, memory):
    ball_mem_index = balls - 1
    floor_mem_index = floors - 1
    if memory[ball_mem_index][floor_mem_index] is not None:
        return memory[ball_mem_index][floor_mem_index]

    tries = 0
    single_try = 1

    if balls == 1:
        return floors
    if floors <= 1:
        return floors

    multi_tries = []
    for floor in range(1, floors + 1):
        multi_tries.append(
            max(
                glass_balls_problem(balls - 1, floor - 1, memory=memory),
                glass_balls_problem(balls, floors - floor, memory=memory)))
    if len(multi_tries) > 0:
        tries += min(multi_tries) + single_try

    memory[ball_mem_index][floor_mem_index] = tries
    return tries

B = 25
M = 900
memory = []
for _ in range(B):
    memory.append([None]*M)
print(glass_balls_problem(balls=B, floors=M, memory=memory))