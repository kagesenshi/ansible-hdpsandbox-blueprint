Ansible script for deploying 5 nodes docker based HDP Sandbox
=============================================================

ansible script that :

 * create 5 docker containers with systemd
 * install ambari in master1 container
 * install ambari-agent in 3 containers (master1, edge, worker1)
 * use ambari blueprint to deploy 3 node hdp cluster on 3 containers

Usage
-------

Create an inventory file (eg: inventory.yml):

```yaml
all:
  hosts:
    localhost:
      ansible_port: 2222
      ansible_host: 127.0.0.1
      ansible_user: root
      ansible_ssh_pass: password
```

Deploy

```sh
ansible-playbook -i inventory.yml playbook.yml
```

Access cockpit at VM's HTTPS port 9090, and a Squid proxy at HTTP port 3128

Ambari is at http://master1.cluster:8080 through the proxy server

Default root password in containers is `password`. Default Ambari admin password is `admin`
