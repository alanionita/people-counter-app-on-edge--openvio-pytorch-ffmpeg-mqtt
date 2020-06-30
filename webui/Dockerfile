FROM node:12-stretch-slim

RUN mkdir webui
WORKDIR /webui
COPY package*.json ./
RUN npm install
COPY . .

EXPOSE 3000