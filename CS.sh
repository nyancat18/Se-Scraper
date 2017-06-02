#!/bin/bash
echo "Generating CSV from text output"
sed 's/,//g' "kp.txt" > "kr.txt"
sed 's/,//g' "us.txt" > "sam.txt"

notify-send "Ready" "The CSV output has been generated"
