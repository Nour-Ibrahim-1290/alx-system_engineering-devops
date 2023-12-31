#!/usr/bin/env bash
# configuration changes automation using Puppet

file { 'etc/ssh/ssh_config': 
	ensure  => present,
	path    => 'etc/ssh/ssh_config',
	content => "
		#SSH client configuration
		Host*
		IdentityFile ~/.ssh/school
		PasswordAuthentication no
		",
}
