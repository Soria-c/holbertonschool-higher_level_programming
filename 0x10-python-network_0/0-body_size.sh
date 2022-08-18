#!/bin/bash
# Script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
# curl -Is $1 | grep -Po 'Content-Length:[[:blank:]]\K([0-9]+)'

regex="Content-Length:[[:blank:]]([0-9]+)"
response=$(curl -Is "$1")
if [[ $response =~ $regex ]]; then
        echo "${BASH_REMATCH[1]}"
fi
