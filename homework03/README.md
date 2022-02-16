# Homework03: Water Quality Analysis

## Homework Objectives
* Reinforce JSON data extraction and manipulation concepts
* Familiarize students with unit testing using `pytest`
* Introduce students to log messages in Python using the `logging` library
* Instill good documentation practices through descriptive docstrings, type hints, and detailed README files

## Homework Description
Using water sample data, calculate the average turbidity of the five most recent water sample measurements and determine if the water is safe to use.
If the water the water is not safe for use, also determine the minimum amount of time it would take (in hours) for the water to be safe to use again.

## Initial Setup
The `pytest` library must be installed in order to perform the unit testing for this homework assignment.
To check if `pytest` is already installed on your machine, type `pytest --version` in a terminal window.
If `pytest` is installed on your machine, you should see pytest followed by a version number appear on your terminal (Ex. `pytest 7.0.1`)
If you do not see this, type `pip3 install pytest` in the terminal to install `pytest`. To confirm the installation was successful, type `pytest --version`
again in your terminal.

## Scripts
This homework contains two Python scripts which are described below.
1. `water_quality.py`
    - Opens the `turbidity_data.json` file and reads in the data (note the script explicitly opens the file of that name)
    - Calculates the average turbidity (in NTUs) of the five most recent water sample measurements
      The turbidity is calculated for each measurement using the following formula:
      ```
      T = a0 * I90
      T = Turbidity in NTU Units (0 – 40)
      a0 = Calibration constant
      I90 = Ninety degree detector current
      ```
    - Uses the average turbidity to calculate the minimum amount of time (in hours) for the water quality to return below the safe threshold
      The minimum time is calculated using the following formula:
      ```
      b = log( Ts/T0 ) / log( 1-d )
      Ts = Turbidity threshold for safe water
      T0 = Current turbidity
      d = Decay factor per hour, expressed as a decimal
      b = Hours elapsed
      ```
    - Prints to the terminal the average turbidity and the minimum time (in hours) for the water quality to return below the safe threshold
2. `test_water_quality.py`
    - Performs various unit tests to ensure all of the functions in `water_quality.py` return correct mathematical answers as well as handle errors properly

## Assumptions
It was assumed for this assignment that the turbidity threshold for safe water was constant at 1.0 NTU and the decay factor per hour was also constant
at 2% (0.02 as a decimal).

## How to Run the Code
Run the following lines of code in a terminal:
1. **Download the data**
    - Type `curl https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json --output turbidity_data.json` to download the data from the web
    - Type `ls` to confirm that the file `turbidity_data.json` has now appeared in your current directory
    - Type `cat turbidity_data.json` to view the contents of the file. A sample of the result can be seen below:
      ```
      {
      "turbidity_data": [
        {
          "datetime": "2022-02-01 00:00",
          "sample_volume": 1.19,
          "calibration_constant": 1.022,
          "detector_current": 1.137,
          "analyzed_by": "C. Milligan"
        },
        {
          "datetime": "2022-02-01 01:00",
          "sample_volume": 1.15,
          "calibration_constant": 0.975,
          "detector_current": 1.141,
          "analyzed_by": "C. Milligan"
        },
        ...
      ```
2. **Execute the main script**
    - Type `./water_quality.py` to execute the script
3. **Interpret the results** <br />
  Sample output 1:
    ```
    Average turbidity based on five most recent measurements = 0.6888 NTU
    INFO:root:Water quality is safe for use. Turbidity is below the threshold.
    Minimum time required to return below a safe threshold is 0.00 hr
    ```
    The first line of the sample output provides the average turbidity of the last five water sample measurements in the dataset. From the sample output above, 
    we can see that the average turbidity was 0.6888 NTU.
    The second line provides an info message letting the user know that the water is safe for use because the the average turbidity is below the threshold.
    The last line provides the minimum amount of time for the water to return below the safe treshold. From the sample output, we can see that the minimum time
    is 0.00 hrs.
  Sample output 2:
    ```
    Average turbidity based on five most recent measurements = 1.1539 NTU
    WARNING:root:Water quality is not safe for use. Turbidity is above threshold.
    Minimum time required to return below a safe threshold is 7.08 hr
    ```
    Similar to Sample output 1, the first line of sample output 2 provides the average turbidity of the last five water sample measurements in the dataset,
    we can see is 1.139 NTU.
    The second line provides a warning message this time letting the user know the water is not safe for use because the average turbidity is above the threshold.
    The last line again provides the minimum amount of time for the water to return below the safe treshold. From the sample output, we can see that the 
    minimum time is 7.08 hrs.
