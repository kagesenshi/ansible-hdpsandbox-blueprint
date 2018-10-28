#!/bin/bash

set -e

if [ ! -f "/var/ambari-init-executed" ]; then
   ambari-server setup -s
fi
echo $(date +%Y-%m-%d:%H:%M:%S) >> /var/ambari-init-executed
