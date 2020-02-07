#!/bin/bash

# Debian/Ubuntu
apt-get install python-pip
pip install git+https://github.com/shadowsocks/shadowsocks.git@master

password=$1

cat>/etc/shadowsocks.json<<EOF
{
    "server":"0.0.0.0",
    "server_port":8388,
    "local_address": "127.0.0.1",
    "local_port":1080,
    "password":"$password",
    "timeout":300,
    "method":"aes-256-cfb",
    "fast_open": false
}
EOF
