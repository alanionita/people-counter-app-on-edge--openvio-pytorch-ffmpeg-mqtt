# intel-facial-recognition-server

## Launching the server

Tested on Node versions 4.2.6 and 8.5.

Get node.js and NPM up and running then...

Install the Node.js dependencies (uuid4 mosca):

```shell
npm install
```

Start the server:

```shell
npm run start
```

## API Documentation

[https://scenarios.stoplight.io/amplified-by-design/specs/facial-recognition]

## MQTT

Mosca MQTT broker is automatically started on port 3001. This can be changed in the configuration file.
For testing or debugging the MQTT broker, if necessary, you can use:

- [mosquitto-clients](https://mosquitto.org/download/)
- [mqtt-spy](http://kamilfb.github.io/mqtt-spy/)

## MQTT Testing using Mosquitto

**relevant for Mac installations

### Install

Use homebrew to install the moqsquitto package

```shell
brew install mosquitto
```

#### Link

Linking the service via homebrew

```shell
brew link mosquitto
```

#### Start the service

Starting the service via homebrew

```shell
brew services start mosquitto
```

### Testing via Mosquitto

#### Prerequisite

Run the server either locally or via Docker

#### Testing

The MQTT server will be mapped on localhost port 3001

```shell
mosquitto_pub -p '3001' -t 'test' -m 'test message'
```

If everything worked well the MQTT server will respond

```shell
Client mosq-EB5ablGTw2db52lhIP connected

Published to $SYS/2FNV0t2/new/clients <- mosq-EB5ablGTw2db52lhIP

Client mosq-EB5ablGTw2db52lhIP

Published to test <- test message

Published to $SYS/2FNV0t2/disconnect/clients <- mosq-EB5ablGTw2db52lhIP
```