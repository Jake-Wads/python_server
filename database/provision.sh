#!/usr/bin/env bash

# Small script to modify a default mysql installation on ubuntu 16.04 to allow
# traffic from the outside world.

# Should be run as root.

# edit the mysql config
sed -i 's/^bind-address.*/bind-address = 0.0.0.0/' /etc/mysql/mysql.conf.d/mysqld.cnf
service mysql restart

# allow traffic on 3306 with ufw
ufw allow in 3306/tcp
ufw allow out 3306/tcp
yes | ufw enable
service ufw restart
