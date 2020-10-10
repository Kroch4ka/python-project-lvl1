#!/usr/bin/env python3

from brain_games.games.brain_calc import calculation_operation
from brain_games.games.engine_brain import launch_game


def main():
    launch_game(calculation_operation)


if __name__  == '__main__':
    main()
