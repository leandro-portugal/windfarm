import random

def gearbox_sensor(turbine_id, rotor_speed_rpm,operating_time_hours):
    conversion_factors = {
        18: 83.333,
        19: 81.578,
        20: 80.000,
        21: 78.571,
        22: 77.272,
        23: 76.086,
        24: 75.000,
        25: 74.000
    }

    conversion_factor = conversion_factors.get(rotor_speed_rpm)
    wear_factor = 1 + (operating_time_hours / 10000)
    
    if conversion_factor is None:
        return {"error": f"Rotor rotation out of range for turbine: {turbine_id}"}
    
    gearbox_speed_rpm = rotor_speed_rpm * conversion_factor
    temperature = random.uniform(60, 90)  * wear_factor if gearbox_speed_rpm > 0 else 30
    vibration = random.uniform(0.2, 1.5)  * wear_factor if gearbox_speed_rpm > 0 else 0.1

    temperature = max(temperature, 60)
    vibration = max(vibration, 0.2)

    return {
        "turbine_id": turbine_id,
        "gearbox_speed_rpm": round(gearbox_speed_rpm, 2),
        "temperature_celsius": round(temperature, 2),
        "vibration_mm_s": round(vibration, 2)
    }
