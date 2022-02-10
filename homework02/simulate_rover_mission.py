import math
import json

MARS_RADIUS = 3389.5 # the radius of Mars in km

def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float:
    """
    Takes the starting and ending latitude and longitude coordinate pairs and returns the distance between them using the Great-circle distance formula.
    
    Args:
        latitude_1 (float): the starting latitude
        longitude_1 (float): the starting longitude
        latitude_2 (float): the ending latitude
        longitude_2 (float):the ending longitude
    
    Returns:
         MARS_RADIUS * d_sigma (float): the distance between two coordinates
    """
    lat1, lon1, lat2, lon2 = map( math.radians, [latitude_1, longitude_1, latitude_2, longitude_2] )
    d_sigma = math.acos( math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1-lon2)))
    return ( MARS_RADIUS * d_sigma )

def calc_travel_time(location1: list, location2: list, rover_speed: float):
    """
    Calculates the amount of time it takes the rover to travel from one location to another.
    
    Args:
        location1 (list): the latitude, longitude pair of the current meteor site 
        location2 (list): the latitude, longitude pair of the next meteor site
        rover_speed (float): the speed of the rover in km/hr
    
    Returns:
        dist / rover_speed (float): the time in hours taken to travel from one location to the next
    """
    dist = calc_gcd( location1[0], location1[1],\
        location2[0], location2[1] ) 
    return (dist / rover_speed)

def meteor_sample_time(meteor_composition: str):
    """
    Takes the composition of the meteor and returns the amount of time it takes to sample that type of meteor.
    
    Args:
        meteor_composition (str): the composition type of the meteor
    
    Returns:
        The amount of time in hours it takes to sample the meteor as a type float number
    """
    if meteor_composition == 'stony':
        return 1.
    elif meteor_composition == 'iron':
        return 2.
    else:
        return 3.

# print the time (hr) taken to travel to the site and the time (hr) to sample the meteor to the terminal 
def print_trip(site_id: int, time_to_next_site: float, sample_time: float):
    print(f'Site #{site_id}: time to travel = {time_to_next_site:.2f} hr, time to sample = {sample_time:.2f} hr')    

def simulate_site_trip(site_id: int, location1: list, location2: list, rover_speed: float, meteor_composition: str):
    """
    Simulates a trip from one meteor site to the next, returns the amount of time it took the travel to and sample a meteor site.
    Also, calls function to print the terminal the time taken to travel to the site and the time to sample the meteor.
    
    Args:
        site_id (int): the site number the rover is currently at
        location1 (list): the latitude, longitude pair of the current meteor site
        location2 (list): the latitude, longitude pair of the next meteor site 
        rover_speed (float): the speed in km/hr of the rover
        meteor_composition (str): the composition of the next meteor
    
    Returns:
        time_to_next_site + sample_time (float): the amount of time it takes to travel and sample a meteor at one site
    """
    time_to_next_site = calc_travel_time(location1, location2, rover_speed) 
    sample_time = meteor_sample_time(meteor_composition)
    print_trip(site_id, time_to_next_site, sample_time)
    return (time_to_next_site + sample_time)

def simulate_rover_mission(starting_location: list, rover_speed: float, site_data: list):
    """
    Simulates the rover mission to visit and sample all meteor sites, prints to the terminal the total duration of the mission.
    
    Args:
        starting_location (list): the latitude, longitude pair for the starting location of the rover
        rover_speed (float): the speed in km/hr of the rover
        site_data (list): a list of dictionaries containing the data for all the meteor sites
    
    Returns:
       Prints to the terminal the total amount of time (hr) it takes the rover to travel and mine all the meteor sites
    """
    total_time = 0. # the total amount of time (hr) the rover takes to complete its mission

    # calculate the time taken to travel from the starting location to the first site and to sample the site
    site_location = [ site_data[0]['latitude'], site_data[0]['longitude'] ] # location of the first meteor site
    meteor_composition = site_data[0]['composition']
    total_time += simulate_site_trip(1, starting_location, site_location, rover_speed, meteor_composition) 

    # for each site (except the last), calculate the time taken to go from one site to the next and to sample the site
    for site_index in range( len(site_data)-1 ):
        site_location1 = [ site_data[site_index]['latitude'], site_data[site_index]['longitude'] ]
        site_location2 = [ site_data[site_index+1]['latitude'], site_data[site_index+1]['longitude'] ]
        meteor_composition = site_data[site_index+1]['composition']
        total_time += simulate_site_trip(site_index+2, site_location1, site_location2, rover_speed, meteor_composition) 
    
    print('=========================')
    print(f'Number of Sites Visted = {len(site_data)}, total mission time: {total_time:.2f} hrs') 

def main():
    """
    Opens and reads the meteor site data file. Initializes the starting location of the rover and its speed.
    """
    with open('meteor_site_data.json', 'r') as f:
        site_data = json.load(f)
    
    starting_location = [16., 82.] # the rover's starting latitude and longitude, respectively  
    rover_speed = 10. # km/hr
    simulate_rover_mission(starting_location, rover_speed, site_data['sites'])

    return 0

if __name__ == '__main__':
    main()
