#!/bin/bash

echo `curl $1 -s | jq .result.overall`
