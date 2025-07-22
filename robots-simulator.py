import time
import random
import urllib.request
import urllib.error
import json

ROBOT_IDS = ["robot_1", "robot_2", "robot_3"]
INTERVAL_SEC = 1

def generate_robot_data(robot_id):
    return {
        "robot_id": robot_id,
        "state": random.choice(["idle", "active", "charging", "dead"]),
        "battery": random.uniform(30, 100),
        "battery_health": random.uniform(20, 80),
    }

def send_data():
    print("Sent data for", end=" ")
    for robot_id in ROBOT_IDS:
        telemetry = generate_robot_data(robot_id)
        json_telemetry = json.dumps(telemetry).encode("utf-8")
        req = urllib.request.Request(
            url = "http://localhost:5000/robot-metrics",
            data = json_telemetry,
            method = "POST",
            headers = {"Content-Type": "application/json"}
        )
        try:
            response = urllib.request.urlopen(req)
            print(robot_id, end=" ")
            response.close()
        except urllib.error.HTTPError as e:
            print(f"HTTP Error: {e.code} {e.reason}", end=" ")
        except urllib.error.URLError as e:
            print(f"URL Error: {e.reason}", end=" ")
    print("", flush=True)

def simulator_loop():
    print("Starting simulator... Press Ctrl+C to stop.", flush=True)
    try:
        while True:
            send_data()
            time.sleep(INTERVAL_SEC)
    except KeyboardInterrupt:
        print("Simulation stopped.", flush=True)

if __name__ == "__main__":
    simulator_loop()
