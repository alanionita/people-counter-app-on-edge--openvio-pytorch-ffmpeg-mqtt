#!/usr/bin/env bash

cd /models
wget http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v2_coco_2018_03_29.tar.gz
tar -xvf ssd_mobilenet_v2_coco_2018_03_29.tar.gz
cd ./ssd_mobilenet_v2_coco_2018_03_29

python3 $MODEL_OP_PATH/mo.py --input_model frozen_inference_graph.pb --tensorflow_object_detection_api_pipeline_config pipeline.config --reverse_input_channels --tensorflow_use_custom_operations_config $MODEL_OP_PATH/extensions/front/tf/ssd_v2_support.json
