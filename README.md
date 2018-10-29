Ansible script for deploying 5 nodes docker based HDP Sandbox
=============================================================

ansible script that :

 * create 5 docker containers with systemd
 * install ambari in master1 container
 * install ambari-agent in all containers
 * install use ambari blueprint to deploy 2 node hdp cluster on 2 containers

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


