# Use puppet to install flask from pip3
# version must be 2.1.0

# Install Flask v2 and Werkzeug globally
exec { 'install_flask_and_werkzeug':
  command => '/usr/bin/pip3 install Flask==2.1.0 Werkzeug==2.1.1',
  unless  => '/usr/bin/pip3 show Flask | grep Version | grep 2.1.0',
}
