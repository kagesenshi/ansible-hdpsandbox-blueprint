Ansible script for deploying 5 nodes docker based HDP Sandbox
=============================================================

ansible script that :

 * create 5 docker containers with systemd
 * install ambari in master1 container
 * install ambari-agent in all containers
 * install use ambari blueprint to deploy 2 node hdp cluster on 2 containers
