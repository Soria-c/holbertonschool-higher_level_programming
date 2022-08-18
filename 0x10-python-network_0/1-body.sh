#!/bin/bash
# Script that takes in a URL, sends a GET request to the URL, and displays the body of the response only if it is 200
regex="HTTP/1.1[[:blank:]]([0-9]{3})";response=$(curl -Is "$1");if [[ $response =~ $regex ]]; then if [ "${BASH_REMATCH[1]}" -eq 200 ]; then curl -s "$1"; fi; fi
