# Marsian Meteorite Landing Data Anaylsis

We have collected meteorite data from the Marsian surface. This homework contains scripts that analyize the average mass, location, and class of these sampled meteors. You can either use the data we have provided or use your own data.

## Homework Objective
* Familiarize students with common docker commands such as pull, build, and run
* Further develop documentation skills
* Introduce students to formatted output in Python

## Scripts
1. `ml_data_analysis.py`: Takes in the input data and prints the following to the terminal:
      - The average mass of all the meteors in the data set
      - The number of meteors found in each quandrant (Northern & Eastern, Northern & Western, Southern & Eastern, Southern & Western)
        - If a quandrant does not appear in the output, then the number of meteors found in that quadrant was zero
      - The number of meteors found belonging to each individual class
3. `test_ml_data_analysis.py`: Tests the various functions in the previous script to ensure they calculate correct values and handle errors appropriately

## How to Run the Pre-built Code
Run the following commands in a terminal:
  1. Pull the image from Docker Hub
      - `docker pull ianwood314/ml_data_analysis:hw04`
  2. Run the image using the sample data provided
      - `docker run --rm ianwood314/ml_data_analysis:hw04 ml_data_analysis.py /data/Meteorite_Landings.json`
      - Once you run the command above, you should see the following output:
        ```
        Summary data following meteorite analysis:

        Average mass of 30 meteor(s):
          83857.3 grams

        Hemisphere summary data:
          There were 21 meteors found in the Northern & Eastern quadrant
          There were 6 meteors found in the Northern & Western quadrant
          There were 3 meteors found in the Southern & Western quadrant

        Class summary data:
          Found class L5              1 times
          Found class H6              1 times
          Found class EH4             2 times
          Found class Acapulcoite     1 times
          Found class L6              6 times
          ...
        ```
## How to Build Your Own Image
  1. Download the Dockerfile
      - Either clone this repository using `git clone` (learn how to clone a repository [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository))
      - Or copy the Dockerfile contents and paste into your own Dockerflile
  2. Build the image from the Dockerfile
      - `docker build -t <username>/ml_data_analysis:<tag> .` (remember to replace with your own username and tag)
  3. Use your own data or download new input data
      - If you would like to use your own input data, it should be in a JSON file in the format shown below:
        ```
        {
          "meteorite_landings": [
            {
              "name": "Ruiz",
              "id": "10001",
              "recclass": "L5",
              "mass (g)": "21",
              "reclat": "50.775",
              "reclong": "6.08333",
              "GeoLocation": "(50.775, 6.08333)"
            },
            {
              "name": "Beeler",
              "id": "10002",
              "recclass": "H6",
              "mass (g)": "720",
              "reclat": "56.18333",
              "reclong": "10.23333",
              "GeoLocation": "(56.18333, 10.23333)"
            },
            ...
        ```
       - Additional data is also available for download using the command below: <br />
         `curl https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json --output <filename>.json` (remember to replace with a filename of your choosing)
  5. Run the containerized code using user-provided data
      - `docker run --rm -v $PWD:/data <username>/ml_data_analysis:<tag> ml_data_analysis.py /data/<filename>.json` (again, remember to replace with your own username and input data filename)

## How to Run the Test Suite with pytest
  1. Run the suite interactively
      - `docker run --rm -it ianwood314/ml_data_analysis:hw04 /bin/bash` to start an interactive shell inside the container
      - `cd /code` to change directory to where the test script is
      - Type `ls` in your terminal to make sure `test_ml_data_analysis.py` is in the `/code` directory. You should see the following:
        ```
        [root@d53048058a98 code]# ls
        ml_data_analysis.py  test_ml_data_analysis.py
        ```
      - Type `pytest` in the terminal. You should see the following output if the tests ran successfully:
        ```
        ============================== test session starts ==============================
        platform linux -- Python 3.6.8, pytest-7.0.0, pluggy-1.0.0
        rootdir: /code
        collected 4 items

        test_ml_data_analysis.py ....                                              [100%]

        ============================== 4 passed in 0.03s ================================
        ```

## Interpret the Results
**Sample Output**
```
Summary data following meteorite analysis:

Average mass of 30 meteor(s):
   83857.3 grams

Hemisphere summary data:
   There were 21 meteors found in the Northern & Eastern quadrant
   There were 6 meteors found in the Northern & Western quadrant
   There were 3 meteors found in the Southern & Western quadrant

Class summary data:
   Found class L5              1 times
   Found class H6              1 times
   Found class EH4             2 times
   Found class Acapulcoite     1 times
   Found class L6              6 times
   ...
```
From the sample output above, we can see that there are three main sections: average mass, hemisphere summary, and class summary. First, the average mass section provides the number of meteors in the data set. Underneath, it provides the average mass of those meteors in grams. For example, we can see from the sample output that 30 meteors were analyized in the sample data the average mass was 83857.3 grams. Second, the hemisphere summary section provides the number of meteors from the data set that were found in each of the four quadrants: Northern & Eastern, Northern & Western, Southern & Eastern, Southern & Western. From the sample output, we can see that there were 21 meteors found in the Northern & Eastern quadrant. Note that in the sample output, there is not a label for Southern & Eastern. This means that zero meteors were found in that quadrant. Lastly, the class summary section details the number of meteors belonging to each class. From the sample output, we can see that 6 meteors were found beloning to the L6 class.
