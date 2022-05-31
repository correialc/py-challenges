'''
Chooses one code challenge to be solved.
'''

import csv
import random
from typing import List

CHALLENGES_DATA_PATH: str = './challenges-data.csv'

def load_challenges(challenges_data_file: str) -> List:

    with open(challenges_data_file, 'r') as csvfile:
        challenges = csv.reader(csvfile, delimiter='|')
        return [tuple(challenge) for challenge in challenges]

def print_challenge(challenge: str) -> None:
    print('\n---------------------------------------------------')
    print(f"Challenge: {challenge_of_the_day[0].upper()}")
    print(f"Strategy: {challenge_of_the_day[1].upper()}")
    print('---------------------------------------------------\n')

if __name__ == '__main__':
    challenges = load_challenges(CHALLENGES_DATA_PATH)
    challenge_of_the_day = random.choice(challenges)
    print_challenge(challenge_of_the_day)
    