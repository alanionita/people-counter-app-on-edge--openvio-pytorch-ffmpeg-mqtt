FROM node:current-alpine3.10

RUN mkdir webservice && cd /webservice && mkdir server
WORKDIR /webservice/server
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3001:3001
RUN npm run start
CMD [ "node", "node-server/server.js" ]
