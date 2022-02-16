#!/usr/bin/env python3

import json
import math
import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)

TURBIDITY_THRESHOLD = 1.0 # NTU
DECAY_FACTOR = 0.02 # decay factor per hour

def time_to_safe_threshold(current_turbidity: float) -> float:
    """
    Takes the current turbidity as an input, returns the minimum amount of time (in hours) required to reach 
    the safe threshold based on an exponential decay model.
 
    Args:
        current_turbidity (float): the current turbidity of the water, taken the average turbidity of the water samples   
 
    Returns:
        min_time (float): the minimum amount of time required to reach the sage threshold 
    """
    if current_turbidity < 0:
        raise ValueError('Current turbidity less than zero.')
    elif current_turbidity == 0:
        raise ValueError('Current turbidity equal to 0')
    
    min_time = 0.
    
    if TURBIDITY_THRESHOLD > current_turbidity:
        logging.info('Water quality is safe for use. Turbidity is below the threshold.')
    else:
        logging.warning('Water quality is not safe for use. Turbidity is above threshold.')
        min_time = math.log(TURBIDITY_THRESHOLD / current_turbidity) / math.log(1 - DECAY_FACTOR) 

    return min_time
    
def calc_avg_turbidity(water_data: List[dict], calibration_const_key: str, detector_current_key: str) -> float:
    """
    Takes water sample data as an input, returns the current water turbidity (in NTUs) as the average turbidity 
    of the water samples.
    
    Args:
        water_data (List[dict]): the water sample data 
        calibration_const_key (str): the dictionary key for the calibration constant
        detector_current_key (str): the dictionary key for the detector current
    
    Returns:
        turbidity_sum / len(water_data) (float): the average turbidity of the water samples
    """
    turbidity_sum = 0.
    
    for water_sample in water_data:
        turbidity_sum += water_sample[calibration_const_key] * water_sample[detector_current_key]

    return ( turbidity_sum / len(water_data) )
    
def main():
    
    with open('turbidity_data.json', 'r') as f:
        water_data = json.load(f)
        
    current_turbidity = calc_avg_turbidity(water_data['turbidity_data'][-5:], 'calibration_constant', 'detector_current')
    print(f'Average turbidity based on five most recent measurements = {current_turbidity:.4f} NTU')
    min_time = time_to_safe_threshold(current_turbidity)
    print(f'Minimum time required to return below a safe threshold is {min_time:.2f} hr')   
 
if __name__ == '__main__':
    main()
