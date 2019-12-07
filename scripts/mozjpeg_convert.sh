convert -resize $1x $2 TGA:- | cjpeg -quant-table 3 -optimize -outfile $3 -targa -smooth 10
ls -lS 