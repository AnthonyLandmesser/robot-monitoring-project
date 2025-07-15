from os import environ
import time
from flask import Flask, request, jsonify
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

app = Flask(__name__)

URL = environ["INFLUXDB_URL"]
TOKEN = environ["INFLUXDB_TOKEN"]
ORG = environ["INFLUXDB_ORG"]
BUCKET = environ["INFLUXDB_BUCKET"]

client = InfluxDBClient(url=URL, token=TOKEN, org=ORG)
write_api = client.write_api(write_options=SYNCHRONOUS)

@app.route("/robot-metrics", methods=["POST"])
def robot_metrics():
    data = request.json
    try:
        point = (
            Point("robot_metrics")
            .tag("robot_id", data["robot_id"])
            .tag("state", data["state"])
            .field("battery", float(data["battery"]))
            .field("battery_health", float(data["battery_health"]))
            .time(time.time_ns(), WritePrecision.NS)
        )
        write_api.write(bucket=BUCKET, org=ORG, record=point)
        return jsonify({"status": "ok"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.teardown_appcontext
def close_influx_client(exception=None):
    write_api.close()
    client.close()