# Regulated number of open files

exec {'set-limit-one':
  command  => 'sudo sed -i "s/nofile 5/nofile 50000/" /etc/security/limits.conf',
  before   => Exec['set-limit-two'],
  provider => shell,
}

exec {'set-limit-two':
  command  => 'sudo sed -i "s/nofile 4/nofile 40000/" /etc/security/limits.conf',
  provider => shell,
}
