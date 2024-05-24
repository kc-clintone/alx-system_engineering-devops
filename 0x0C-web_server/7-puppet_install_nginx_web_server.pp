# Automating using puppet

# Ensure Nginx package is installed
package { 'nginx':
  ensure => installed,
}

# Ensure the root HTML file is present with the required content
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
  require => Package['nginx'],
}

# Use exec resource to add the rewrite rule if it doesn't already exist
exec { 'add_nginx_rewrite_rule':
  command => 'sed -i "/listen 80 default_server;/a rewrite ^/redirect_me https://www.github.com/kc-clintone permanent;" /etc/nginx/sites-available/default',
  unless  => 'grep "rewrite ^/redirect_me https://www.github.com/kc-clintone permanent;" /etc/nginx/sites-available/default',
  path    => ['/bin', '/usr/bin'],
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Use exec resource to configure Nginx settings
exec { 'configure_nginx':
  command => 'sed -i "/^\\s*root /d" /etc/nginx/sites-available/default; \
              sed -i "/^\\s*index /d" /etc/nginx/sites-available/default; \
              sed -i "/server_name _;/a \\    root /var/www/html;" /etc/nginx/sites-available/default; \
              sed -i "/server_name _;/a \\    index index.html index.htm;" /etc/nginx/sites-available/default; \
              sed -i "/try_files \\$uri \\$uri\\/ =404;/d" /etc/nginx/sites-available/default; \
              sed -i "/location \\/ {/a \\        try_files \\$uri \\$uri\\/ =404;" /etc/nginx/sites-available/default',
  unless  => 'grep "rewrite ^/redirect_me https://www.github.com/kc-clintone permanent;" /etc/nginx/sites-available/default',
  path    => ['/bin', '/usr/bin'],
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Ensure the Nginx service is running and enabled to start at boot
service { 'nginx':
  ensure    => running,
  enable    => true,
  require   => Package['nginx'],
  subscribe => Exec['add_nginx_rewrite_rule', 'configure_nginx'],
}
