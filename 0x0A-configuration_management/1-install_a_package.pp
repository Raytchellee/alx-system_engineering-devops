#!/usr/bin/pup
# Installs a flask package

package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
