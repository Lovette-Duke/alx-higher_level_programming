#!/bin/bash
# display the size of a body for a given URL.
curl -sI "$1" | wc -c``
