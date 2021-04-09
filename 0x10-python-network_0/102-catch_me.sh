#!/bin/bash
# Script to catch them
curl -s -L -X PUT "$1" -d "user_id=98" -H "Origin: HolbertonSchool"
