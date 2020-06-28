FROM clearlinux/openvino

# Move the files across to the container
ADD ./requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Expose port    
EXPOSE 3003