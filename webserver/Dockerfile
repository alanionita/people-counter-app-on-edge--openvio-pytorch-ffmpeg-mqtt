FROM node:current-alpine3.10

RUN mkdir webserver
WORKDIR /webserver
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3001
EXPOSE 3002
