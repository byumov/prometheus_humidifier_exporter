# Prometheus exporter for Xiaomi Smartmi Air Humidifier 2

## Run with Docker

```bash
docker run -d --name prometheus_humidifier -p 8000:8000 -e "TOKEN=xxxxxxxx" -e "IP=xx.xx.xx.xx" byumov/prometheus_humidifier
```

## Docker Hub

![Docker Pulls](https://img.shields.io/docker/pulls/byumov/prometheus_humidifier.svg)

[https://hub.docker.com/r/byumov/prometheus_humidifier](https://hub.docker.com/r/byumov/prometheus_humidifier)
