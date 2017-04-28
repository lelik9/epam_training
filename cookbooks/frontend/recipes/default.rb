#
# Cookbook Name:: frontend
# Recipe:: default
#
# Copyright 2017, YOUR_COMPANY_NAME
#
# All rights reserved - Do Not Redistribute
#
#include_recipe 'chef_nginx::default'

nodes = search(:node, "recipe:backend")

node.default['nginx']['backend']['servers'] = nodes.collect{|node| node['fqdn']}

include_recipe 'chef_nginx::default'

