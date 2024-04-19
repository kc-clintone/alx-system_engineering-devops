# This will create a file called '0-create_a_file.pp' in the /tmp folder

file {'/tmp/school':
    ensure  => 'file',
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0744',
    content => 'I love Puppet',    
}
