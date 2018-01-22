#! /bin/bash
DATE=`date | sed 's/ /_/g' | sed 's/:/_/g'`
PRODUCT_NAME="PRODUCT_"
PRODUCT_FULL_NAME=${PRODUCT_NAME}${DATE}.tar

echo ${PRODUCT_FULL_NAME}

tar -cvf ${PRODUCT_FULL_NAME} /home/ubuntu/NetworkDeviceTracker/source/product.py /home/ubuntu/NetworkDeviceTracker/build.sh /home/ubuntu/NetworkDeviceTracker/execute.sh

if [ "$?" = "0" ]; then
    echo ".tar is created successfully"
else
    echo "error in creating .tar"
    exit 1
fi

tar -xf ${PRODUCT_FULL_NAME} -C /home/ubuntu/JenkinsQA-NetworkDeviceTracker


#tar -cf ${PRODUCT_FULL_NAME}/a.tar /home/ubuntu/qq/NetworkDeviceTracker/source/product.py /home/ubuntu/qq/NetworkDeviceTracker/build.sh /home/ubuntu/qq/NetworkDeviceTracker/execute.sh
#echo ${PRODUCT_FULL_NAME}

#echo "Extracting...${PRODUCT_FULL_NAME}"

#tar -zxvf ${PRODUCT_FULL_NAME}


