#!/bin/bash
# scrip to get the status code
curl -s -w "%{http_code}\n" "$1" -o /dev/null
