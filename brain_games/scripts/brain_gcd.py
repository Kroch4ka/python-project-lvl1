#!/usr/bin/env python3

from brain_games.games.brain_gcd import gcd
from brain_games.games.engine_brain import engine_brain


def main():
    engine_brain(gcd, 'Find the greatest common divisor of given numbers.')


if __name__ == '__main__':
    main()
