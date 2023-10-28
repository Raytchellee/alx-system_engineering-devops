# Using Puppet to set up authentication

file_line { 'Turn off passwd auth':
  path     => '/etc/ssh/ssh_config',
  line     => '    PasswordAuthentication no',
  replace  => true,
}


file_line { 'Declaring the identity file':
  path     => '/etc/ssh/ssh_config',
  line     => '    IdentityFile ~/.ssh/school',
  replace  => true,
}
