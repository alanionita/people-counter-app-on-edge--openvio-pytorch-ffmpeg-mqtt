"""People Counter."""
"""
 Copyright (c) 2018 Intel Corporation.
 Permission is hereby granted, free of charge, to any person obtaining
 a copy of this software and associated documentation files (the
 "Software"), to deal in the Software without restriction, including
 without limitation the rights to use, copy, modify, merge, publish,
 distribute, sublicense, and/or sell copies of the Software, and to
 permit person to whom the Software is furnished to do so, subject to
 the following conditions:
 The above copyright notice and this permission notice shall be
 included in all copies or substantial portions of the Software.
 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
 MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
 LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
 OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
 WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""




import os
import sys
import time
import json
import logging as log
from inference import Network
from mqtt_service import connect_mqtt
from argparser_service import build_argparser
from processing_service import preprocessing


def infer_on_stream(args, client):
    """
    Initialize the inference network, stream video to network,
    and output stats and video.

    :param args: Command line arguments parsed by `build_argparser()`
    :param client: MQTT client
    :return: None
    """
    # Initialise the class
    infer_network = Network()
    # Set Probability threshold for detections
    # prob_threshold = args.prob_threshold

    ### Load the model through `infer_network` ###
    infer_network.load_model(args.model)
    # Get input shape
    input_shape = infer_network.get_input_shape()

    ### TODO: Handle the input stream ###

    ### TODO: Loop until stream is over ###

    ### TODO: Read from the video capture ###

    ### Pre-process the image as needed ###
    preprocessed_image = preprocessing(args.input, input_shape)
    ### Start asynchronous inference for specified request ###
    infer_network.exec_net(preprocessed_image, 0)

    ### Wait for the result ###
    # Paramater is request number not wait time
    status = infer_network.wait(0)

    ### Get the results of the inference request ###
    if status == 0:
        output_shape = infer_network.get_output(0)
        print('Inference output shape :: ', output_shape)
    ### TODO: Extract any desired stats from the results ###

    ### TODO: Calculate and send relevant information on ###
    ### current_count, total_count and duration to the MQTT server ###
    ### Topic "person": keys of "count" and "total" ###
    ### Topic "person/duration": key of "duration" ###

    ### TODO: Send the frame to the FFMPEG server ###

    ### TODO: Write an output image if `single_image_mode` ###


def main():
    """
    Load the network and parse the output.

    :return: None
    """
    # Grab command line args
    args = build_argparser().parse_args()
    # Connect to the MQTT server
    client = connect_mqtt()

    # Perform inference on the input stream
    infer_on_stream(args, client)


if __name__ == '__main__':
    main()
