import time
import random
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# config
INFLUX_URL = "http://localhost:8086"
TOKEN = "secret-token"
ORG = "robotics"
BUCKET = "telemetry"

# settings
ROBOT_IDS = ["robot_1", "robot_2", "robot_3"]
INTERVAL_SEC = 1  # Time between data points per robot

# connection
client = InfluxDBClient(url=INFLUX_URL, token=TOKEN, org=ORG)
write_api = client.write_api(write_options=SYNCHRONOUS)

# simulates robot telemtry
def generate_robot_data(robot_id):
    return {
        "state": random.choice(["idle", "active", "charging", "dead"]),
        "battery": random.uniform(30, 100),
        "battery_health": random.uniform(20, 80),
    }

# sends robots telemetry to db
def send_data():
    print("Starting simulator... Press Ctrl+C to stop.", flush=True)
    try:
        while True:
            print("Sent data for", end=" ")
            for robot_id in ROBOT_IDS:
                telemetry = generate_robot_data(robot_id)
                point = (
                    Point("robot_metrics")
                    .tag("robot_id", robot_id)
                    .tag("state", telemetry["state"])
                    .field("battery", telemetry["battery"])
                    .field("battery_health", telemetry["battery_health"])
                    .time(time.time_ns(), WritePrecision.NS)
                )
                write_api.write(bucket=BUCKET, org=ORG, record=point)
                print(robot_id, end=" ")
            print("", flush=True)
            time.sleep(INTERVAL_SEC)
    except KeyboardInterrupt:
        print("Simulation stopped.", flush=True)
    finally:
        client.close()

if __name__ == "__main__":
    send_data()
