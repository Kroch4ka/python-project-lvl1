#!/usr/bin/env python3

from brain_games.games.brain_progression import progression
from brain_games.games.engine_brain import engine_brain


def main():
    engine_brain(progression, "What number is missing in the progression?")


if __name__ == '__main__':
    main()
