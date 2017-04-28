#
# Cookbook Name:: backend
# Recipe:: default
#
# Copyright 2017, YOUR_COMPANY_NAME
#
# All rights reserved - Do Not Redistribute
#

#include_recipes 'mysql'

apt_update

mysql_service 'default' do
  bind_address node['mysql']['address']
  port         node['mysql']['port']
  data_dir     node['mysql']['data_dir']
  action [:create, :start]
end
