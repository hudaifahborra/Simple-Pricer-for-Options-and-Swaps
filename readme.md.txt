# Simple Pricer for Options and Swaps

This is a basic Python tool for pricing financial derivatives: European options using the Black-Scholes model and vanilla interest rate swaps.

## Features
- **Black-Scholes Pricer**: Calculates call and put option prices based on spot price, strike, risk-free rate, time to maturity, and volatility.
- **Vanilla Swap Pricer**: Prices a simple interest rate swap with fixed and floating legs, using a flat discount rate.

## Installation
1. Ensure Python 3.x is installed.
2. Install dependencies: `pip install -r requirements.txt`

## Usage
Run the script: `python pricer.py`

Example outputs:
- Call Price: 10.45, Put Price: 5.57
- Swap Value: 0.00 (at par)

Modify parameters in the code for custom calculations.

## Extensions
- Add Greeks for options (e.g., delta).
- Implement multi-curve discounting for swaps.
- Integrate with real market data.

## Disclaimer
This is for educational purposes only. Real trading requires advanced models and risk management.