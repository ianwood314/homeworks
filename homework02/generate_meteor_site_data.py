import random
import json

def generate_site_data(number_of_sites, latitude_interval, longitude_interval, composition_types):
    """
    Generates random meteor site data, like location and composotion, and returns the data as a dictionary.
    
    Args:
        number_of_sites (int): the number of meteor sites to randomly generate
        latitude_interval (list): a sorted list of two float numbers describing the lower and upper range of latitude values
        longitude_interval (list): a sorted list of two float numbers describing the lower and upper range of longitude values
        
    Returns:
        site_data (dict): contains a list of dictionaries where each dictionary contains the randmonly generated data for a meteor site
    """
    site_data = {}
    site_data['sites'] = [] 
    for site_id in range(number_of_sites):
        site_data['sites'].append( {'site_id': site_id+1, 'latitude': rand_num_between(latitude_interval),\
        'longitude': rand_num_between(longitude_interval), 'composition': random.choice(composition_types) } )        
    
    return site_data    

def rand_num_between(interval_list): 
    """
    Takes a sorted list of two floats and returns a random number between the given interval values.
    
    Arg:
        interval_list (list): a sorted list of two float numbers describing the lower and upper range of possible values
    """
    return random.uniform(interval_list[0], interval_list[1])

def main():
    """
    Generates a JSON file containing the randomly generated meteor site data using parameters given by the user, like the number of sites, 
    the range of possible latitude and logitude values, and the composition of the meteor.
    """
    number_of_sites = 5
    latitude_interval = [16., 18.]
    longitude_interval = [82., 84.]
    composition_types = ['stony','iron','stony-iron']
    
    site_data = generate_site_data(number_of_sites, latitude_interval, longitude_interval, composition_types)
    with open('meteor_site_data.json', 'w') as o:
        json.dump(site_data, o, indent=2)    

    return 0

if __name__ == '__main__':
    main()
