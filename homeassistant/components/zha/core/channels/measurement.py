"""Measurement channels module for Zigbee Home Automation."""
from zigpy.zcl.clusters import measurement

from .. import registries
from ..const import (
    REPORT_CONFIG_DEFAULT,
    REPORT_CONFIG_IMMEDIATE,
    REPORT_CONFIG_MAX_INT,
    REPORT_CONFIG_MIN_INT,
)
from .base import ZigbeeChannel


@registries.ZIGBEE_CHANNEL_REGISTRY.register(measurement.FlowMeasurement.cluster_id)
class FlowMeasurement(ZigbeeChannel):
    """Flow Measurement channel."""

    REPORT_CONFIG = [{"attr": "measured_value", "config": REPORT_CONFIG_DEFAULT}]


@registries.ZIGBEE_CHANNEL_REGISTRY.register(
    measurement.IlluminanceLevelSensing.cluster_id
)
class IlluminanceLevelSensing(ZigbeeChannel):
    """Illuminance Level Sensing channel."""

    REPORT_CONFIG = [{"attr": "level_status", "config": REPORT_CONFIG_DEFAULT}]


@registries.ZIGBEE_CHANNEL_REGISTRY.register(
    measurement.IlluminanceMeasurement.cluster_id
)
class IlluminanceMeasurement(ZigbeeChannel):
    """Illuminance Measurement channel."""

    REPORT_CONFIG = [{"attr": "measured_value", "config": REPORT_CONFIG_DEFAULT}]


@registries.ZIGBEE_CHANNEL_REGISTRY.register(measurement.OccupancySensing.cluster_id)
class OccupancySensing(ZigbeeChannel):
    """Occupancy Sensing channel."""

    REPORT_CONFIG = [{"attr": "occupancy", "config": REPORT_CONFIG_IMMEDIATE}]


@registries.ZIGBEE_CHANNEL_REGISTRY.register(measurement.PressureMeasurement.cluster_id)
class PressureMeasurement(ZigbeeChannel):
    """Pressure measurement channel."""

    REPORT_CONFIG = [{"attr": "measured_value", "config": REPORT_CONFIG_DEFAULT}]


@registries.ZIGBEE_CHANNEL_REGISTRY.register(measurement.RelativeHumidity.cluster_id)
class RelativeHumidity(ZigbeeChannel):
    """Relative Humidity measurement channel."""

    REPORT_CONFIG = [
        {
            "attr": "measured_value",
            "config": (REPORT_CONFIG_MIN_INT, REPORT_CONFIG_MAX_INT, 100),
        }
    ]


@registries.ZIGBEE_CHANNEL_REGISTRY.register(measurement.SoilMoisture.cluster_id)
class SoilMoisture(ZigbeeChannel):
    """Soil Moisture measurement channel."""

    REPORT_CONFIG = [
        {
            "attr": "measured_value",
            "config": (REPORT_CONFIG_MIN_INT, REPORT_CONFIG_MAX_INT, 100),
        }
    ]


@registries.ZIGBEE_CHANNEL_REGISTRY.register(measurement.LeafWetness.cluster_id)
class LeafWetness(ZigbeeChannel):
    """Leaf Wetness measurement channel."""

    REPORT_CONFIG = [
        {
            "attr": "measured_value",
            "config": (REPORT_CONFIG_MIN_INT, REPORT_CONFIG_MAX_INT, 100),
        }
    ]


@registries.ZIGBEE_CHANNEL_REGISTRY.register(
    measurement.TemperatureMeasurement.cluster_id
)
class TemperatureMeasurement(ZigbeeChannel):
    """Temperature measurement channel."""

    REPORT_CONFIG = [
        {
            "attr": "measured_value",
            "config": (REPORT_CONFIG_MIN_INT, REPORT_CONFIG_MAX_INT, 50),
        }
    ]


@registries.ZIGBEE_CHANNEL_REGISTRY.register(
    measurement.CarbonMonoxideConcentration.cluster_id
)
class CarbonMonoxideConcentration(ZigbeeChannel):
    """Carbon Monoxide measurement channel."""

    REPORT_CONFIG = [
        {
            "attr": "measured_value",
            "config": (REPORT_CONFIG_MIN_INT, REPORT_CONFIG_MAX_INT, 0.000001),
        }
    ]


@registries.ZIGBEE_CHANNEL_REGISTRY.register(
    measurement.CarbonDioxideConcentration.cluster_id
)
class CarbonDioxideConcentration(ZigbeeChannel):
    """Carbon Dioxide measurement channel."""

    REPORT_CONFIG = [
        {
            "attr": "measured_value",
            "config": (REPORT_CONFIG_MIN_INT, REPORT_CONFIG_MAX_INT, 0.000001),
        }
    ]


@registries.ZIGBEE_CHANNEL_REGISTRY.register(measurement.PM25.cluster_id)
class PM25(ZigbeeChannel):
    """Particulate Matter 2.5 microns or less measurement channel."""

    REPORT_CONFIG = [
        {
            "attr": "measured_value",
            "config": (REPORT_CONFIG_MIN_INT, REPORT_CONFIG_MAX_INT, 0.1),
        }
    ]


@registries.ZIGBEE_CHANNEL_REGISTRY.register(
    measurement.FormaldehydeConcentration.cluster_id
)
class FormaldehydeConcentration(ZigbeeChannel):
    """Formaldehyde measurement channel."""

    REPORT_CONFIG = [
        {
            "attr": "measured_value",
            "config": (REPORT_CONFIG_MIN_INT, REPORT_CONFIG_MAX_INT, 0.000001),
        }
    ]
