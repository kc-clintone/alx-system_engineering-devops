# Automate custom header creation with puppet

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Define custom HTTP header value as the hostname of the server
$server_hostname = $facts['hostname']

# Configure Nginx to add custom HTTP header response
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        # Add custom HTTP header response
        add_header X-Served-By

