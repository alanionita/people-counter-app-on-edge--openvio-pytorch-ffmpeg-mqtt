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
            print("Check whether extensions are available to add to IECore.")
            exit(1)

        ### Add any necessary extensions [optional since OpenVINO v.2020] ###

        ### Return the loaded inference plugin ###
        ### Note: You may need to update the function parameters. ###
        self.exec_network = self.plugin.load_network(self.network, device_name)
        return self.plugin

    def get_input_shape(self):
        ### Return the shape of the input layer ###
        input_blob = next(iter(self.network.inputs))
        return self.network.inputs[input_blob].shape

    def exec_net(self, image):
        ### Start an asynchronous request ###
        ### Return any necessary information ###
        ### Note: You may need to update the function parameters. ###
        input_blob = next(iter(self.network.inputs))
        infer_request_handle = self.exec_network.start_async(
            request_id=0, inputs={input_blob: image})
        infer_status = infer_request_handle.wait()
        print('Infer status :: ', infer_status)
        while infer_status:
            status = self.exec_network.requests[0].wait(-1)
            if status == 0:
                break
            else:
                status.sleep(1)
        return self.exec_network    

    def wait(self):
        ### TODO: Wait for the request to be complete. ###
        ### TODO: Return any necessary information ###
        ### Note: You may need to update the function parameters. ###
        return

    def get_output(self):
        # TODO: Extract and return the output results
        ### Note: You may need to update the function parameters. ###
        return
