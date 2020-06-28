#!/bin/bash

# Prints all env variables with _ in the name

docker inspect -f \
    '{{range $index, $value := .Config.Env}}{{println $value}}{{end}}' \
    $1 | grep _