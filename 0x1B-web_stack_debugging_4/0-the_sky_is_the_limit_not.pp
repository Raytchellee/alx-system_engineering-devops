# Disributed requests evenly

exec {'replace':
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  before   => Exec['restart'],
  provider => shell,
}

exec {'restart':
  command  => 'sudo service nginx restart',
  provider => shell,
}
