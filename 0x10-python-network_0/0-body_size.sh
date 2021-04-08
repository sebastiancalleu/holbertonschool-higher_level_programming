#!/bin/bash
curl -s  "$1"  -I | grep Content-Length | cut -d " " -f 2