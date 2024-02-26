DOWNLOAD_LINK="https://www.dropbox.com/scl/fi/sscul6m1vzcixwtt6evbc/sample.mp4?rlkey=jo4i538e5i0l7hm00x3urxw3z&dl=0"
FILE_NAME="sample.mp4"

apk add --no-cache wget

cd ..

./mediamtx > output.log 2>&1 &

cd home

wget -O $FILE_NAME $DOWNLOAD_LINK

ffmpeg -re -stream_loop -1 -i $FILE_NAME -c copy -f rtsp rtsp://localhost:8554/stream