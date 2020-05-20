# Replace wrongly named file
exac { 'mv class-wp-locale.php class-wp-locale.phpp':
     path => ['/bin'],
     cwd => '/var/www/html/wp-includes',

 }
