# Hackerrank problem: https://www.hackerrank.com/challenges/mandragora


def get_max_score(mandragoras):
    experience = 0
    strength = 1
    sorted_hp_list = sorted(mandragoras)
    hp_sum = sum(mandragoras)
    for i in range(len(sorted_hp_list)):
        kill_sum = strength * hp_sum
        eat_sum = (strength + 1)*(hp_sum - sorted_hp_list[i])
        if eat_sum > kill_sum:
            strength += 1
            hp_sum -= sorted_hp_list[i]
        else:
            experience = strength * hp_sum
            return experience


t = int(input())
for i in range(t):
    n_mandragoras = int(input())
    mandragoras = [int(x) for x in input().split()]
    print(get_max_score(mandragoras))