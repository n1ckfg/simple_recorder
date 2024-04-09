for f in *.h264; do
	ffmpeg -r 24 -i $f -c copy $f.mp4 ;
done

