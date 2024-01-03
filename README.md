# Prometheus exporter for Xiaomi Smartmi Air Humidifier 2

Tested only with version zhimi.humidifier.ca1 / AirHumidifierCA1

![Docker Pulls](img/grafana.png)

## Get device token

Use instructions: [https://github.com/jghaanstra/com.xiaomi-miio/blob/master/docs/obtain_token.md](https://github.com/jghaanstra/com.xiaomi-miio/blob/master/docs/obtain_token.md)

Or just install patched app: [http://www.kapiba.ru/2017/11/mi-home.html](http://www.kapiba.ru/2017/11/mi-home.html)

## Run with Docker

```bash
docker run -d --name prometheus_humidifier -p 8000:8000 -e "TOKEN=xxxxxxxx" -e "IP=xx.xx.xx.xx" byumov/prometheus_humidifier
```

## Docker Hub

![Docker Pulls](https://img.shields.io/docker/pulls/byumov/prometheus_humidifier.svg) ![Docker Cloud Automated build](https://img.shields.io/docker/cloud/automated/byumov/prometheus_humidifier.svg) ![Docker Cloud Build Status](https://img.shields.io/docker/cloud/build/byumov/prometheus_humidifier.svg)

[https://hub.docker.com/r/byumov/prometheus_humidifier](https://hub.docker.com/r/byumov/prometheus_humidifier)
