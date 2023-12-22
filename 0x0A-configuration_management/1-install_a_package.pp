# A script that installs flask from pip3

package {'Flask':
    name     =>  'flask==2.1.0',
    provider => 'pip3'
}
