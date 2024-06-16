
# ESP32-Camera-Station


## Environment Variables

| Environment Variables | Type | Explanation | Example |
| --- | --- | --- | --- |
| CAMERASERVER_URL | str | - | http://172.16.99.32 |
| SLEEP_IN_LOOP_MS | int | - | 100 |


## Build Environment

### Install using poetry

```bash
git clone https://github.com/kevin-tofu/esp32-camera-station.git
cd esp32-camera-station
poetry add pyproject.toml
```

### Build using docker

```bash
docker build -t esp32-station .
```

## How to run

### poetry

```bash
poetry run python esp32-camera-station
```

### Docker

```bash
docker run -it -d --name mystation /
 -e "CAMERASERVER_URL=http://172.16.99.32" /
 -e "SLEEP_IN_LOOP_MS=200" /
 esp32-station
```
