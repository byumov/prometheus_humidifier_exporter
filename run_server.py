from miio import airhumidifier
from prometheus_client import Gauge
import prometheus_client
import logging
import time
import argparse

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', help='IP', required=True)
    parser.add_argument('--token', help='token', required=True)
    parser.add_argument('--port', help='prometheus port', required=True)
    args = parser.parse_args()

    humidifier = airhumidifier.AirHumidifierCA1(args.ip, args.token)

    temperature = Gauge('temp', 'temp, C')
    humidity = Gauge('humidity', 'humidity')
    power = Gauge('power', 'power state')
    fan_speed = Gauge('fan_speed', 'fan speed')

    # start the server
    prometheus_client.start_http_server(int(args.port))
    log.info("Server started at port {}".format(args.port))

    # update metrics every 5 sec
    while True:
        try:
            status = humidifier.status()
        except:
            log.error("Can't get information from device")
            continue
        temperature.set(status.temperature)
        humidity.set(status.humidity)
        if status.is_on:
            power.set(1)
        else:
            power.set(0)
        fan_speed.set(status.motor_speed)
        time.sleep(5)


if __name__ == '__main__':
    main()
