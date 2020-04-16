#!/bin/bash

service filebeat start 

while true; do
pcapfiles=(./*.pcap)
        for ((i=0; i<${#pcapfiles[@]}; i++)); do
            if [ ${#pcapfiles[@]} -eq 2 ]
            then
                size=$(stat --format=%s ${pcapfiles[$i]})
                if [ $size -gt 2000000 ]
                then
                        echo "${pcapfiles[$i]}"
                        ./bin/cfm ${pcapfiles[$i]} ./results/
                        rm ${pcapfiles[$i]}
                        #filenamecsv="./results/${pcapfiles[$i]}_Flow.csv"
                        #echo "Predicting over dataset  $filenamecsv"

                        #python3 simple_randomforest.py $filenamecsv
                fi
                #echo "stat --format=%s ${pcapfiles[$i]}" | bash
            fi
        done
done
#echo "${#pcapfiles[@]}

bash /root/pcaps/process_results.sh
