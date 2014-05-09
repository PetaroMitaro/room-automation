#!/bin/bash
if (($1 > 12))
then
	 hr=$(($1 - 12))
	echo "$hr:$2 p.m."
else
	hr=$1
	echo "$hr:$2 a.m."
fi
