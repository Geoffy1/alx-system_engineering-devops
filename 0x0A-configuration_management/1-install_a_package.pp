# install puppet-lint (2.1.0)

package { 'puppet-lint-2.1.0':
    ensure   => '2.1.0',
    name     => 'puppet-lint',
    provider => 'gem'
}
