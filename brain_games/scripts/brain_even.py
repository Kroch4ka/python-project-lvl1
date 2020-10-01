#!/usr/bin/env python3

from brain_games.games.engine_brain import engine_brain
from brain_games.games.brain_even import brain_even


def main():
    engine_brain(brain_even, 'Answer "yes" if number even otherwise answer "no".')


if __name__ == '__main__':
    main()
