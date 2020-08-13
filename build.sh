#!/bin/bash
./buildfast.sh
cd src
makeindex book.idx -s StyleInd.ist
biber book
cd ../
./buildfast.sh
./buildfast.sh
