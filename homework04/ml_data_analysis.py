#!/usr/bin/env python3
import sys
import json
from typing import List
import logging
import socket

format_str=f'[%(asctime)s {socket.gethostname()}] %(filename)s:%(funcName)s:%(lineno)s - %(levelname)s: %(message)s'
logging.basicConfig(level=logging.WARNING, format=format_str)


def compute_average_mass(meteorite_data: List[dict], key:str) -> float:
    """
    Iterates through a list of dictionaries, pulling out values associated with
    a given key. Returns the average of those values.

    Args:
        meteorite_data (list): A list of dictionaries, each dict should have the
                                same set of keys.
        key (string): A key that appears in each dictionary associated
                               with the desired value (will enforce float type).

    Returns:
        result (float): Average value.
    """
    
    if (len(meteorite_data) == 0):
        logging.error('a list of dicts is empty')
    total_mass = 0.
    for item in meteorite_data:
        total_mass += float(item[key])
    return ( total_mass / len(meteorite_data) )


def check_hemisphere(latitude: float, longitude: float) -> str:
    """
    Given latitude and longitude in decimal notation, returns which hemispheres
    those coordinates land in.

    Args:
        latitude (float): Latitude in decimal notation.
        longitude (float): Longitude in decimal notation.

    Returns:
        location (string): Short string listing two hemispheres.
    """
    if latitude == 0 or longitude == 0:
        #logging.error('youre not really in a hemisphere')
        raise(ValueError)
    location = 'Northern' if (latitude > 0) else 'Southern'
    location = f'{location} & Eastern' if (longitude > 0) else f'{location} & Western'
    
    return(location)

def count_hemispheres(meteorite_data: List[dict], lat_key: str, long_key: str) -> dict:
    """
    Iterates through a the list of meteorite data dictionaries and pulls out the value
    associated with a given key. Counts the number of times each value occurs in the list
    of dictionaries and returns the result.

    Args:
        meteorite_data (list): A list of dictionaries, each should have the same set of keys
        lat_key (str): the key for the latitude
        long_key (str): the key for longitude
    
    Returns:
        hemispheres_observed (dict): Dictionaru of the hemisphere counts.
    """
    hemispheres_observed = {}
    for item in meteorite_data:
        hemisphere = check_hemisphere(float(item[lat_key]), float(item[long_key]))
        if hemisphere in hemispheres_observed:
            hemispheres_observed[hemisphere] += 1
        else:
            hemispheres_observed[hemisphere] = 1
    
    return hemispheres_observed

def count_classes(meteorite_data: List[dict], key: str) -> dict:
    """
    Iterates through a list of dictionaries, and pulls out the value associated
    with a given key. Counts the number of times each value occurs in the list of
    dictionaries and returns the result.

    Args:
        meteorite_data (list): A list of dictionaries, each dict should have the
                                same set of keys.
        key (string): A key that appears in each dictionary associated
                               with the desired value.

    Returns:
        classes_observed (dict): Dictionary of class counts.

    """
    classes_observed = {}
    for item in meteorite_data:
        if item[key] in classes_observed:
            classes_observed[item[key]] += 1
        else:
            classes_observed[item[key]] = 1
    
    return(classes_observed)

def print_summary(meteorite_data: List[dict]):
    print('Summary data following meteorite analysis:\n')
    print(f'Average mass of {len(meteorite_data)} meteor(s):')
    print(f'  {compute_average_mass(meteorite_data, "mass (g)")} grams\n')
    print('Hemisphere summary data:')
    hemisphere_data = count_hemispheres(meteorite_data, 'reclat', 'reclong')
    for item in hemisphere_data:
        print(f'  There were {hemisphere_data[item]} meteors found in the {item} quadrant')
    print('\nClass summary data:')
    meteor_class_data = count_classes(meteorite_data, 'recclass')
    for item in meteor_class_data:
        print(f'  Found class {item:15s} {meteor_class_data[item]} times') 

def main():

    with open(sys.argv[1], 'r') as f:
        ml_data = json.load(f)
    
    print_summary(ml_data['meteorite_landings'])
    #print(compute_average_mass(ml_data['meteorite_landings'], 'mass (g)'))

    #for row in ml_data['meteorite_landings']:
        #print(check_hemisphere(float(row['reclat']), float(row['reclong'])))

    #print(count_classes(ml_data['meteorite_landings'], 'recclass'))
if __name__ == '__main__':
    main()
