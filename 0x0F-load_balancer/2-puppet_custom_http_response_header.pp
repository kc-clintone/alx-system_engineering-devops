# Automate creating a custom HTTP header with puppet

exec {'update package list':
  command => '/usr/bin/sudo apt-get update',
}
-> package {'nginx':
  ensure => 'present',
}
-> file_line {'http_header':
  path  => '/etc/nginx/nginx.conf',
  match => 'http {',
  line  => "http {\n\tadd_header X-Served-By \"${hostname}\";",
}
-> exec {'run':
  command => '/usr/sbin/service nginx restart',
}
