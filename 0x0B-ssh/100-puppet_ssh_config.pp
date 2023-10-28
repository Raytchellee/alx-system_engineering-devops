# Using Puppet to set up authentication

file_line { 'Remove authentication':
  path     => '/etc/ssh/ssh_config',
  line     => '    PasswordAuthentication no',
  replace  => true,
}


file_line { 'Indicating the IdentityFile':
  path     => '/etc/ssh/ssh_config',
  line     => '    IdentityFile ~/.ssh/school',
  replace  => true,
}
