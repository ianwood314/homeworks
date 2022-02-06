# Homework02

## Assignment Objectives
* Familiarize students with common data frameworks, such as JSON
* Cultivate good writing and documentation skills through README files to ensure students can effectively communicate their project and its importance to others
* Reinforce basic programming skills in Python 

## Homework Description
Simulate a rover mission to investigate five meteor landing sites on the Martian surface. 
Use Python to generate random data for the landing sites and calculate the time it would take the rover to travel to all sites from a starting location.

## Scripts
This homework contains two Python scripts.
1. `generate_meteor_site_data.py`
    - Generates a random latitude, longitude pair for each of the five sites
    - Randomly selects one of the following meteor compositions: stony, iron, or stony-iron
    - Saves the data in a JSON file titled `meteor_site_data.json`
2. `simulate_rover_mission.py`
    - Opens the `meteor_site_data.json` file and reads in the data (note the script explicitly opens the file of that name)
    - Uses the latitude, longitude coordinate pairs in the JSON file to calculate the distance from each site to the subsequent site 
    - Uses the distance and rover speed to calculate the time taken to reach each site from the last site
    - Calculates the time taken to sample the meteor, which depends on the meteor composition
    - Prints to the terminal the amount of time it took the rover to travel from each site to the next, to sample the meteor, and the total time it took to visit and sample all the sites

## How to Run the Code
Run the following lines of code:
1. **Generate and Visualize the sample data**
`python3 generate_meteor_data.py` to execute the script
`cat meteor_site_data.json` to visualize the sample data created from the last code
2. **Run the Simulation**
`python3 simulate_rover_mission.py` to execute the script
3. Interpret the Results
**Sample Output**
```
Site #1: time to travel = 3.64 hr, time to sample = 3.00 hr
Site #2: time to travel = 5.79 hr, time to sample = 2.00 hr
Site #3: time to travel = 11.12 hr, time to sample = 2.00 hr
Site #4: time to travel = 5.16 hr, time to sample = 2.00 hr
Site #5: time to travel = 7.46 hr, time to sample = 2.00 hr
=========================
Number of Sites Visted = 5, total mission time: 44.17 hrs
```
Looking at Site #1 from the sample output, we can see it took the rover about 3.62 hours to travel from its starting location to the first site and it look 3.00 hours to sample the meteor at Site #1. Similarly, for Site #2, we can see that it took the rover 5.79 hours to travel from Site #1 to Site #2 and 2.00 hours to sample the meteor at the site. At the bottom of the sample output, we can see the total number of sites visted by the rover and the total amount of time it took the rover to travel to and sample all the sites.
