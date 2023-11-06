#using puppet to automate task 0


exec {'installing nginx':
  provider => shell,
  command  => 'sudo apt-get -y update;
  sudo apt-get -y install nginx',
  before   => Exec['adding header'],
}

exec { 'adding header':
  provider    => shell,
  environment => ["HOST=${hostname}"],
  command     => 'sudo sed -i "47i\\\tadd_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default',
  before      => Exec['nginx restart'],
}

exec { 'nginx restart':
  provider => shell,
  command  => 'sudo service nginx restart',
}
