#!/bin/bash
# a bash script that takes in a URL, sends a get request and display only tha body of a 200 status
curl -ls "$1"
