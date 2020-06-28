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

python3 main.py -m $MODEL_PATH/$MODEL_NAME -i data/sitting-on-car.jpg

# model-downloader --print_all
