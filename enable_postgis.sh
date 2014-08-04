POSTGIS_SQL_PATH=`pg_config --sharedir`/contrib/postgis-2.1

# Creating the template spatial database.
createdb -h localhost -U postgres -E UTF8 template_postgis
createlang -h localhost -U postgres -d template_postgis plpgsql # Adding PLPGSQL language support.

# Allows non-superusers the ability to create from this template
psql -h localhost -U postgres -d postgres -c "UPDATE pg_database SET datistemplate='true' WHERE datname='template_postgis';"

# Loading the PostGIS SQL routines
psql -h localhost -U postgres -d template_postgis -f $POSTGIS_SQL_PATH/postgis.sql
psql -h localhost -U postgres -d template_postgis -f $POSTGIS_SQL_PATH/spatial_ref_sys.sql

# Enabling users to alter spatial tables.
psql -h localhost -U postgres -d template_postgis -c "GRANT ALL ON geometry_columns TO PUBLIC;"
psql -h localhost -U postgres -d template_postgis -c "GRANT ALL ON geography_columns TO PUBLIC;"
psql -h localhost -U postgres -d template_postgis -c "GRANT ALL ON spatial_ref_sys TO PUBLIC;"
