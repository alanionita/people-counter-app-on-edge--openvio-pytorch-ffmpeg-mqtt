FROM clearlinux/openvino

# Move the files across to the container
ADD ./requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY ./app/* /app/
COPY ./run-inference-commands.sh /app/run-inference-commands.sh
# Expose port    
EXPOSE 3003