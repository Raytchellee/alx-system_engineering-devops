# installing nginx with puppet

package { 'nginx':
  ensure => installed,
  name   => 'nginx',
}
file { '/var/www/html/index.nginx-debian.html':
  content => 'Hello World!',
  path    => '/var/www/html/index.nginx-debian.html'
}
file_line { 'redirection':
  ensure   => present,
  path     => '/etc/nginx/sites-available/default',
  after    => 'server_name _;',
  line     => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  multiple => true
}
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
