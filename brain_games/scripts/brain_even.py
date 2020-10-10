
#!/usr/bin/env python3

from brain_games.games.engine_brain import launch_game
from brain_games.games.brain_even import formatting_even_game


def main():
    launch_game(formatting_even_game)


if __name__ == '__main__':
    main()
