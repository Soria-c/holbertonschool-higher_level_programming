#!/bin/bash
# Script that takes in a URL and displays all HTTP methods the server will accept
curl -iLs -X OPTIONS "$1" | grep -Po "allow:[[:blank:]]\K([[:upper:]]+(,[[:blank:]])?)+"
