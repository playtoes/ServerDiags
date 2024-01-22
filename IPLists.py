#!/bin/bash
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <server_name_or_ip>"
    exit 1
fi

server="$1"

# Get the list of IP addresses configured on the server
ip_addresses=$(ifconfig | grep 'inet ' | awk '{print $2}')

if [[ -n "$ip_addresses" ]]; then
    echo "IP addresses configured on $server:"
    echo "$ip_addresses"
else
    echo "No IP addresses found on $server."
fi

/** Mike Maksosa music
