# Exec a command

exec { 'pkill killmenow':
  path  =>  '/usr/bin/:/usr/local/bin/:/bin/'
}