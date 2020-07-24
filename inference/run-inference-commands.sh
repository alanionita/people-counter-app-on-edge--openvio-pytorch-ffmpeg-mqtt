#!/usr/bin/env bash

# Source the setupvars and copy the source command to .bashrc
echo "source /opt/intel/openvino/bin/setupvars.sh" >>/root/.bashrc
source /opt/intel/openvino/bin/setupvars.sh

python3 main.py -m $MODEL_DIR/frozen_inference_graph -i data/cars.mp4 | ffmpeg -v warning -f rawvideo -pixel_format bgr24 -video_size 768x432 -framerate 24 -i - http://ffserver:3004/fac.ffm

exec "$@"
