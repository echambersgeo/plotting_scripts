#!/usr/bin/env python
# #encoding: utf-8
#-------------------------------------------------------------
# - How to use this script. 
# - This script is used to select and plot seismograms with user input. In multiple places all can be used or multiple inputs 
# - can be input such as stations or channels.
# - Due to different naming conventions in directory structures the use of for loops is required so as not to break.
# - Run by activating a python 3 environment and obspy e.g. conda actiavte OBS_toolbox_conda.
# - Then type python plotting_events_script.py
#########
# - SCRIPT STILL IN PROGRESS. ONCE WORKS REMOVE REDUNDANT COMMENT LINES!!!!
#########
#------------------------------------------------------------------------------------#
# - Import the useful packages #------------------------------------------------------------------------------------#
import obspy
import os
from obspy.core import read

dataarea=input("Select data area e.g. /mnt/seismodata/EC/DOWNLOAD_DATA/local/IA/old_way/data/ : ")
identifier=input("Select filename identifier e.g. old_way :")
figuresave="/mnt/home_geo/echambers/Documents/Figures/"

year=int(input("Input year (4 digits): "))
month=input("Input month (2 digits): ")
network=input("Input network (e.g. IA): ")

#echo the options for events in the month folder
print(os.listdir(f"{dataarea}/{year}/{month}/"))
event=input("Select event from list above: ")

##echo the options for stations 
allstations=[]
for stationfront in os.listdir(f"{dataarea}/{year}/{month}/{event}/"):

    if os.path.isdir(f"{dataarea}/{year}/{month}/{event}/{stationfront}/"):
        #print(subdir)
        #print(os.listdir(f"{dataarea}/{year}/{month}/{event}/{stationfront}/"))
        allstations+=os.listdir(f"{dataarea}/{year}/{month}/{event}/{stationfront}/")
print(allstations)        
#print(os.path.isdir(f"{dataarea}/{year}/{month}/{event}/"))
#stationfront=input("Select station start from list above: ").split()

#print(os.listdir(f"{dataarea}/{year}/{month}/{event}/{subdir[0].lower()}/"))
#os.listdir(dataarea/year/month/event/*/* )
stations=input("Select station from list above or specify all: ").split()
if stations == ["all"]:
    stations=allstations

    
for station in stations:
    stationfront=station.split(".")[1][0]
    ##echo the available channels
    #print(os.listdir(f"{dataarea}/{year}/{month}/{event}/{network[0].lower()}/{station}/"))
    
    #os.listdir(dataarea/year/month/event/net lower case first letter only/net+station lower case/* )
    #channels=input("Select channels from list above. Multiple can be chosen separated by space: ").split()
    if network=="IA":
        channels=["hhe", "hhn", "hhz", "dz"]
    else:
        channels=["bhe", "bhn", "bhz", "dz"]

    #channels= 1 2 3
    #def function(*args):
    #    print args
    #function(1, 2, 3)
    for channel in channels:
        if channel[0] == 'd':
            filename = f"{station.split('.')[1].lower()}.{channel}"
        elif network=="IA": 
            filename = f"{event}.{station.split('.')[1].lower()}.{channel}"
        else:
            filename = f"{event}_{station.split('.')[1].lower()}.{channel}"
        eventfile = read(f"{dataarea}/{year}/{month}/{event}/{stationfront}/{station}/{filename}")
        print(eventfile)

        eventfile.plot(outfile=f"{figuresave}{identifier}.{event}.{station.split('.')[1].lower()}.{channel}.png")
    #test = read('$dataarea/2018/05/180509_032326/i/ia.ia001/180509_032326.ia001.hhz')
    ##test.plot(size=(800, 200))
    #test.plot(outfile='/mnt/home_geo/echambers/Documents/Figures/180509_032326.ia001.hhz.png')
    ##print(test)
    #test2 = read('/mnt/seismodata/EC/DOWNLOAD_DATA/local/IA/old_way/data/2018/05/180509_032326/i/ia.ia001/ia001.dz')
    ##test2.plot(size=(800, 200))
    #test2.plot(outfile='/mnt/home_geo/echambers/Documents/Figures/180509_032326.ia001.dz.png')

