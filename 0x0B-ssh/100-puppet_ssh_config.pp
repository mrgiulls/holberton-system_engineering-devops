# Set up your client SSH configuration file so that u can connect to a server without typin a password
file_line { 'identity_file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '	IdentityFile ~/.ssh/school',
}

file_line { 'password_no':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '	PasswordAuthentication no',
}