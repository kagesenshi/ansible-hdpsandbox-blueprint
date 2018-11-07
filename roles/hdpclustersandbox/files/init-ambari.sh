#!/bin/bash

set -e

if [ ! -f "/var/ambari-init-executed" ]; then
   ambari-server setup -s
fi
echo "host all postgres 172.20.10.0/24 trust" >> /var/lib/pgsql/data/pg_hba.conf
echo "host all rangeradmin 172.20.10.0/24 md5" >> /var/lib/pgsql/data/pg_hba.conf
service postgresql reload
echo $(date +%Y-%m-%d:%H:%M:%S) >> /var/ambari-init-executed
