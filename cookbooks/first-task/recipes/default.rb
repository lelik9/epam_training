#
# Cookbook Name:: first-task
# Recipe:: default
#
# Copyright 2017, YOUR_COMPANY_NAME
#
# All rights reserved - Do Not Redistribute
#
include_recipe 'iptables'
include_recipe 'ntp'
include_recipe 'apt'
include_recipe 'sudo'

apt_update

apt_package 'base' do
  action :install
  package_name ['htop', 'wget', 'git', 'iotop', 'tcpdump', 'vim', 'sysstat']
end

user 'user' do
  username node['user']
  home  '/home/'+node['user']
  shell '/bin/bash'
  manage_home true
  action :create
end

directory '/home/'+node['user']+'/.ssh' do
  action :create
end

template '/home/'+node['user']+'/.ssh/authorized_keys' do
  atomic_update true
  source 'id_rsa.pub' 
end

bash 'ssh' do
  code <<-EOL
	sed -e 's/UsePAM/UsePAM no/' /etc/ssh/sshd_config >> /etc/ssh/sshd_config.new
	cp /etc/ssh/sshd_config /etc/ssh/sshd_config.old; mv /etc/ssh/sshd_config.new /etc/ssh/sshd_config
	EOL
end

service 'sshd' do
  action :reload
end

bash 'clearMOTD' do
 code 'rm -rf etc/update-motd.d/*'
end

cookbook_file '/etc/update-motd.d/00-header' do
  source '00-header'
  mode '0777'
  action :create
end
