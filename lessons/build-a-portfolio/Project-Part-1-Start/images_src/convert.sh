#!/bin/sh

CONVERTA="/c/Program Files/ImageMagick-7.0.3-Q16/convert.exe"
SRC="$1"
LOW=60
"${CONVERTA}" $SRC.jpg -quality $LOW low_$SRC.jpg
"${CONVERTA}" $SRC.jpg -quality $LOW low_$SRC.webp
"${CONVERTA}" $SRC.jpg -quality $LOW -resize 50% "$SRC"_"$LOW"q_50pc.jpg
"${CONVERTA}" $SRC.jpg -quality $LOW -resize 50% "$SRC"_"$LOW"q_50pc.webp

# To use this script,
# run the following from a terminal
# in a folder containing an image named foo.jpg (or whatever):
#   chmod u+x convert.sh
#   ./convert.sh foo
