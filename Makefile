SHELL := /bin/bash
app = locutus

clean:
	## TODO address when we lack perms to delete these
	find . -name __pycache__ -prune -exec rm -fr {} \;
	find . -name "*.pyc" -exec rm -fr {} \;
	find . -name .eggs -prune -exec rm -fr {} \;
	find . -name "*.egg-info" -prune -exec rm -fr {} \;
	rm -fr build/ dist/
	## Kill pytest_cache for good measure
	rm -rf .pytest_cache
	## fix for file import error...
	rm -rf ./test/__pycache__

require-stage:
ifndef stage
	$(error stage arg is required for this target)
endif

cp-envvars:
	cp ./envvars.sample ./envvars

dist: cp-envvars
	docker-compose run ${app}-dist

build-deploy: dist
	docker-compose build ${app}-deploy

build-dev: dist
	docker-compose build ${app}

deploy: require-stage build-deploy
	docker-compose run ${app}-deploy \
	  ./node_modules/serverless/bin/serverless deploy --stage ${stage}

test: build-dev
	docker-compose run ${app} /test.sh

ftest: require-stage build-dev
	docker-compose run ${app} robot \
	  --variablefile ftest/env/${stage}.py \
	  ftest

test-dev: test

build-docs:
	./node_modules/.bin/spectacle -1 -t docs docs/docs.json
