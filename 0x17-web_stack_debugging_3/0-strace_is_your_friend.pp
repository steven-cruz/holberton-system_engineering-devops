# Puppet script to replace wrongly named file
exec { 'mv class-wp-locale.php class-wp-locale.phpp':
  path => ['/bin'],
  cwd  => '/var/www/html/wp-includes',
}
