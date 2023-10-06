#!/usr/bin/env bash
# A Bash script to set up web servers for the deployment of web_static.

# Nginx Web Servers configuration
SERVER_CONFIG="server {
	listen 80 default_server;
	listen [::]:80 default_server;

	server_name _;
	index index.html index.htm;
	error_page 404 /404.html;
	add_header X-Served-By \$hostname;

	location / {
		root /var/www/html/;
		try_files \$uri \$uri/ =404;
	}

	location /hbnb_static/ {
		alias /data/web_static/current/;
		try_files \$uri \$uri/ =404;
	}

	if (\$request_filename ~ redirect_me) {
		rewrite ^https://github.com/njdam/ permanent;
	}

	location = /404.html {
		root /var/www/error/;
		internal;
	}
}"

# Simple home page Html file to test nginx configuration
HOME_PAGE="<!DOCTYPE html>
<html lang='en'>
	<head>
		<title>Home - AirBnB Clone</title>
	</head>
	<body>
		<h1>Welcome to AirBnB!</h1>
		<p>Practices makes perfect but Life - God = Zero</p>
	<body>
</html>
"

# Checking if Nginx is not installed in order to be installed
# shellcheck disable=SC2230
if [[ "$(which nginx | grep -c nginx)" == '0' ]]; then
    apt-get update
    apt-get -y install nginx
fi

# Making path where to store data and handling error 404
mkdir -p /var/www/html /var/www/error
chmod -R 755 /var/www
echo 'Hello World!' > /var/www/html/index.html
echo -e "Ceci n\x27est pas une page" > /var/www/error/404.html

# Making path directories to test my configuration
mkdir -p /data/web_static/releases/test /data/web_static/shared
echo -e "$HOME_PAGE" > /data/web_static/releases/test/index.html
[ -d /data/web_static/current ] && rm -rf /data/web_static/current

# Symbolic linking web_static release with weba-static current
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Changing owner of data to ubuntu user
chown -hR ubuntu:ubuntu /data

# Configuration of Nginx web server by custom configuration and linking
bash -c "echo -e '$SERVER_CONFIG' > /etc/nginx/sites-available/default"
ln -sf '/etc/nginx/sites-available/default' '/etc/nginx/sites-enabled/default'

# Restarting nginx if is not started to apply changes
if [ "$(pgrep -c nginx)" -le 0 ]; then
	service nginx start
else
	service nginx restart
fi
