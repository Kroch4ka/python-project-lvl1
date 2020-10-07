
#!/usr/bin/env python3

from brain_games.games.engine_brain import interact_with_player
from brain_games.games.brain_even import formatting_even_game


def main():
    interact_with_player(formatting_even_game)


if __name__ == '__main__':
    main()
