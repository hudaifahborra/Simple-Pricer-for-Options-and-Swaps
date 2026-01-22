import numpy as np
from scipy.stats import norm

# Black-Scholes Pricer
def black_scholes(S0, K, r, T, sigma, option_type='call'):
    d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    if option_type == 'call':
        price = S0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == 'put':
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S0 * norm.cdf(-d1)
    else:
        raise ValueError("Invalid option type")
    
    return price

# Vanilla Swap Pricer (Annual payments, flat rate)
def vanilla_swap_pricer(notional, fixed_rate, floating_rate, r, T, n_payments):
    # Fixed leg: sum of discounted fixed payments
    fixed_leg = sum([notional * fixed_rate / (1 + r)**t for t in range(1, n_payments + 1)])
    
    # Floating leg: approximated as notional * (floating_rate - r) * T, but for simplicity, assume at par if floating_rate == r
    # More accurately, floating leg value is 0 if reset at current rate; here we discount floating payments
    floating_leg = sum([notional * floating_rate / (1 + r)**t for t in range(1, n_payments + 1)])
    
    swap_value = floating_leg - fixed_leg
    return swap_value

# Example Usage
if __name__ == "__main__":
    # Option Example: S0=100, K=100, r=0.05, T=1, sigma=0.2
    call_price = black_scholes(100, 100, 0.05, 1, 0.2, 'call')
    put_price = black_scholes(100, 100, 0.05, 1, 0.2, 'put')
    print(f"Call Price: {call_price:.2f}, Put Price: {put_price:.2f}")
    
    # Swap Example: Notional=1e6, Fixed=0.05, Floating=0.05, r=0.05, T=5, n=5
    swap_value = vanilla_swap_pricer(1e6, 0.05, 0.05, 0.05, 5, 5)
    print(f"Swap Value: {swap_value:.2f}")