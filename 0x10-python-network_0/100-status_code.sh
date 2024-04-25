#!/bin/bash
# script to send request

curl -s -o /dev/null -w "%{http_code} "$1"
