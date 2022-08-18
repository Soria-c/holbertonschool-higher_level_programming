#!/bin/bash
# Script that takes in a URL and displays all HTTP methods the server will accept
curl -ILs "$1" | grep -Po "(Allow|allow):[[:blank:]]\K([[:upper:]]+(,[[:blank:]])?)+"
