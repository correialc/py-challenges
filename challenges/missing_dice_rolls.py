from itertools import combinations_with_replacement


def missing_dice_rolls(A, F, M):

    dice_rolls_perm = combinations_with_replacement([1, 2, 3, 4, 5, 6], F)
    missing_sum = M * (len(A) + F) - sum(A)

    for p in list(dice_rolls_perm):
        if sum(p) == missing_sum:
            return list(p)

    return [0]
