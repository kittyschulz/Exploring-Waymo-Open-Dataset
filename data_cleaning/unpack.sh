!/bin/bash

# make new directory in instance
mkdir waymo_data

# copy tarballs from waymo bucket to instance
gsutil -m cp -R gs://waymo_open_dataset_v_1_0_0/training  waymo_data/
cd waymo_data/training

#unpack tarballs to instance and then delete tarball from instance
for i in {00..31}
do
  tar_filepath=$(printf "training_00%02d.tar" $i)
  echo "Working on ${tar_filepath}"
  tar -xvf ${tar_filepath}
  rm ${tar_filepath}
done

#upload TF records to bucket
gsutil -m cp waymo_data/training/*.tfrecord  gs://waymo-training-set

