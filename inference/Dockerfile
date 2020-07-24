FROM openvino/ubuntu18_dev as dev

USER root

# ========================
# OpenVINO - DEV 
# ========================

# Define vars
ARG MODEL_OP_PATH="/opt/intel/openvino/deployment_tools/model_optimizer"
ARG MODEL_DL_PATH="/opt/intel/openvino/deployment_tools/tools/model_downloader"
ARG DEPLOYMENT_MANAGER_PATH="/opt/intel/openvino/deployment_tools/tools/deployment_manager"

# OpenVINO - Dev / Model Downloader

# ENV MODEL_NAME="vehicle-attributes-recognition-barrier-0039"
# ENV MODEL_PRECISION="FP32"

# Copy the file with the model definitions to the container
# COPY ./models.txt /app

# Download the model
# RUN python3 $MODEL_DL_PATH/downloader.py --name $MODEL_NAME -o $MODEL_DIR --precisions $MODEL_PRECISION;

# Model Optimiser
WORKDIR /models
COPY ./models/* ./

# **** Downloaded the model separately using `wget http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v2_coco_2018_03_29.tar.gz`

RUN apt-get -y update && \ 
    tar -xvf ssd_mobilenet_v2_coco_2018_03_29.tar.gz && \
    python3 $MODEL_OP_PATH/mo.py \
    --input_model \
    ./ssd_mobilenet_v2_coco_2018_03_29/frozen_inference_graph.pb --tensorflow_object_detection_api_pipeline_config \
    ./ssd_mobilenet_v2_coco_2018_03_29/pipeline.config \
    --reverse_input_channels \
    --tensorflow_use_custom_operations_config \
    $MODEL_OP_PATH/extensions/front/tf/ssd_v2_support.json

# ================================
# OpenVINO - Runtime
# ================================

FROM openvino/ubuntu18_runtime as runtime

# Set user
USER root

# Set workdir and create a /models dir
WORKDIR /app
RUN mkdir models

# Env vars
ENV OPENVINO_DIR="/opt/intel/openvino"
ENV MODEL_DIR="/app/models"

# Move optimised model from developement
COPY --from=dev /models/* ./models/

# Move the files to the container
COPY ./requirements.txt ./requirements.txt
COPY ./app/* /app/
COPY ./run-inference-commands.sh /app/run-inference-commands.sh

# Install dependencies
RUN apt-get -y update && \
    apt-get -y install ffmpeg && \
    pip3 install wheel && \
    pip3 install -r ./requirements.txt

# Expose the port
EXPOSE 3003

# Usign CMD instead of Entrypoint seems to fix issues with env variables not
# being usable within the container

CMD ["/bin/bash"]