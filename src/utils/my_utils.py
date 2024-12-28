import random

from decimal import Decimal

def random_float_with_step(start: float, end: float, step: float):
    # Convert inputs to Decimal for precision
    start_dec = Decimal(str(start))
    end_dec = Decimal(str(end))
    step_dec = Decimal(str(step))
    
    # Calculate the range in integer steps
    range_start = int(start_dec / step_dec)
    range_end = int(end_dec / step_dec)
    
    # Generate a random step and multiply by the step size
    random_step = random.randint(range_start, range_end)
    return float(random_step * step_dec)
