#!/usr/bin/env bash

# Source the setupvars and copy the source command to .bashrc
echo "source /opt/intel/openvino/bin/setupvars.sh" >>/root/.bashrc
source /opt/intel/openvino/bin/setupvars.sh

# Write to mp4
# python3 main.py -m $MODEL_DIR/frozen_inference_graph -i data/cars.mp4 | ffmpeg -v warning -f v4l2 -vcodec mjpeg -r 10 -pixel_format bgr24 -s 640x480 -i - out/out.mp4

python3 main.py -i data/cars.mp4 -m $MODEL_DIR/frozen_inference_graph | ffmpeg -v warning -f rawvideo -pixel_format bgr24 -video_size 768x432 -framerate 60 -i - http://ffserver:3004/fac.ffm

exec "$@"
