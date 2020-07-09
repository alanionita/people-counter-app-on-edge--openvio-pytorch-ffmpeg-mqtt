FROM openvino/ubuntu18_dev as openvino-dev

USER root

# ========================
# OpenVINO DEV - VARIABLES
# ========================

# Constants
ARG INSTALL_DIR=/opt/intel/openvino

ENV OPENVINO_DIR="/opt/intel/openvino"
ENV MODEL_OP_PATH="/usr/share/openvino/model-optimizer/mo.py"
ENV MODEL_DL_PATH="/opt/intel/openvino/deployment_tools/tools/model_downloader"
ENV DEPLOYMENT_MANAGER_PATH="/opt/intel/openvino/deployment_tools/tools/deployment_manager"
ENV MODEL_DIR="/models"

# Variables
ENV MODEL_NAME="vehicle-attributes-recognition-barrier-0039"
ENV MODEL_PRECISION="FP32"

# set the working directory to /app
WORKDIR /app

# ================================
# OpenVINO DEV - Pre-requisites
# ================================

# Install ffmpeg which is a cv2 dependency
RUN apt-get -y install ffmpeg
COPY ./requirements.txt ./requirements.txt
RUN pip3 install -r ./requirements.txt

# ========================
# OpenVINO DEV - MODELS
# ========================

# Copy the file with the model definitions to the container
COPY ./models.txt /app

# Download the model
RUN python3 $MODEL_DL_PATH/downloader.py --name $MODEL_NAME -o $MODEL_DIR --precisions $MODEL_PRECISION;


# ========================
# OpenVINO APP - Setup
# ========================

# Move the files across to the container
COPY ./app/* /app/
COPY ./run-inference-commands.sh /app/run-inference-commands.sh

# Expose the port
EXPOSE 3003

# Usign CMD instead of Entrypoint seems to fix issues with env variables not
# being usable within the container

CMD ["/bin/bash"]