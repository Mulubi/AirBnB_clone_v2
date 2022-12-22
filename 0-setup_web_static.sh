#!/usr/bin/env bash
# Sets up a web server for deployment of web_static.

# Set the host and user to connect as
# host=['54.157.156.170' , '3.90.85.138']
# user='ubuntu'

# Connect to the host and update the package lists
sudo apt-get update
# Install nginx
sudo apt-get install -y nginx

# Set the required directories
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/current

# Create a fake HTML file
html_file='/data/web_static/releases/test/index.html'

# Insert simple content into the html file
echo "Warren Mulubi Tech Guy" > html_file
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Set the ownership and permission of the data file
chown -R ubuntu /data/
chgrp -R ubuntu /data/

# Set the Nginx configuration file
nginx_config="/etc/nginx/sites-available/default"

# Update the Nginx Config to use the alias directive
printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }
    location /redirect_me {
        return 301 http://cuberule.com/;
    }
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > nginx_config

# Restart Nginx
service nginx restart
