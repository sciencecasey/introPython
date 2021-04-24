"""
use a directed graph to solve the max flow of the baseball teams
is there a way for a team to finish with the most wins in their division
1. check if a time is arbitrarily eliminated bc w[i] + r[i] < w[k]
2. create a weighted directed graph, keeping the team of interest out of the graph entirely
    each graph assumes the the team of interest wins the rest of their wins
    s: source, t: sink
    gameV: 0-1, 0-2, 0-3, 1-2, 1-3, 2-3 (all combinations of games that could take place even if not scheduled)
    teamV: collapse onto the teams
    edge s_game: weighted with number of games remaining bt. specific teams
    edge game_team: weighted by the wins (max flow automatically simulates the possible wins)
    edge team_t: w[compare_team]+r[compare_team]-w[team]
        return from the flow statistics:
            if all the edges from s_game are saturated, it means that the team of interest is not eliminated
            else: eliminate the team
"""
import numpy as np
import pandas as pd
import networkx as nx
from itertools import combinations


def main():
    filepaths = ["ivy_league.txt", "mlb.txt", "potter.txt", "world_cup.txt"]
    for path in filepaths:
        basic_list = read_input(path)
        table = convert_table(basic_list)
        # make dictionary to hold the eliminated values
        f = list(np.repeat(False, len(table.index)))
        eliminated = dict(zip(list(table.index), f))
        # trivial eliminations
        trivial_elim(table, eliminated)
        # make graphs
        for org,val in eliminated.items():
            if not val:
                # not eliminated make graph
                g = make_graph(table, org)
                result = nx.maximum_flow(g, "s", "t")
                # if games left originally != games left after maxflow
                e = g.edges.data()
                s_before = [] # save the input weights
                for _,__,capacity in e:
                    if _ == 's':
                        s_before.append(capacity['capacity'])
                if sum(s_before) != result[0]:
                    # set the org to eliminated
                    eliminated[org] = True
                    print(f'{org} was eliminated by max flow')
                else:
                    print(f'{org} is still in the competition: not eliminated')


def print_out(elim: dict):
    pass
    # print each team and if eliminated or not


# trivial elimination
def trivial_elim(table: pd.DataFrame, elim: dict):
    """
    adjusts the elimination dictionary to
    """
    for org in range(0, len(table.index)):
        y = table["wins"][org] + table["remaining"][org] < (table["wins"])
        if any(y):
            elim[table.index[org]] = True  # eliminate the organization
            by = list(table.index[y])
            print(f'{table.index[org]} was trivially eliminated by ', end="")
            print(*by, sep=", ")
    return elim


def read_input(inpath: str):
    """
    reads messy input into a nested list
    returns the list
    """
    file = open(inpath, 'r')
    times = int(file.readline())  # the number of lines in the file after this one
    table = []
    for loop in range(0, times):
        line = file.readline().strip()
        # split according to spaces
        listed = line.split(" ")
        while "" in listed:
            listed.remove("")
        table.append(listed)
    file.close()
    return table


def convert_table(table: list):
    """
    formats nested lists into a pandas data frame
    """
    table = pd.DataFrame(table)
    # rename the rows
    names = table.iloc[:, 0].values
    names = names.astype(str)
    table.index = names
    table = table.drop(0, axis=1)  # remove redundancy
    # rename the columns
    col_titles = ['wins', 'losses', 'remaining']
    col_titles.extend(names)
    table.columns = col_titles
    # change data types
    table = table.apply(pd.to_numeric)
    return table


def make_graph(table: pd.DataFrame, org: str):
    # convert data frame to a graph
    interest = list(table.index)
    interest.remove(org)
    # make one graph per organization
    # print("Making graph for: " + org)
    g = nx.DiGraph()
    g.add_nodes_from(interest)
    # add all 2-way game combinations
    combs = list(combinations(list(g.nodes), 2))
    g.add_nodes_from(combs)
    g.add_node("s")
    g.add_node("t")
    # add edges from start -> game -> team -> end
    for org_ in interest:
        for game in combs:
            path_ = ["game", 0]
            if org_ in game:
                org1, org2 = game  # unpack tuple
                # add edges
                g.add_edge("s", game, capacity=table[org1][org2])  # number of games edge
                g.add_edge(game, org1)  # unweighted wins paths
                g.add_edge(game, org2)
                # output path
                g.add_edge(org1, "t", capacity=(table["wins"][org] + table["remaining"][org] - table["wins"][org1]))
                g.add_edge(org2, "t", capacity=(table["wins"][org] + table["remaining"][org] - table["wins"][org2]))

    return g


if __name__ == '__main__':
    main()
