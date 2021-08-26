#!/usr/bin/env bash
# Configure web server

sudo apt-get update
sudo apt-get install -y nginx
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "This is a Test" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}' /etc/nginx/sites-available/default
sudo service nginx restart