FROM clearlinux/openvino

# Move the files across to the container
RUN mkdir inference
WORKDIR /inference
ADD ./requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ./wait-for-it.sh wait-for-it.sh
COPY ./app .

# Expose port    
EXPOSE 3003