runserver:
	# poetry run gunicorn --bind 0.0.0.0:8000 src.config.wsgi:application
	poetry run python -m src.manage runserver 0.0.0.0:8000

runserver-prod:
	poetry run gunicorn --bind 0.0.0.0:8000 src.config.wsgi:application

collectstatic:
	poetry run python -m src.manage collectstatic --noinput


migrate:
	poetry run python -m src.manage migrate


collect:
	poetry run python -m src.manage migrate
	poetry run python -m src.manage initadmin


migrations:
	poetry run python -m src.manage makemigrations

initadmin:
	poetry run python -m src.manage initadmin


refresh-db:
	poetry run python -m src.manage flush
	poetry run python -m src.manage migrate
	poetry run python -m src.manage initadmin

fakedata:
	poetry run python -m src.manage fakedata

loaddata:
	poetry run python -m src.manage migrate
	poetry run python -m src.manage initadmin
	poetry run python -m src.manage load_data
