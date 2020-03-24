# Using puppet puppet will be installed.

package {'puppet-lint':
  ensure   => '2.1.1',
  name	   => 'peppet-lint',
  provider => 'gem'
}
