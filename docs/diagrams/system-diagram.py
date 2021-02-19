from diagrams import Cluster, Diagram
from diagrams.onprem.client import User
from diagrams.onprem.container import Docker

with Diagram("System Diagram", show=False):
    user = User("User camera")
    with Cluster("Shared network"):
        cont_ffmpeg = Docker('ffmpeg server') 
        with Cluster("Processing"):
            cont_inference = Docker('inference')
        with Cluster("App and stats"):
            cont_webapp = Docker('ui') 
            cont_mqtt = Docker('mqtt server')
            app = (
                cont_inference >> [cont_mqtt, cont_webapp]
            )   

    user >> cont_ffmpeg >> cont_inference
    

    