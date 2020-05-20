# Replace wrongly named file
exac { 'mv class-wp-locale.php class-wp-locale.phpp':
     command  => 'sed -i "s|class-wp-locale.phpp|class-wp-locale.php|g" /var/www/html/wp-settings.php',
    provider => shell,
 }
