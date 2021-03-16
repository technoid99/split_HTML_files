#!/bin/bash
input="files.txt"

ls pages/ | sed 's/\.[^.]*$//' > "$input" 

while IFS= read -r line
do
  pandoc.exe -f html -t docx pages/"$line".html -o pages/"$line".docx 
done < "$input"
