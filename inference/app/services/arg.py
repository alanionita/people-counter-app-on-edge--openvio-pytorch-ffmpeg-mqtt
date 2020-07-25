from argparse import ArgumentParser

def build_argparser():
    """
    Parse command line arguments.

    :return: command line arguments
    """
    parser = ArgumentParser()
    parser.add_argument("-m", "--model", required=True, type=str,
                        help="Path to an xml file with a trained model.")
    parser.add_argument("-i", "--input", required=True, type=str,
                        help="Path to image or video file")
    # parser.add_argument("-l", "--cpu_extension", required=False, type=str,
    #                     default=None,
    #                     help="MKLDNN (CPU)-targeted custom layers."
    #                          "Absolute path to a shared library with the"
    #                          "kernels impl.")
    # parser.add_argument("-d", "--device", type=str, default="CPU",
    #                     help="Specify the target device to infer on: "
    #                          "CPU, GPU, FPGA or MYRIAD is acceptable. Sample "
    #                          "will look for a suitable plugin for device "
    #                          "specified (CPU by default)")
    # parser.add_argument("-pt", "--prob_threshold", type=float, default=0.5,
    #                     help="Probability threshold for detections filtering"
    #                     "(0.5 by default)")
    return parser