# Automate custom header creation with puppet

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

exec { 'configure_nginx':
  command  => '/usr/bin/apt-get -y update && \
               /usr/bin/apt-get -y install nginx && \
               /bin/sed -i "/listen 80 default_server;/a add_header X-Served-By \$HOSTNAME;" /etc/nginx/sites-available/default && \
               /usr/sbin/service nginx restart',
  provider => shell,
}

