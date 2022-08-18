#!/bin/bash
# Script that takes in a URL, sends a GET request to the URL, and displays the body of the response only if it is 200
curl -sL "$1"
