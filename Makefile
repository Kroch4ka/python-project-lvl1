#Makefile
install:
	poetry install
	poetry add prompt
linter:
	poetry run flake8 brain_games
