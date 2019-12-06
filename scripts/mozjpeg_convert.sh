convert -resize 120x $1 TGA:- | cjpeg -quant-table 3 -optimize -outfile $2 -targa -smooth 10
ls -lS 