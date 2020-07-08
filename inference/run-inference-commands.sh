#!/usr/bin/env bash

# set model path
set_model_path() {
    if [ "$MODEL_PRECISION" ]; then
        MODEL_PATH=$(find $MODEL_DIR -name "$MODEL_NAME.xml" | grep $MODEL_PRECISION)
    else
        echo "MODEL_PRECISION not found"
        MODEL_PATH=$(find $MODEL_DIR -name "$MODEL_NAME.xml")
    fi

    export MODEL_PATH=${MODEL_PATH%/*}
}

set_model_path

# python3 main.py -m $MODEL_PATH/$MODEL_NAME -i data/sitting-on-car.jpg
python3 main.py -m $MODEL_PATH/intel/vehicle-attributes-recognition-barrier-0039/FP32/vehicle-attributes-recognition-barrier-0039 -i data/cars.mp4

exec "$@"
# ffmpeg -v warning -f rawvideo -pixel_format bgr24 -video_size 768x432 -framerate 24 -i - http://localhost:3004/fac.ffm
