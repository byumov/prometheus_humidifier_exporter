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

    temperature = Gauge('humidifier_temp', 'temp, C')
    humidity = Gauge('humidifier_humidity', 'humidity')
    power = Gauge('humidifier_power', 'power state')
    fan_speed = Gauge('humidifier_fan_speed', 'fan speed')
    water_level = Gauge('humidifier_water_level', 'water level %')

    # start the server
    prometheus_client.start_http_server(int(args.port))
    log.info("Server started at port {}".format(args.port))

    # update metrics every 5 sec
    while True:
        try:
            status = humidifier.status()
            # <AirHumidiferStatus 
            # power=on, 
            # mode=OperationMode.Auto, 
            # temperature=22.9, 
            # humidity=39%, 
            # led_brightness=LedBrightness.Dim, 
            # buzzer=False, 
            # child_lock=False, 
            # target_humidity=70%, 
            # trans_level=None, 
            # motor_speed=844, 
            # depth=125, 
            # dry=True, 
            # use_time=24011819, 
            # hardware_version=0001, 
            # button_pressed=None, 
            # strong_mode_enabled=False, 
            # firmware_version_major=2.1.0, 
            # firmware_version_minor=0>
        except Exception as err:
            log.error("Can't get information from device, check token or network: %s", err)
            time.sleep(5)
            continue
        water_level.set(status.depth)
        temperature.set(status.temperature)
        humidity.set(status.humidity)
        if status.is_on:
            power.set(1)
        else:
            power.set(0)
        fan_speed.set(status.motor_speed)
        time.sleep(15)


if __name__ == '__main__':
    main()
