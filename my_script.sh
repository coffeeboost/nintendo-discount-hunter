#!/bin/sh
if [[ -f process_data.ipynb ]]
then
 jupyter nbconvert --execute process_data.ipynb
 rm process_data.html
else
 echo "source file is not found"
fi
