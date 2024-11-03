import random

def gearbox_sensor(turbine_id, rotor_speed_rpm):
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
    
    if conversion_factor is None:
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

# Exemplo de uso da função gearbox_sensor

# Defina um ID para a turbina e a velocidade do rotor em RPM
turbine_id = "Turbina_01"
rotor_speed_rpm = 20  # Exemplo de velocidade do rotor

# Chame a função gearbox_sensor
result = gearbox_sensor(turbine_id, rotor_speed_rpm)

# Exiba o resultado
print(result)
