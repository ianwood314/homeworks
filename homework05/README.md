# Meteorite Landings Data Application

## Homework Objectives
* Create a persistant database using Redis to store the meteorite landings data
* Create a Flask application in Python to send and recieve the data stored in the database
* Query data in a dataset using a Flask application

## Description of Data
- `Meteorite_Landings.json`: file contains all of the meteorite landing sites as a list of dictionaries where each dictionary contains
information on the geographic location, mass, and class of the meteorite at the site.

## Scripts
1. `app.py`: Contains the Flask routes which the user can use to send and recieve data
    - Contains a `POST` method which loads the meteorite data into a Redis database instance
    - Contains a `GET` method which outputs the meteorite data in the terminal

## How to Build Your Own Image
Run the following commands in a terminal:
  1. Clone this repository using `git clone` (learn how to clone a repository [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository))
      - Once you've cloned the reposotory, you should see these files on your computer:
        ```
        [ianwood@isp02 homework05]$ ls
        app.py  Dockerfile  Makefile  README.md  requirements.txt
        ```
  2. Download the Meteorite Landings Dataset
      - `curl https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json --output Meteorite_Landings.json`
  3. Build the image
      - `docker build -t <your username>/meteorite-landings-data:1.0 .`, remember to replace <your username> with your `docker` username
  4. Start the Redis container
      - `docker run -d -p <your redis port number>:6379 -v $(pwd)/data:/data:rw --name=<container name>-redis redis:6 --save 1 1`
      - Example:
        ```
        [ianwood@isp02 homework05]$ docker run -d -p 6438:6379 -v $(pwd)/data:/data:rw --name=ianwood-redis redis:6 --save 1 1
        7b15893fb8663e00db6d056b36b93cd6b87c0817be2aa642056af43e013e94fd
        ```
      - From the example above, the Redis container was started with name `ianwood-redis` with ID `7b1589...`
  5. Start the Flask container
      - `docker run --name "meteorite-landings-data" -d -p <your flask port number>:5000 ianwood314/meteorite-landings-data:1.0`
      - Example:
        ```
        [ianwood@isp02 homework05]$ docker run --name "meteorite-landings-data" -d -p 5038:5000 ianwood314/meteorite-landings-data:1.0
        516d81fbe9fc3470278480fdcbd9b2d18a9d5fb0b9cbe0406b5bdc9861974bf4
        ```
      - From the example above, the Flask container has a name `meteorite-landings-data` and ID `516d81...`
  6. Find the IP Address that connects the Redis and Flask containers
      - `docker inspect <redis container id> | grep IPAddress`
      - If you forgot your redis container ID, you can run `docker ps -a | grep <redis container name>`
      - Example:
        ```
        [ianwood@isp02 homework05]$ docker ps -a | grep ianwood-redis
        7b15893fb866   redis:6                                   "docker-entrypoint.s…"   5 hours ago    Up 5 hours                0.0.0.0:6438->6379/tcp, :::6438->6379/tcp   ianwood-redis
        [ianwood@isp02 homework05]$ docker inspect 7b15893fb866 | grep IPAddress
            "SecondaryIPAddresses": null,
            "IPAddress": "172.17.0.5",
                    "IPAddress": "172.17.0.5",
        ```
      - From the output above, we can see that the IP Address that connects the Redis and Flask containers is `172.17.0.5`
  7. Navigate into `app.py` to provide the application with the IP Address we just found
      - `vim app.py` to navigate into the Python script
      - Set the `host` variable equal to the IP Address in the ``get_redis_client` function
        ```
        ...
        def get_redis_client()
            return redis.Redis(host='172.17.0.5', port=6379, db=0)
        ...
        ```
  8. You are now ready to query the data in the application

## Interpret the Results
The three types of acceptable commands to interact with this application are below:
  1. `curl localhost:<your flask port number>/data -X POST` to load the data into the Redis container
      - Example:
      ```
      [ianwood@isp02 homework05]$ curl localhost:5038/data -X POST
        -- Successfully uploaded data --
      ```
      - From the example output above, we can see that the dataset was successfully loaded into the Redis container.
  2. `curl localhost:<your flask port number>/data -X GET` to output all of the data in the dataset
      - Example:
      ```
      [ianwood@isp02 homework05]$ curl localhost:5038/data -X GET
      [
        {
          "GeoLocation": "(-33.16667, -64.95)", 
          "id": "10005", 
          "mass (g)": "780", 
          "name": "Mitchell", 
          "recclass": "L6", 
          "reclat": "-33.16667", 
          "reclong": "-64.95"
        },
        ...
        {
          "GeoLocation": "(51.78333, -1.78333)", 
          "id": "10024", 
          "mass (g)": "700", 
          "name": "Bautista", 
          "recclass": "LL5", 
          "reclat": "51.78333", 
          "reclong": "-1.78333"
        }
      ]
      ```
      - From the example output above, we can see all the entries in the dataset in JSON format
  3. `localhost:<your flask port number>/data?start=<starting index> -X GET` to query only a subset of the data in the dataset, 
      where <starting index> is the index of the data entry you would like to start at.
      - Example:
      ```
      [ianwood@isp02 homework05]$ curl localhost:5038/data?start=28 -X GET
      [
        {
          "GeoLocation": "(-31.6, -65.23333)", 
          "id": "10009", 
          "mass (g)": "1620", 
          "name": "Hachey", 
          "recclass": "L6", 
          "reclat": "-31.6", 
          "reclong": "-65.23333"
        }, 
        {
          "GeoLocation": "(51.78333, -1.78333)", 
          "id": "10024", 
          "mass (g)": "700", 
          "name": "Bautista", 
          "recclass": "LL5", 
          "reclat": "51.78333", 
          "reclong": "-1.78333"
        }
      ]
      ```
      - From the example output above, we can see the data entries in the dataset starting from index 28 to the end of the dataset.
