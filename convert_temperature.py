def convert_temperature(temp, unit):
    """Convert temperature between Celsius, Fahrenheit, and Kelvin."""
    try:
        temp = float(temp)
    except ValueError:
        return "Please enter a valid number for the temperature."
    
    unit = unit.upper()
    if unit == 'C':
        fahrenheit = (temp * 9/5) + 32
        kelvin = temp + 273.15
        return f"{temp}°C is equivalent to {fahrenheit}°F and {kelvin}K"
    elif unit == 'F':
        celsius = (temp - 32) * 5/9
        kelvin = celsius + 273.15
        return f"{temp}°F is equivalent to {celsius}°C and {kelvin}K"
    elif unit == 'K':
        celsius = temp - 273.15
        fahrenheit = (celsius * 9/5) + 32
        return f"{temp}K is equivalent to {celsius}°C and {fahrenheit}°F"
    else:
        return "Unrecognized unit. Please use 'C' for Celsius, 'F' for Fahrenheit, or 'K' for Kelvin."

# Solicitando entrada del usuario
temp_input = input("Enter the temperature (e.g., 25C, 77F, 298K): ")
temp_value, unit = temp_input[:-1], temp_input[-1]

# Llamando a la función y mostrando el resultado
result = convert_temperature(temp_value, unit)
print(result)
