<h1>Test.py</h1> 

<h2>Introduction </h2>
This is a small/toy app which queries the weather station housed on top of the Chapel Hill (NC) Public Library building. The app returns a csv file -- 'Library_weather.csv' -- containing Temperature, Rainfall, Humidity, UV Index... values recorded throughout the day in table format.
 

<h3> Using the app</h3>
The app is written in python and should run similarly to any other python script by using for instance the "$>python Test.py" command in Terminal on any Mac or Linux machine.

<h3>How to set up the dev environment</h3>
This app uses the 'requests' and 'csv' modules, which if not already installed must first be installed into your python package, using for example "$>pip install requests csv" or "$>conda install requests csv" for pip/anaconda package managers respectively. 
<br>
The app also makes a call for "test-secrets.py" a user-created json file containing the access-key and macaddress for the weather station. (These keys must be individually obtained from Chapel Hill library staff).

 <h4>License and author info<h4>
Code written by Keron Subero and falls under General Public License -- GPLv3 <https://www.gnu.org/licenses/gpl-3.0.en.html>. Any questions please search me out and send me a message on LinkedIn.
