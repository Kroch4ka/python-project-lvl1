#!/usr/bin/env python3

from brain_games.games.brain_progression import formatting_progression
from brain_games.games.engine_brain import interact_with_player


def main():
    interact_with_player(formatting_progression)


if __name__ == '__main__':
    main()
