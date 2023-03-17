# 5G Network Slicing for Wi-Fi Networks

This code package is related to the paper:

M. Nerini and D. Palma, "[5G Network Slicing for Wi-Fi Networks](https://ieeexplore.ieee.org/document/9463988)," 2021 IFIP/IEEE International Symposium on Integrated Network Management (IM), 2021, pp. 633-637.

## Introduction

This project aims to provide a framework to develop and evaluate network slicing techniques for Wi-Fi networks. We provide a customizable Wi-Fi indoor scenario, realized with the *ns-3* network simulator, in which several mobile Stations (STAs) are connected to an Access Point (AP) placed in the centre of a room. In general, the STAs have distinct performance requirements, and are grouped in different networks slices (e.g. eMBB, mMTC and URLLC).

On top of this scenario, we facilitate the implementation and the testing of radio resources allocation algorithms to realize network slicing in the radio access segment of Wi-Fi networks. In particular, three steps need to be followed:
* Configure the environment parameters, such as the number of Wi-Fi STAs, required throughput in each slice and the dimensions of the room.
* Write a dynamic algorithm which allocates radio resources at each time slot, by receiving in input the run-time Key Performance Indicators (KPIs) of the network. There is no limit on the kind of algorithm which can be implemented, and also Machine Learning (ML) techniques are supported.
* Finally, when the simulation time is over, the experienced performance (i.e. throughput, error probability, latency, energy consumption and spectrum efficiency) can be accessed from a .csv file.

<p align="center"> 
<img src="https://github.com/matteonerini/5g-network-slicing-for-wifi-networks/blob/main/figs/scenario.png" width="50%">
</p>

## Description

This repository contains Python codes which call the relative *ns-3* C++ scripts, simulating the considered Wi-Fi scenario with different seeds and different initializations, if required.

To validate your own original network slicing algorithm through simulations you will need to use the files ```run_wifi.py``` and ```wifi.cc``` properly configured. Detailed instructions about it are provided in the Section Usage.

Instead, you can reproduce the results presented in the paper "5G Network Slicing for Wi-Fi Networks" with the additional files. More precisely:
* Launch ```run_wifi_1ch.py``` to reproduce the *single channel* approach. This file will call the ```wifi_1ch.cc``` *ns-3* script to simulate the today's Wi-Fi access technique, in which only one wireless channel is available for all the STAs connected to the AP. We suggest to use this as a reference for the evaluation of your original resources allocation algorithms.
* Launch ```run_wifi_static.py``` to reproduce the *static network slicing* approach. This file will call the ```wifi_static.cc``` *ns-3* script.
* Launch ```run_wifi_dynamic.py``` to reproduce the *dynamic network slicing* approach. This file will call the ```wifi_dynamic.cc``` *ns-3* script.


## Usage

In this section, you can find detailed instructions on how to use our framework to validate your network slicing algorithms through simulations in *ns-3*. First of all, execute the following steps to be able to use our codes:
* Install the *ns-3* network simulator in your machine following the instructions from the main website [nsnam.org](https://www.nsnam.org/).
* Download this repository as a .zip and extract it.
* Paste its content inside the ```scratch``` directory, which is inside the *ns-3* release directory, automatically created upon the *ns-3* installation.

Alternatively, you can download only the specific files you want to use and paste them in the ```scratch``` directory. Everything is now ready.

To launch a Python script, for example ```run_wifi.py```, open a terminal in the ```scratch``` directory and type:

```
python ./run_wifi.py
```

Please, note that all the Python scripts contained in this repository are written in Python 2.7. Thus, you will need this version to run them.

### Configuration of the ```run_wifi.py``` Script

Before to launch ```run_wifi.py```, make sure to properly set all the available options, including the ```ns3_script``` variable. Once launched, ```run_wifi.py``` will call the *ns-3* script indicated by ```ns3_script```, and will create a .csv file in which the output of the simulations will be registered.

### Configuration of the ```wifi.cc``` Script

The idea behind our framework is to create three wireless channels, one for each of the three network slices. Each channel is fully characterized by the following properties: the channel bandwidth, the channel number (given by the center frequency as in the *ns-3* [documentation](https://www.nsnam.org/docs/models/html/wifi-user.html)), the Guard Interval (GI), the Modulation and Coding Scheme (MCS) index and the transmission power. Thus, your algorithm should output suitable values for these properties. To integrate a slicing technique, two functions in the ```wifi.cc``` script must be modified:
* The function ```compute_channels``` must contain the algorithm which compute the initial channels' properties. At this stage, the devices have not started yet their transmissions. Thus, only the characteristics of the scenario can be taken as inputs (e.g. the number of connected STAs), while we do not have any information about the KPIs of the network.
* The function ```update_channels``` is called every interval of time *T* (*T* = 1 second in our setup) to update the channels' properties. Thus, it must contain the dynamic, smart algorithm which computes updated values of the channels' properties based on the real-time KPIs.
