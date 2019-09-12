#!/bin/bash

# mkdir waymo_data
# gsutil -m cp -R gs://waymo_open_dataset_v_1_0_0/training  waymo_data/
cd waymo_data/training

for i in {00..31}
do
  tar_filepath=$(printf "training_00%02d.tar" $i)
  echo "Working on ${tar_filepath}"
  # tar -xvf ${tar_filepath}
  # rm ${tar_filepath}
done
