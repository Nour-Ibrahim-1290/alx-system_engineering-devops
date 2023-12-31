#!/usr/bin/env bash
# configuration changes automation using Puppet

file { 'ect/ssh/ssh_config': 
	ensure => present,
	content => "
		#SSH client configuration
		host*
		IdentityFile ~/.ssh/school
		PasswordAuthentication no
		",
}
