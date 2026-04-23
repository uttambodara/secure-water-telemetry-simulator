# Mock IoT Water Sensor & Telemetry Dataset

This project simulates a realistic IoT water sensor used in smart infrastructure environments. It generates time-series telemetry data with built-in security considerations, including replay-attack detection and anomaly testing.

## What This Project Does

- Simulates a HYDROLOGIC-style water sensor
- Generates realistic pressure and flow telemetry
- Uses ISO 8601 UTC timestamps for global consistency
- Implements monotonically increasing counters for replay detection
- Injects realistic anomalies (leaks, blockages, stuck sensors)
- Exports data in JSON format for downstream analysis

## Why This Matters for Security

IoT security depends on understanding how real devices behave — not just how they should behave.

This project was designed to:
- Model how unsecured telemetry can be spoofed or replayed
- Provide realistic data for anomaly detection testing
- Prepare sensor output for live MQTT pipelines and attack simulation

## Files

- `src/water_sensor.py` — Mock IoT sensor implementation
- `sensor_data.json` — Generated telemetry dataset (100 readings)

## Next Phase

This dataset is used in a follow-up project to publish telemetry over an intentionally insecure MQTT pipeline, observe attacks in real time, then implement proper defenses.

