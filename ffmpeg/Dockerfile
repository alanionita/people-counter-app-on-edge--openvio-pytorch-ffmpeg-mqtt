FROM vimagick/ffmpeg

RUN mkdir ffserver
WORKDIR /ffserver

COPY . .

EXPOSE 3004

CMD ["ffserver -d -f server.conf & "]