# Fixed error using stace

exec { 'Fix php error':
  provider => shell,
  command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
}
