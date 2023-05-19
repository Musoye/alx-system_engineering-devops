# Slve why our server is failing
include stdlib

file_line { 'allow many requests':
  ensure  => present,
  path    => '/etc/default/nginx',
  line    => 'LIMIT="-n 4096"',
  replace => true
}

exec { 'restart nginx':
  command  => 'sudo service nginx restart',
  provider => shell
}
