#!/usr/bin/env python3

from brain_games.engine import play
from brain_games.games import even
from brain_games.games_const import DESCRIPTION_calc,START_calc,STOP_calc


def main():

    play(even)


if __name__ == '__main__':
    main()
