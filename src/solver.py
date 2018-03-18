import numpy as np
import csv

# from deap import *


def get_players(data_path):
    with open(data_path, 'r') as f:
        reader = csv.DictReader(f, delimiter=',')
        # for row in reader:
        #   print(row)
        total_players = list(reader)
    return [x for x in total_players if int(x['Avaliable'])]


def get_name(players, index):
    return players[index]['Name']


def get_tech(players, index):
    return int(players[index]['Technique'])


def fn_fitness(players, position_list):
    tech_diff_list = []

    for position in position_list:
        teamA_tech = get_tech(players, position[0]) + get_tech(
            players, position[1])
        teamB_tech = get_tech(players, position[2]) + get_tech(
            players, position[3])
        tech_diff_list.append(abs(teamA_tech - teamB_tech))

    return sum(tech_diff_list), tech_diff_list


def random_algorithm(players, num_court):
    random_idx_list = np.random.choice(
        list(range(len(players))), 4 * num_court, replace=False)

    position_list = []
    position = []
    for idx in random_idx_list:

        if len(position) < 4:
            position.append(idx)
        else:
            position_list.append(position[:])
            position = [idx]
    position_list.append(position[:])
    return position_list


# DEBUG
def print_position(players, position_list):
    for position in position_list:
        player_data_list = list(map(lambda idx: '({}:{})'.format(get_name(players, idx), get_tech(players, idx)), position))
        print('{}, {} VS {}, {}'.format(
            player_data_list[0], player_data_list[1], player_data_list[2],
            player_data_list[3]))


if __name__ == '__main__':

    num_court = 2

    # data test
    players = get_players('../data/example.csv')

    fail_flag = True

    while (fail_flag):
        position_list = random_algorithm(players, num_court)

        # DEBUG
        print_position(players, position_list)

        fitness, tech_diff_list = fn_fitness(players, position_list)
        print(fitness, tech_diff_list)

        if fitness < 1:
            fail_flag = False

    print_position(players, position_list)
