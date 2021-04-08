#!/bin/bash
# script to print the allow http methods
curl -s "$1" -I | grep Allow | cut -d " " -f 2-
