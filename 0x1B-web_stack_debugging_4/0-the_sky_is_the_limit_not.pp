# reset conection port 22
exec { 'increase the uLimit of nginx':
C:\Users\ASUS>sed -i \'s/15/15000/g\' /etc/default/nginx',
  path    => ['/bin']
}
exec { 'restart nginx':
  command => 'service nginx restart',
  path    => ['/usr/bin']
}
