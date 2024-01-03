FROM python:3.11-alpine AS build
RUN apk add --update --no-cache gcc musl-dev libffi-dev openssl-dev
COPY . /app/
WORKDIR /app
RUN pip install .

FROM python:3.11-alpine
COPY --from=build /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/
COPY --from=build /usr/local/bin/prometheus_humidifier_exporter /usr/local/bin/
CMD prometheus_humidifier_exporter --ip $IP --port 8000 --token $TOKEN
