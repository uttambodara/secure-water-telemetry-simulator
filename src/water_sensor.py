import random
from datetime import datetime, timezone


class WaterSensor:
    """
    Simulates a Hydroficient HYDROLOGIC water sensor.

    Generates realistic pressure and flow readings, including
    controlled anomalies, for testing IoT pipelines and
    security detection logic.
    """

    def __init__(self, device_id):
        # Unique identifier for the physical device
        self.device_id = device_id

        # Monotonically increasing counter used to detect replay attacks
        self.counter = 0

        # Baseline values used to create realistic variation
        self.base_pressure_up = 82.0
        self.base_pressure_down = 76.0
        self.base_flow = 40.0

    def get_reading(self):
        """
        Generate a normal sensor reading.

        - Increments a sequence counter
        - Uses UTC timestamps (ISO 8601) for cross-region consistency
        - Adds small random variation to simulate real sensors
        """
        self.counter += 1

        return {
            "device_id": self.device_id,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "counter": self.counter,
            "pressure_upstream": round(self.base_pressure_up + random.uniform(-2, 2), 1),
            "pressure_downstream": round(self.base_pressure_down + random.uniform(-2, 2), 1),
            "flow_rate": round(self.base_flow + random.uniform(-3, 3), 1),
        }

    def get_leak_reading(self):
        """
        Simulate a leak condition.

        Characterized by abnormally high flow rate while
        pressures remain within expected ranges.
        """
        reading = self.get_reading()
        reading["flow_rate"] = round(random.uniform(80, 120), 1)
        return reading

    def get_blockage_reading(self):
        """
        Simulate a pipe blockage.

        Blockages cause high upstream pressure and
        significantly reduced downstream pressure.
        """
        reading = self.get_reading()
        reading["pressure_upstream"] = round(random.uniform(85, 95), 1)
        reading["pressure_downstream"] = round(random.uniform(30, 50), 1)
        return reading

    def get_stuck_reading(self):
        """
        Simulate a malfunctioning (stuck) sensor.

        All reported values remain constant across readings,
        indicating a failed or frozen sensor.
        """
        reading = self.get_reading()
        stuck_value = 82.0
        reading["pressure_upstream"] = stuck_value
        reading["pressure_downstream"] = stuck_value
        reading["flow_rate"] = stuck_value
        return reading
