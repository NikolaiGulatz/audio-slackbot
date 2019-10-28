.PHONY: test

tox:
	@poetry run tox

black:
	@poetry run black .

black_check:
	@poetry run black --check .

pylint:
	@poetry run pylint audio_slackbot

test:
	@poetry run pytest --cov=audio_slackbot --cov-report term-missing test/

lint: pylint black_check
