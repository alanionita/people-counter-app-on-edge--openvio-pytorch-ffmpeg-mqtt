FROM alpine:3.8
RUN apk add curl bash ffmpeg && \
    rm -rf /var/cache/apk/*

COPY ffserver.conf /etc/ffserver.conf
ENV FFSERVER_LOG_LEVEL "error"

ENTRYPOINT [ "ffserver" ]