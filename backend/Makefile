MANAGE := python manage.py

.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: venv
venv: ## Make a new virtual environment
	pipenv shell

.PHONY: install
install: venv ## Install or update dependencies
	pipenv install

freeze: ## Pin current dependencies
	pipenv lock -r > ../requirements.txt

migrate: ## Make and run migrations
	$(MANAGE) makemigrations
	$(MANAGE) migrate

collectstatic: ## Run collectstatic
	$(MANAGE) collectstatic --noinput

changepassword: ## Change password superuser
	$(MANAGE) changepassword flavienhugs@pm.me

.PHONY: test
test: ## Run tests
	$(MANAGE) --verbosity=0 --parallel --failfast

createsuperuser: ## Run the Django server
	$(MANAGE) createsuperuser --username="flavienhugs@pm.me" --email="flavienhugs@pm.me"
