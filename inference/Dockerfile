FROM openvino/ubuntu18_dev as openvino-dev

USER root

# ========================
# OpenVINO DEV - VARIABLES
# ========================

# Constants
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
COPY $OPENVINO_DIR/bin/setupvars.sh /app


# ================================
# OpenVINO DEV - Pre-requisites
# ================================

# Install ffmpeg which is a cv2 dependency
RUN apt-get -y install ffmpeg

# Install Python dependencies
ARG PY_DEPS="paho-mqtt \
    opencv-python-headless"

RUN pip3 install ${PY_DEPS}

# ========================
# OpenVINO DEV - MODELS
# ========================

# Copy the file with the model definitions to the container
COPY ./models.txt /app

# Setup model-downloader and model-converter aliases
# RUN  echo "alias model-downloader='python3 ${MODEL_DL_PATH}/downloader.py'" >> ~/.bash_aliases && \
#     echo "alias model-converter='python3 ${MODEL_DL_PATH}/converter.py'" >> ~/.bash_aliases && \
#     echo ~/.bash_aliases && \
#     source ~/.bash_aliases

# Download the model
RUN python3 $MODEL_DL_PATH/downloader.py --name $MODEL_NAME -o $MODEL_DIR --precisions $MODEL_PRECISION;


# ========================
# OpenVINO DEV - VARIABLES
# ========================

# Generate the deployment package
RUN $DEPLOYMENT_MANAGER_PATH/deployment_manager.py \
    --targets cpu gpu vpu gna hddl --output_dir /tmp --archive_name openvino_deploy_package

# =====================
# OpenVINO RUNTIME
# =====================

# Move the files across to the container
COPY ./app/* /app/
COPY ./run-inference-commands.sh /app/run-inference-commands.sh

# Source all the OpenVINO variables
RUN source /app/setupvars.sh

EXPOSE 3003
ENTRYPOINT ["/bin/bash"]