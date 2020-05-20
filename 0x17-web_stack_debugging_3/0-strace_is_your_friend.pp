# Replace wrongly named file
exac { 'mv class-wp-locale.php class-wp-locale.phpp':
     command => "sed -i 's/phpp/php/g' wp-settings.php",
     path => ['/bin'],
     cwd => '/var/www/html/',
 }
