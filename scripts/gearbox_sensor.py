import random

def gearbox_sensor(turbine_id, rotor_speed_rpm):
    match rotor_speed_rpm:
        case 18:
            conversion_factor = 83
        case 19:
            conversion_factor = 78
        case 20:
            conversion_factor = 75
        case 21:
            conversion_factor = 76
        case 22:
            conversion_factor = 72
        case 23:
            conversion_factor = 73
        case 24:
            conversion_factor = 70
        case 25:
            conversion_factor = 72
        case _:
            return {"error": f"Rotor rotation out of range for turbine: {turbine_id}"}
    
    gearbox_speed_rpm = rotor_speed_rpm * conversion_factor
    temperature = random.uniform(60, 90) if gearbox_speed_rpm > 0 else 30
    vibration = random.uniform(0.2, 1.5) if gearbox_speed_rpm > 0 else 0.1

    return {
        "turbine_id": turbine_id,
        "gearbox_speed_rpm": round(gearbox_speed_rpm, 2),
        "temperature_celsius": round(temperature, 2),
        "vibration_mm_s": round(vibration, 2)
    }
