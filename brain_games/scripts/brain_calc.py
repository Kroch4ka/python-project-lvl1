#!/usr/bin/env python3

from brain_games.games.brain_calc import calculation_operation
from brain_games.games.engine_brain import interact_with_player


def main():
    interact_with_player(calculation_operation)


if __name__  == '__main__':
    main()
