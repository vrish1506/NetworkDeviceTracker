#! /bin/bash
DATE=`date | sed 's/ /_/g' | sed 's/:/_/g'`
PRODUCT_NAME="PRODUCT_"
PRODUCT_FULL_NAME=${PRODUCT_NAME}${DATE}".tar.gz"


tar -zcvf ${PRODUCT_FULL_NAME} source/product.py build.sh execute.sh
echo ${PRODUCT_FULL_NAME}

echo "Extracting...${PRODUCT_FULL_NAME}"

tar -zxvf ${PRODUCT_FULL_NAME}
