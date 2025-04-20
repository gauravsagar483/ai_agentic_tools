from typing import Any
from mcp.server.fastmcp import FastMCP, Context


# Initialize FastMCP server
mcp = FastMCP("local mcp server")


@mcp.tool()
async def calculate_bmi(height_cm: float, weight_kg: float) -> dict[str, Any] | None:
    """
    Calculate Body Mass Index (BMI) based on height in centimeters and weight in kilograms.
    Returns the BMI value and the corresponding BMI category.
    """
    if height_cm <= 0 or weight_kg <= 0:
        raise ValueError("Height and weight must be positive numbers.")

    height_m = height_cm / 100  # Convert height to meters
    bmi = weight_kg / (height_m ** 2)
    bmi_rounded = round(bmi, 2)

    # Determine BMI category
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return {
        "bmi": bmi_rounded,
        "category": category
    }



@mcp.tool()
async def calculate_carbon_footprint(
    ctx: Context,
    daily_car_km: float,
    annual_flights: int,
    monthly_kwh: float,
    diet_type: str
) -> dict:
    """
    Estimate annual CO₂ emissions based on transportation, energy usage, and diet.
    
    Parameters:
    - daily_car_km: Average kilometers driven per day by car.
    - annual_flights: Number of short-haul flights taken per year.
    - monthly_kwh: Average monthly electricity consumption in kilowatt-hours.
    - diet_type: Dietary habit ('omnivore', 'vegetarian', 'vegan').
    
    Returns:
    - Dictionary containing CO₂ emissions from each category and the total.
    """
    # Emission factors
    CAR_EMISSION_FACTOR = 0.170  # kg CO₂ per km (average petrol car)
    FLIGHT_EMISSION = 250.0      # kg CO₂ per short-haul flight
    ELECTRICITY_EMISSION_FACTOR = 0.475  # kg CO₂ per kWh (global average)

    # Diet emission factors (kg CO₂ per year)
    DIET_EMISSIONS = {
        "omnivore": 2200.0,
        "vegetarian": 1700.0,
        "vegan": 1500.0
    }

    # Calculate emissions
    car_emissions = daily_car_km * 365 * CAR_EMISSION_FACTOR
    flight_emissions = annual_flights * FLIGHT_EMISSION
    electricity_emissions = monthly_kwh * 12 * ELECTRICITY_EMISSION_FACTOR
    diet_emissions = DIET_EMISSIONS.get(diet_type.lower(), 1700.0)  # Default to vegetarian if unknown

    total_emissions = car_emissions + flight_emissions + electricity_emissions + diet_emissions

    return {
        "car_emissions_kg": round(car_emissions, 2),
        "flight_emissions_kg": round(flight_emissions, 2),
        "electricity_emissions_kg": round(electricity_emissions, 2),
        "diet_emissions_kg": round(diet_emissions, 2),
        "total_emissions_kg": round(total_emissions, 2)
    }

