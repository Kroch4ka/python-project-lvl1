#!/usr/bin/env python3

from brain_games.games.brain_progression import formatting_progression
from brain_games.games.engine_brain import launch_game


def main():
    launch_game(formatting_progression)


if __name__ == '__main__':
    main()
