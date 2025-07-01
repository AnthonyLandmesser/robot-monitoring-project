# About

This project simulates robots state and battery health telemetry and configures a grafana dashboard to analyze key preformace indicators in a visually appealing way

# Setup

You need docker, docker compose, and python installed. You also need the influxdb_client python library installed.

To run, in the repo directory run:
```bash
docker compose up -d
python robots-simulator.py
```
and then open browser to http://localhost:3000/dashboards and click on the dashboard

To turn everything off:
press ctrl c to cancel the python script and then run 
```bash
docker compose down
```