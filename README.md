# Prometheus exporter for Xiaomi Smartmi Air Humidifier 2


## Run with Docker
```bash
docker run -d --name prometheus_humidifier -p 8000:8000 -e "TOKEN=xxxxxxxx" -e "IP=xx.xx.xx.xx" byumov/prometheus_humidifier
```
