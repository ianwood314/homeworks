import math
import json

# returns the distance (km) between two coordinates using the great circle distance algorithm
def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float:
    lat1, lon1, lat2, lon2 = map( math.radians, [latitude_1, longitude_1, latitude_2, longitude_2] )
    d_sigma = math.acos( math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1-lon2)))
    return ( 3389.5 * d_sigma ) # radius of Mars is about 3389.5 km

# returns the time (hr) taken to travel from one location to the next
def calc_travel_time(location1: list, location2: list, rover_speed: float):  
    dist = calc_gcd( location1[0], location1[1],\
        location2[0], location2[1] ) 
    return (dist / rover_speed)

# returns the amount of time (hr) it takes to sample a meteor based on its composition
def meteor_sample_time(meteor_composition: str):
    if meteor_composition == 'stony':
        return 1.
    elif meteor_composition == 'iron':
        return 2.
    else:
        return 3.

# print the time (hr) taken to travel to the site and the time (hr) to sample the meteor to the terminal 
def print_trip(site_id: int, time_to_next_site: float, sample_time: float):
    print(f'Site #{site_id}: time to travel = {time_to_next_site:.2f} hr, time to sample = {sample_time:.2f} hr')    

# returns the amount of time it takes to travel and sample a meteor at one site
# prints to the terminal the time taken to travel to the site and the time to sample the meteor 
def simulate_site_trip(site_id: int, location1: list, location2: list, rover_speed: float, meteor_composition: str): 
    time_to_next_site = calc_travel_time(location1, location2, rover_speed) 
    sample_time = meteor_sample_time(meteor_composition)
    print_trip(site_id, time_to_next_site, sample_time)
    return (time_to_next_site + sample_time)

# prints to the terminal the total amount of time (hr) it takes the rover to travel and mine all the meteor sites
def simulate_rover_mission(starting_location: list, rover_speed: float, site_data: dict):
    total_time = 0. # the total amount of time (hr) the rover takes to complete its mission

    # calculate the time taken to travel from the starting location to the first site and to mine the site
    site_location = [ site_data[0]['latitude'], site_data[0]['longitude'] ] # location of the first meteor site
    meteor_composition = site_data[0]['composition']
    total_time += simulate_site_trip(1, starting_location, site_location, rover_speed, meteor_composition) 

    # for each site (except the last), calculate the time taken to go from one site to the next and to mine the site 
    for site_index in range( len(site_data)-1 ):
        site_location1 = [ site_data[site_index]['latitude'], site_data[site_index]['longitude'] ]
        site_location2 = [ site_data[site_index+1]['latitude'], site_data[site_index+1]['longitude'] ]
        meteor_composition = site_data[site_index+1]['composition']
        total_time += simulate_site_trip(site_index+2, site_location1, site_location2, rover_speed, meteor_composition) 
    
    print('=========================')
    print(f'Number of Sites Visted = {len(site_data)}, total mission time: {total_time:.2f} hrs') 

def main():

    with open('meteor_site_data.json', 'r') as f:
        site_data = json.load(f)
    
    starting_location = [16., 82.] # the rover's starting latitude and longitude, respectively  
    rover_speed = 10. # km / hr
    simulate_rover_mission(starting_location, rover_speed, site_data['sites'])

    return 0

if __name__ == '__main__':
    main()
