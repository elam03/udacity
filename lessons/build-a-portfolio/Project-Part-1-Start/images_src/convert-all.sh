#!/bin/bash
for FILE in *.jpg; do
	BASENAME=`basename ${FILE} .jpg`
	echo "Converting ${FILE}..."
	./convert.sh ${BASENAME}
done
