# Fixed error using stace

exec { 'fixed-php-error':
  path    => '/bin',
  command => 'sed -i 's/phpp/php/g'  /var/www/html/wp-settings.php';
}
