for f in *.h264; do
	ffmpeg -r 24 -i $f $f.mp4 ;
done

