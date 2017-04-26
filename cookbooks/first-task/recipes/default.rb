#
# Cookbook Name:: first-task
# Recipe:: default
#
# Copyright 2017, YOUR_COMPANY_NAME
#
# All rights reserved - Do Not Redistribute
#
apt_update

apt_package 'base' do
  action :install
  package_name ['htop', 'wget', 'git', 'iotop', 'tcpdump', 'vim', 'sysstat']
end
