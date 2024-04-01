#!/bin/bash
# sends a GET request to the URL, and displays
# the body of the response with a header variable.
curl --header "X-School-User-Id:98" -s "$1"
