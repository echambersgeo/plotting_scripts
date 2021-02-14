#!/usr/bin/env python
# #encoding: utf-8
#-------------------------------------------------------------
# - How to use this script. 
# - This script is used to plot an individual seismogram when you directly specify it's location within the script.
# - Run by activating a python 3 environment and obspy e.g. conda actiavte OBS_toolbox_conda.
# - Then type python plotting_events_script_single.py

#------------------------------------------------------------------------------------#
# - Import the useful packages #------------------------------------------------------------------------------------#
import obspy
import os
from obspy.core import read


dataarea="/mnt/seismodata/EC/DOWNLOAD_DATA/local/IA/old_way/data"
year="2018"
month="05"
network="IA"
station="ia001"
stationall=f"{network.lower()}.{station}"
event="180509_032326"
channel="hhz"
test = read(f'{dataarea}/{year}/{month}/{event}/i/{stationall}/{event}.{station}.{channel}')
test.plot(outfile=f'/mnt/home_geo/echambers/Documents/Figures/{event}.{station}.{channel}.png')
