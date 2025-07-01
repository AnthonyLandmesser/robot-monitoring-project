# About

This project contains a way to perform camera calibration on non-standard distortion. This was developed solely by me with no hardware or equipment that was sponsored. This software is permissive open source so can/has been used in private projects. See the license for more details.

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