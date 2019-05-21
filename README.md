# EC-Messages

## Set up

This script was designed to work with and has only been tested against Python 3.6.  </br>

When running this script for the first time, it is recommended to create either a new virtual environment or new conda environment for the script to run in.  I recommend using the anaconda distribution of Python (https://www.anaconda.com/distribution/).  </br>

To create a new conda environment, run the following command: </br>
 <t> conda create --name (name of conda environment) python=3.6
  
I do not recommend installing the full Anaconda distribution into the newly created Conda environment as that will add a lot of libraries that are not necessary.  </br>

After conda environment is set up, change directory to where the script is unzipped: </br>
<t>  cd (path to folder where script resides)

## sample startup script

python EC-message-convert.py -p '/Users/jame9353/Box/EC19 MASINT/MASINT-Demodata/8-5/V6/obsCombined' -g 'https://wdcrealtime.esri.com:6143/geoevent/rest/receiver/ec-json-in' . 

-p is the path to the data </br>
-g is the geoevent REST Endpoint </br>
