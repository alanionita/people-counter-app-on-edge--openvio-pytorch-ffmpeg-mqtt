#!/usr/bin/env python3
"""
 Copyright (c) 2018 Intel Corporation.

 Permission is hereby granted, free of charge, to any person obtaining
 a copy of this software and associated documentation files (the
 "Software"), to deal in the Software without restriction, including
 without limitation the rights to use, copy, modify, merge, publish,
 distribute, sublicense, and/or sell copies of the Software, and to
 permit persons to whom the Software is furnished to do so, subject to
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

import logging as log
from openvino.inference_engine import IENetwork, IECore


class Network:
    """
    Load and configure inference plugins for the specified target devices 
    and performs synchronous and asynchronous modes for the specified infer requests.
    """

    def __init__(self):
        ### Initialize any class variables desired ###
        self.plugin = IECore()
        self.network = None
        self.exec_network = None
        self.input_blob = None
        return

    def load_model(self, model_path, device_name="CPU"):
        ### Load the model ###
        model_xml = model_path + ".xml"
        model_bin = model_path + ".bin"
        self.network = IENetwork(model=model_xml, weights=model_bin)

        ### Check for supported layers ###
        supported_layers = self.plugin.query_network(
            network=self.network, device_name=device_name)

        unsupported_layers = [
            layer for layer in self.network.layers.keys() if layer not in supported_layers]
        if len(unsupported_layers) != 0:
            print("Unsupported layers found: {}".format(unsupported_layers))
            exit(1)
        ### Return the loaded inference plugin ###
        ### Note: You may need to update the function parameters. ###
        self.exec_network = self.plugin.load_network(self.network, device_name)
        return self.plugin

    def get_input_shape(self):
        ### Return the shape of the input layer ###
        self.input_blob = next(iter(self.network.inputs))
        return self.network.inputs[self.input_blob].shape

    def exec_net(self, image, request_no):
        ### Start an asynchronous request ###
        ### Return any necessary information ###
        ### Note: You may need to update the function parameters. ###
        self.exec_network.start_async(
            request_id=request_no, inputs={self.input_blob: image})
        return 
    
    def wait(self, request_no):
        ### Wait for the request to be complete. ###
        ### Return any necessary information ###
        ### Note: You may need to update the function parameters. ###
        status = self.exec_network.requests[request_no].wait(-1)
        return status

    def get_output(self, request_no):
        # Extract and return the output results
        ### Note: You may need to update the function parameters. ###
        output_blob = next(iter(self.network.outputs))
        return self.exec_network.requests[request_no].outputs[output_blob]
