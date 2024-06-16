
# ESP32-Camera-Station


## Environment Variables

| Environment Variables | Type | Explanation | Example |
| --- | --- | --- | --- |
| CAMERASERVER_URL | str | - | http://172.16.99.32 |
| SLEEP_IN_LOOP_MS | int | - | 100 |


## Build Environment

### Install using poetry

```bash
poetry install
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
docker run --t -d esp32-station
```
