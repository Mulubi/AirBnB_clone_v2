#!/usr/bin/env bash
# Sets up a web server for deployment of web_static.

# Set the host and user to connect as
# host=['54.157.156.170' , '3.90.85.138']
# user='ubuntu'

# Set the required directories
data='/data/'
web_static='/data/web_static/'
releases='/data/web_static/releases/'
shared='/data/web_static/shared/'
releases_test='/data/web_static/releases/test/'
symbolic_link='/data/web_static/current'
# Create a fake HTML file
html_file='/data/web_static/releases/test/index.html'

# Connect to the host and update the package lists
sudo apt-get update
# Install nginx 
sudo apt-get install -y nginx

#Create the required folders if they do not exist
if [ ! -d $releases_test ]; then mkdir -p
$releases_test; fi
if [ ! -d $shared ]; then mkdir -p
$shared; fi
if [ ! -d $symbolic_link ]; then mkdir -p
$symbolic_link; fi

# Insert simple content into the html file
echo "Warren Mulubi Tech Guy" > html_file
ln -sf $releases_test $symbolic_link

# Set the ownership and permission of the data file
chown -R ubuntu $data
chgrp -R ubuntu $data

# Set the Nginx configuration file
nginx_config="/etc/nginx/sites-available/default"

# Update the Nginx Config to use the alias directive
sed -i 's|root /var/www/html;|root /var/www
/html;\n\t\talias /data/web_static/current/;|' $nginx_config

# Restart Nginx
service nginx restart
