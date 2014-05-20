
.PHONY: default

default: createdb
	. ./env.sh
	. var/bin/activate && app/manage.py collectstatic --noinput
	. var/bin/activate && app/manage.py syncdb --noinput
	. var/bin/activate && app/manage.py migrate

createdb:
	createuser -d -l -s pawtrain || echo user already exists
	createdb -O pawtrain pawtrain || echo db already exists

.PHONY: test
test:
	. var/bin/activate && app/manage.py test pawtrain

.PHONY: shell
shell:
	. var/bin/activate && app/manage.py shell_plus

.PHONY: develop
develop:
	. var/bin/activate && app/manage.py runserver 127.0.0.1:8008

.PHONY: prod
prod:
	[ -e var/tmp/supervisor.sock ] || (. var/bin/activate && var/bin/supervisord)
	. var/bin/activate && var/bin/supervisorctl start pawtrain-gunicorn

.PHONY: clean
clean:
	rm -Rf var

