# Install nginx using puppet

package {'get latest nginx version':
  ensure => 'present',
}

exec {'install nginx':
  command  => 'sudo apt-get update ; sudo apt-get -y install nginx',
  provider => shell,

}

file {'/var/www/html/index.nginx-debian.html':
    content => 'Hello World!',
}

exec {'sudo sed -i "s/listen 80 default_server;/listen 80 default_server;\\n\\tlocation \/redirect_me {\\n\\t\\treturn 301 https:\/\/www.github.com/kc-clintone\/;\\n\\t}/" /etc/nginx/sites-available/default':
  provider => shell,
}

exec {'restart nginx':
  command  => 'sudo service nginx restart',
  provider => shell,
}