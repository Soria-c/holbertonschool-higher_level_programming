#!/bin/bash
# Script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
curl -s -X POST "$1/?email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD"
