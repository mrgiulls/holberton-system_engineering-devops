#Create a file

file {'Create a file':
    path    => '/tmp/school',
    mode    =>  '0744',
    owner   =>  www-data,
    group   =>  www-data,
    content =>  'I love Puppet',
}