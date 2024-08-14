# Fixes an apache2 server returning a 500 error

# Define file path
$file_path = '/var/www/html/wp-settings.php'

# Define string causing error
$old_string = 'class-wp-locale.phpp'

# Define correct string
$new_string = 'class-wp-locale.php'

# Perform string replacement on file
exec {'replace_class-wp-locale.phpp':
  command => "sudo sed -i 's/${old_string}/${new_string}/g' ${file_path}",
  path    => '/bin:/usr/bin',
  onlyif  => "grep -q '${old_string}' ${file_path}"
}
