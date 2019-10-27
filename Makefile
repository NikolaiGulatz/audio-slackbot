.PHONY: test

tox:
	@poetry run tox

black:
	@poetry run black .

pylint:
	@poetry run pylint audio_slackbot

pytest:
	@poetry run pytest --cov=audio_slackbot --cov-report term-missing test/
