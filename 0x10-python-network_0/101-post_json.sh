#!/bin/bash
# script to load a json
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
