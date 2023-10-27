# Terminates killmenow process

exec {'killmenow':
    command  => '/usr/bin/pkill killmenow',
}
