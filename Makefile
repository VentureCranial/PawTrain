
.PHONY: default

default: createdb
	. ./env.sh
	# . var/bin/activate && app/manage.py collectstatic --noinput
	. var/bin/activate && app/manage.py syncdb --noinput
	. var/bin/activate && app/manage.py migrate
	. var/bin/activate && app/manage.py loaddata oauth_fixtures.yaml

deploy: clean
	make deploy-fast

deploy-fast:
	docker stop pawtrain-dev || true
	docker rm pawtrain-dev || true
	cp /home/pawtrain/oauth_fixtures.yaml /home/pawtrain/PawTrain/app/web/fixtures/
	docker run -t -i -p 0.0.0.0:8008:8008 --name='pawtrain-dev' -v /home/pawtrain/PawTrain:/home/pawtrain/PawTrain -v /var/tmp/pip-cache/:/var/tmp/pip-cache/ venturecranial/pawtrain-deploy make -C /home/pawtrain/PawTrain deploy-stage2

deploy-stage2:
	/etc/init.d/postgresql start
	su pawtrain -c 'make develop'

createdb:
	cat ./enable_postgis.sh
	. ./enable_postgis.sh
	createuser -d -l -s pawtrain -h 127.0.0.1 -U postgres || echo user already exists
	createdb -T template_postgis -O pawtrain -h 127.0.0.1 -U postgres pawtrain || echo db already exists


.PHONY: test
test:
	. var/bin/activate && app/manage.py test pawtrain

.PHONY: shell
shell:
	. var/bin/activate && app/manage.py shell_plus

.PHONY: develop
develop: default
	. var/bin/activate && app/manage.py runserver 0.0.0.0:8008

.PHONY: prod
prod:
	[ -e var/tmp/supervisor.sock ] || (. var/bin/activate && var/bin/supervisord)
	. var/bin/activate && var/bin/supervisorctl start pawtrain-gunicorn

.PHONY: clean
clean:
	rm -Rf var

.PHONY: resetmigration
resetmigration:
	rm -f app/web/migrations/0001_initial.py*
	. var/bin/activate && ./app/manage.py schemamigration --initial web
	. var/bin/activate && ./app/manage.py reset_db --noinput
	. var/bin/activate && ./app/manage.py syncdb --migrate --noinput
	. var/bin/activate && ./app/manage.py loaddata dev_fixtures.yaml
