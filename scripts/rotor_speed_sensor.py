import random

def rotor_sensor(turbine_id, wind_speed_kmh):
    
    if wind_speed_kmh < 10:
        rotor_speed_rpm = 0
        status_brakes = "Inactive"
    elif wind_speed_kmh >= 10 and wind_speed_kmh < 20:
        rotor_speed_rpm = 18
        status_brakes = "Inactive"
    elif wind_speed_kmh >= 20 and wind_speed_kmh < 30:
        rotor_speed_rpm = 19
        status_brakes = "Inactive"
    elif wind_speed_kmh >= 30 and wind_speed_kmh < 40:
        rotor_speed_rpm = 20
        status_brakes = "Inactive"
    elif wind_speed_kmh >= 40 and wind_speed_kmh < 50:
        rotor_speed_rpm = 21
        status_brakes = "Inactive"
    elif wind_speed_kmh >= 50 and wind_speed_kmh < 60:
        rotor_speed_rpm = 22
        status_brakes = "Inactive"
    elif wind_speed_kmh >= 60 and wind_speed_kmh < 70:
        rotor_speed_rpm = 23
        status_brakes = "Inactive"
    elif wind_speed_kmh >= 70 and wind_speed_kmh < 80:
        rotor_speed_rpm = 24
        status_brakes = "Inactive"
    elif wind_speed_kmh >= 80 and wind_speed_kmh <= 90:
        rotor_speed_rpm = 25
        status_brakes = "Inactive"
    else:
        rotor_speed_rpm =0
        status_brakes = "Active"


    return {
        "turbine_id": turbine_id,
        "rotor_speed_rpm": round(rotor_speed_rpm, 2),
        "wind_speed_kmh": wind_speed_kmh,
        "status_brakes": status_brakes
    }
