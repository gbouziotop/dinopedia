build-initial:
	docker-compose build --build-arg USER_ID="$(shell id -u)" --build-arg GROUP_ID="$(shell id -g)"
	mkdir www
	docker-compose run --rm --user $(shell id -u):$(shell id -g) app python dinopedia/manage.py migrate
	docker-compose run --rm --user $(shell id -u):$(shell id -g) app python dinopedia/manage.py collectstatic

build-all:
	docker-compose build --build-arg USER_ID="$(shell id -u)" --build-arg GROUP_ID="$(shell id -g)"
	docker-compose run --rm --user $(shell id -u):$(shell id -g) app python dinopedia/manage.py makemigrations $(app) --noinput
	docker-compose run --rm --user $(shell id -u):$(shell id -g) app python dinopedia/manage.py collectstatic

build-all-no-cache:
	docker-compose build --build-arg USER_ID="$(shell id -u)" --build-arg GROUP_ID="$(shell id -g)" --no-cache

build-app:
	docker-compose build --build-arg USER_ID="$(shell id -u)" --build-arg GROUP_ID="$(shell id -g)" app

build-app-no-cache:
	docker-compose build --build-arg USER_ID="$(shell id -u)" --build-arg GROUP_ID="$(shell id -g)" --no-cache app

collect-static:
	docker-compose run --rm --user $(shell id -u):$(shell id -g) app python dinopedia/manage.py collectstatic

make-migrations:
	docker-compose run --rm --user $(shell id -u):$(shell id -g) app python dinopedia/manage.py makemigrations $(app) --noinput

shell-plus:
	docker-compose run --rm --user $(shell id -u):$(shell id -g) app python dinopedia/manage.py shell_plus

test_py:
	docker-compose run -e PYTHONIOENCODING=UTF-8 --rm --user $(shell id -u):$(shell id -g) app python dinopedia/manage.py test dinopedia --failfast --parallel

create-superuser:
	docker-compose run --rm --user $(shell id -u):$(shell id -g) app python dinopedia/manage.py createsuperuser

linter-py:
	docker-compose run --rm linter_py

