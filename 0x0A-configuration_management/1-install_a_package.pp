# install puppet-lint (2.1.0)

package { 'flask':
    ensure   => '2.1.0',
    #name     => 'Flask 2.1.0',
    provider => 'pip3'
}
