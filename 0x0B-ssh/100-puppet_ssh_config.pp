#!/usr/bin/env bash
# configuration changes automation using Puppet

file { 'etc/ssh/ssh_config': 
	ensure => present,
	content => "
		#SSH client configuration
		host*
		IdentityFile ~/.ssh/school
		PasswordAuthentication no
		",
}
