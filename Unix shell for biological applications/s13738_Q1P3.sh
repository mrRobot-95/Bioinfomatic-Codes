#!/bin/bash

files=$(ls ./fastas)
cd ./fastas
for file in $files
  do
    regexes=$(grep -E -c "(WGKWV|AAEIR)" $file)
    if [ $regexes -eq 1 ]
      then
	line=$(head -n 1 $file)
        echo "$line" >> ../AP2_advanced_headers.txt
    fi
  done
