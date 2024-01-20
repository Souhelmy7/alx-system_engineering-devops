# 1-install_a_package.pp

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

package { 'Werkzeug':
  ensure   => '2.1.1',  # Specify a version that is compatible with Flask 2.1.0
  provider => 'pip3',
}

exec { 'Refresh the shell':
  command     => 'exec $SHELL',
  path        => ['/bin', '/usr/bin', '/usr/local/bin'],
  refreshonly => true,
}
