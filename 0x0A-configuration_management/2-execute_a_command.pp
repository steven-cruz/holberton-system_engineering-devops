# create a manifest that kills a process named killmenow.
exec {'killnemow':
  command => '/usr/bin/pkill --full killmenow'
}
