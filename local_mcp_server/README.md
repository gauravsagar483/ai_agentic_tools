# Local MCP Server

The `local_mcp_server` module provides a lightweight implementation of a server using the `FastMCP` framework. It allows you to define tools for various computational tasks and expose them as asynchronous endpoints. This README describes the setup and usage of the module.

## Featured Tools

Server can be added to the Claude desktop for querying with LLM
- **BMI Calculation**: Compute Body Mass Index (BMI) and determine the corresponding category.
- **Carbon Footprint Estimation**: Estimate annual CO₂ emissions based on transportation, energy usage, and dietary habits.

## Installation

Ensure you have Python 3.9+ installed. Install the required dependencies:

```bash
uv sync
source .venv/bin/activate
```

## Usage

### Initialize the Server

The server is initialized using the `FastMCP` class:

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("local mcp server")
```

### Tools

#### 1. Calculate BMI

This tool calculates the BMI based on height (in cm) and weight (in kg) and categorizes the result.

```python
@mcp.tool()
async def calculate_bmi(height_cm: float, weight_kg: float) -> dict[str, Any] | None:
    """
    Calculate Body Mass Index (BMI) based on height in centimeters and weight in kilograms.
    Returns the BMI value and the corresponding BMI category.
    """
```

**Parameters**:
- `height_cm` (float): Height in centimeters.
- `weight_kg` (float): Weight in kilograms.

**Returns**:
- A dictionary containing:
  - `bmi`: The calculated BMI value.
  - `category`: The BMI category (`Underweight`, `Normal`, `Overweight`, `Obese`).

#### 2. Calculate Carbon Footprint

This tool estimates annual CO₂ emissions based on transportation, energy usage, and diet.

```python
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
    """
```

**Parameters**:
- `daily_car_km` (float): Average kilometers driven per day by car.
- `annual_flights` (int): Number of short-haul flights taken per year.
- `monthly_kwh` (float): Average monthly electricity consumption in kilowatt-hours.
- `diet_type` (str): Dietary habit (`omnivore`, `vegetarian`, `vegan`).

**Returns**:
- A dictionary containing:
  - `car_emissions_kg`: CO₂ emissions from car usage.
  - `flight_emissions_kg`: CO₂ emissions from flights.
  - `electricity_emissions_kg`: CO₂ emissions from electricity usage.
  - `diet_emissions_kg`: CO₂ emissions from diet.
  - `total_emissions_kg`: Total annual CO₂ emissions.

## Running the Server

To start the server, define your tools and run the `FastMCP` instance:

```python
if __name__ == "__main__":
    mcp.run()
```

## Example

Here is an example of how to use the tools:

```python
# Example usage of calculate_bmi
result = await calculate_bmi(170, 70)
print(result)  # Output: {'bmi': 24.22, 'category': 'Normal'}

# Example usage of calculate_carbon_footprint
result = await calculate_carbon_footprint(ctx, 20, 2, 300, "omnivore")
print(result)
```

## License

This project is licensed under the MIT License.  