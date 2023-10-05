#!/usr/bin/env bash
# Setting up my web servers for the deployment of web_static

mkdir -p /data/web_static
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test
echo "test deploying web_static" > /data/web_static/releases/test/index.html
ln -fs /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data
sed -i '/^\tserver_name/ a\\tlocation /hbnb_static \{\n\t\talias /data/web_static/current;\n\t\}\n' /etc/nginx/sites-available/default
service nginx restart
