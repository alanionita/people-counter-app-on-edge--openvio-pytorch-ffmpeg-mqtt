FROM clearlinux/openvino

RUN mkdir inference
WORKDIR /inference
ADD ./requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ./app .
EXPOSE 3003