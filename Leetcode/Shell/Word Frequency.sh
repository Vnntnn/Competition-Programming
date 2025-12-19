#!/bin/bash
tr -s '[:space:]' '\n' < words.txt | grep -v '^$' | sort | uniq -c | sort -nr | awk '{print $2, $1}'