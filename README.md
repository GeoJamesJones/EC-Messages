# EC-Messages

## Set up Python Environment

This script was designed to work with and has only been tested against Python 3.6.  </br>

When running this script for the first time, it is recommended to create either a new virtual environment or new conda environment for the script to run in.  I recommend using the anaconda distribution of Python (https://www.anaconda.com/distribution/).  </br>

To create a new conda environment, run the following command: </br>
- conda create --name (name of conda environment) python=3.6
  
I do not recommend installing the full Anaconda distribution into the newly created Conda environment as that will add a lot of libraries that are not necessary.  </br>

After conda environment is set up, change directory to where the script is unzipped: </br>
- cd (path to folder where script resides)
    
Once in the directory where the script was installed, run the following command:</br>
- pip install -r requirements.txt
    
## Set up GeoEvent Server

Go to your GeoEvent manager, then procede to Site - Configuration Store - Import Configuration.  </br>

When the window opens up, add the XML file located in the GeoEvent Files folder in the directory where the script was unzipped.  </br>
- (Directory where script was unzipped)\GeoEvent Files </br>

This should add: </br>
- Input:  ec-json-in </br>
- Output: ec-fs-out </br>
- GeoEvent Service: ENTERPRISE CHALLENGE </br>

## sample startup script

After getting the python installed and configured, run the following command:  </br>

python EC-message-convert.py -p (path to where data will either be added or currently resides) -g (GeoEvent REST Endpoint) 

-p is the path to the data </br>
-g is the geoevent REST Endpoint, this can be found in the input from the Set up GeoEvent server section. </br>
