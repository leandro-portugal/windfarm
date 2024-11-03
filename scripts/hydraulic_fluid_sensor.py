import random

def hydraulic_fluid_sensor(turbine_id,operating_time_hours):

    pressure_range = (150,300)
    temperature_range = (20, 60) 
    wear_factor = 1 + (operating_time_hours / 10000) 

    pressure = random.uniform(*pressure_range) * wear_factor
    temperature = random.uniform(*temperature_range) * wear_factor

    max_pressure = 315
    max_temperature = 80
    pressure = min(pressure, max_pressure)
    temperature = min(temperature, max_temperature)

    return {
        "turbine_id": turbine_id,
        "operating_time_hours": operating_time_hours,
        "pressure_bar": round(pressure, 2),
        "temperature_celsius": round(temperature, 2)
    }
