#Makefile
install:
	poetry install
	poetry add prompt
<<<<<<< HEAD
linter:
=======
lint:
>>>>>>> 5718999b4f000a8db8aa45bac7ebf451d646cfba
	poetry run flake8 brain_games
