import random
import json

def generate_site_data(number_of_sites, latitude_interval, longitude_interval, composition_types):
    site_data = {}
    site_data['sites'] = [] 
    for site_id in range(number_of_sites):
        site_data['sites'].append( {'site_id': site_id+1, 'latitude': rand_num_between(latitude_interval),\
        'longitude': rand_num_between(longitude_interval), 'composition': random.choice(composition_types) } )        
    
    return site_data    

def rand_num_between(interval_list): # returns a random float between the given interval values
    return random.uniform(interval_list[0], interval_list[1])

def main():
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
