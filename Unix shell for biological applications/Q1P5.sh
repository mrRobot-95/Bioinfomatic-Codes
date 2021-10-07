#!/bin/bash

cd ./fastas

files=$(ls)
for file in $files
do 
	cat $file >> ../combined.fasta
done
