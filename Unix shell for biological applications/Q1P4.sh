#!/bin/bash

cd ./fastas
lis=$(ls)
num=$(cat $lis | grep -c ">")

echo "Total number of fasta files: $num"


