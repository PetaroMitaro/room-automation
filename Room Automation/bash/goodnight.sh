#!/bin/bash
lightState=$( sudo python ~/commands/fetchLightState.py )
echo $lightState
#ask arduino for light state

#turn light till light state is off
