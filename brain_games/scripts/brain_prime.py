#!/usr/bin/env python3

from brain_games.games.engine_brain import interact_with_player
from brain_games.games.brain_prime import formatting_prime

def main():
    interact_with_player(formatting_prime)


if __name__ == '__main__':
    main()
