FROM node:current-alpine3.10

RUN mkdir webui
WORKDIR /webui
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000:3000
