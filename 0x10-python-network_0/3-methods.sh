#!/bin/bash
curl -s "$1" -I | grep Allow | cut -d " " -f 2-