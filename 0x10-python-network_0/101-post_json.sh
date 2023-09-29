#!/bin/bash
# Sends a JSON POST request to a given URL with a given JSON file.
curl -s -H "Content-type: application/json" -d "$(cat "$2")" "$1"
