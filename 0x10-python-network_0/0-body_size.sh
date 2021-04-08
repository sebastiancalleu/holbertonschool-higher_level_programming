#!/bin/bash
# script to get the content-length from a response
curl -s  "$1"  -I | grep Content-Length | cut -d " " -f 2